import os
import youtube_services
import json

# 1 Read the list of the countries that we will be analyzing.
# 2 For every country in the countries list
# 2.1 collect the comments from the videos that re not null
# 2.2 Save the comments to CSVs with filenames in this format <country><videoName>.csv
COUNTRIES_LIST_FILENAME = 'allCountriesYTLinks.json'
# COUNTRIES_LIST_FILENAME = 'testList.json'
YT_VIDEO_TYPES_TO_INCLUDE = ["music-video"]
DATA_FOLDER = 'D:\GitHub Repositories\Eurovision data\Eurovision-Youtube-Comments\Data'
COUNTRIES_TO_ANALYZE_SEMI2 = ["San Marino", "Estonia", "Czech Republic", "Greece", "Austria", "Poland", "Moldova",
                              "Iceland", "Serbia", "Georgia", "Albania", "Portugal", "Bulgaria", "Finland", "Latvia", "Switzerland", "Denmark"]

COUNTRIES_TO_ANALYZE_SEMI1 = ["Lithuania", "Slovenia", "Russia", "Sweden", "Australia", "North Macedonia",
                              "Ireland", "Cyprus", "Norway", "Croatia", "Belgium", "Israel", "Romania", "Azerbaijan", "Ukraine", "Malta"]


def count_country_types(countriesDict, countries_to_include, video_type):
    countDict = {}
    for country, details in [(country, details) for country, details in countriesDict['countries'].items() if country in countries_to_include]:
        for yt_video_type, yt_video_url in [(name, video) for name, video in details['videos'].items() if name in video_type]:
            if not yt_video_url == '':
                if yt_video_type in countDict.keys():
                    countDict[yt_video_type] += 1
                else:
                    countDict[yt_video_type] = 1
    print(countDict)


#        countries_dict, video_types_to_include, data_folder)

def create_data_sets(countriesDict, video_types_to_include, data_folder):
    for country, details in countriesDict['countries'].items():
        country_folder_path = os.path.join(data_folder, country)
        os.mkdir(country_folder_path)
        for yt_video_type, yt_video_url in [(name, video) for name, video in details['videos'].items() if name in video_types_to_include]:
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
