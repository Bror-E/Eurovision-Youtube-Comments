import os
import youtube_services
import json

# 1 Read the list of the countries that we will be analyzing.
# 2 For every country in the countries list
# 2.1 collect the comments from the videos that re not null
# 2.2 Save the comments to CSVs with filenames in this format <country><videoName>.csv
COUNTRIES_LIST_FILENAME = 'testList.json'
YT_VIDEO_TYPES_TO_INCLUDE = ['musicVideo', 'rehersal2']
DATA_FOLDER = 'D:\GitHub Repositories\Eurovision data\Data'


def load_countries_list(filename):
    with open(filename) as f:
        data = json.load(f)
    return data


def create_data_sets(countriesDict):
    for country, details in countriesDict['countries'].items():
        country_folder_path = os.path.join(DATA_FOLDER, country)
        os.mkdir(country_folder_path)
        for yt_video_type, yt_video_url in [(name, video) for name, video in details['videos'].items() if name in YT_VIDEO_TYPES_TO_INCLUDE]:
            print(
                f"Getting comments from : {country}'s, {yt_video_type} ({yt_video_url})")
            youtube_services.get_comments(part="snippet",
                                          maxResults=100,
                                          textFormat="plainText",
                                          order="time",
                                          videoId=youtube_services.get_video_id_from_url(
                                              yt_video_url),
                                          csv_filename=f'{country}_{yt_video_type}.csv',
                                          csv_path=country_folder_path)


#countriesDict = load_countries_list(COUNTRIES_LIST_FILENAME)
# create_data_sets(countriesDict)
