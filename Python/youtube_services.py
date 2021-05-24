
import requests
import json
from csv import writer
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
import os
import codecs


test_url = "https://www.youtube.com/watch?v=i6r3MMMAo3Q"
API_KEY_FILENAME = "youtubeDataV3.txt"


def get_api_key(filename):
    with open(filename) as f:
        key = f.readline()
    return key


def build_youtube_data_v3_service(apiKeyFilename):
    key = get_api_key(apiKeyFilename)
    return build("youtube", "v3", developerKey=key)


def get_video_id_from_url(url):
    u_pars = urlparse(url)
    quer_v = parse_qs(u_pars.query).get("v")
    if quer_v:
        return quer_v[0]
    pth = u_pars.path.split("/")
    if pth:
        return pth[-1]


def get_comments(part="snippet",
                 maxResults=100,
                 textFormat="plainText",
                 order="time",
                 videoId='',
                 csv_filename="empty",
                 csv_path=''):
    comments = []
    service = build_youtube_data_v3_service(API_KEY_FILENAME)
    response = service.commentThreads().list(
        part=part,
        maxResults=maxResults,
        textFormat=textFormat,
        order=order,
        videoId=videoId
    ).execute()
    counter = 0
    while response:  # this loop will continue to run until you max out your quota
        print(f'Getting comments {counter} -> {counter+maxResults}')
        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"].rstrip(
                '\n')
            comments.append(comment)
            with codecs.open(os.path.join(csv_path, csv_filename), "a+", encoding="utf-16") as f:
                csv_writer = writer(f)
                csv_writer.writerow([comment])
        if "nextPageToken" in response:
            response = service.commentThreads().list(
                part=part,
                maxResults=maxResults,
                textFormat=textFormat,
                order=order,
                videoId=videoId,
                pageToken=response["nextPageToken"]
            ).execute()
        else:
            break
        counter += maxResults
