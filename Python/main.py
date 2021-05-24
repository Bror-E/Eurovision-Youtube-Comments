import json
import os
import analyze_data_tuples
import organize_data

COUNTRIES_LIST_FILENAME = 'all_countries_youtube_links.json'
COUNTRIES_IN_FINALE = ["Netherlands", "France", "Germany", "Italy", "Spain", "United Kingdom", "Lithuania", "Russia",
                       "Sweden", "Cyprus", "Norway", "Belgium", "Israel", "Azerbaijan", "Ukraine", "Malta", "San Marino", "Greece", "Moldova", "Iceland", "Serbia", "Albania", "Portugal", "Bulgaria", "Finland", "Switzerland"]

COUNTRIES_ALLOWED_TO_VOTE = ["Lithuania", "Slovenia", "Russia", "Sweden", "Australia", "Macedonia", "Ireland", "Italy", "Germany", "Netherlands",
                             "Cyprus", "Norway", "Croatia", "Belgium", "Israel", "Romania", "Azerbaijan", "Ukraine", "Malta", "San Marino", "Estonia", "Czech Republic", "Greece", "Austria", "Poland", "Moldova", "Iceland",
                             "Serbia", "Georgia", "Albania", "Portugal", "Bulgaria", "Finland", "Latvia", "Switzerland", "Denmark", "France", "Spain", "United Kingdom"]


DATA_FOLDER_SEMI = "D:\GitHub Repositories\Eurovision data\Eurovision-Youtube-Comments\Data\Semi Finals"
DATA_FOLDER_FINAL = "D:\GitHub Repositories\Eurovision data\Eurovision-Youtube-Comments\Data\Final"

VIDEO_TYPES_TO_INCLUDE = ['music-video', 'semi-final']


def get_data(countries_filename, data_folder, countries_to_get_data, video_types_to_include):
    countries_dict = load_countries_list(countries_filename)
    countries_dict['countries'] = {country: videoes for country,
                                   videoes in countries_dict['countries'].items() if country in countries_to_get_data}
    organize_data.create_data_sets(
        countries_dict, video_types_to_include, data_folder)


def load_countries_list(filename):
    with open(filename) as f:
        data = json.load(f)
    return data


def get_countries_names(data_folder):
    with open(os.path.join(data_folder, 'countries_names.json'), "r", encoding='utf-8') as json_file:
        return json.load(json_file)


def make_json(dict, path, filename):
    with open(os.path.join(path, f'{filename}.json'), "w", newline="\n") as outfile:
        json.dump(dict, outfile, indent=4)


def analyze_data(data_folder, countries_competing, videoes_types_to_include):
    # Read the json of country names to a dictionary
    country_names = get_countries_names(data_folder)
    countries_points = analyze_data_tuples.get_countries_points(
        country_names, countries_competing, data_folder, videoes_types_to_include)
    make_json(countries_points, DATA_FOLDER_FINAL, 'country_points')
    counted = analyze_data_tuples.count_up_all_points(countries_points)
    print(counted)
    print('We have a winner!')
    print(f'The winner is: {counted[0]}')
    make_json(counted, DATA_FOLDER_FINAL, 'winner')


if __name__ == "__main__":
    # get_data(COUNTRIES_LIST_FILENAME, DATA_FOLDER_FINAL,
    #         COUNTRIES_IN_FINALE, VIDEO_TYPES_TO_INCLUDE)
    analyze_data(DATA_FOLDER_FINAL, COUNTRIES_IN_FINALE,
                 VIDEO_TYPES_TO_INCLUDE)
