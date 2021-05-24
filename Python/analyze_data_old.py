from collections import Counter
import os
import json

COUNTRIES_TO_LOOK_FOR_SEMI1 = ["Lithuania", "Slovenia", "Russia", "Sweden", "Australia", "Macedonia", "Ireland", "Italy", "Germany", "Netherlands",
                               "Cyprus", "Norway", "Croatia", "Belgium", "Israel", "Romania", "Azerbaijan", "Ukraine", "Malta"]

COUNTRIES_TO_LOOK_FOR_SEMI2 = ["San Marino", "Estonia", "Czech Republic", "Greece", "Austria", "Poland", "Moldova", "Iceland",
                               "Serbia", "Georgia", "Albania", "Portugal", "Bulgaria", "Finland", "Latvia", "Switzerland", "Denmark", "France", "Spain", "United Kingdom"]

COUNTRIES_TO_ANALYZE_SEMI2 = ["San Marino", "Estonia", "Czech Republic", "Greece", "Austria", "Poland", "Moldova", "Iceland",
                              "Serbia", "Georgia", "Albania", "Portugal", "Bulgaria", "Finland", "Latvia", "Switzerland", "Denmark"]

COUNTRIES_TO_ANALYZE_SEMI1 = ["Lithuania", "Slovenia", "Russia", "Sweden", "Australia", "Macedonia", "Ireland",
                              "Cyprus", "Norway", "Croatia", "Belgium", "Israel", "Romania", "Azerbaijan", "Ukraine", "Malta"]


# Lets make a list of tuples like : (<CountryName>, [List of possible names to look for])


VIDEO_TYPES_TO_INCLUDE = ['music-video']

DATA_FOLDER = "D:\GitHub Repositories\Eurovision data\Eurovision-Youtube-Comments\Data"
SCORES = [12, 10, 8, 7, 6, 5, 4, 3, 2, 1]


def analyze_file(file_path, words_to_look_for):
    words = open(file_path, "r", encoding='utf-16').read().split()
    return [word.lower()
            for word in words if word.lower() in words_to_look_for]


def analyze_country(country, words_to_look_for, video_types_to_include):
    word_list = []
    words_to_look_for.remove(country.lower())

    for video_type in video_types_to_include:
        filepath = os.path.join(DATA_FOLDER, country,
                                f'{country}_{video_type}.csv')
        word_list = word_list + analyze_file(filepath, words_to_look_for)
    return Counter(word_list)


def analyze_countries(countries, countries_to_look_for, video_types_to_include):
    country_frequency_list = {}
    for country in countries:
        country_frequency_list[country] = analyze_country(
            country, countries_to_look_for, VIDEO_TYPES_TO_INCLUDE).most_common(10)
    return country_frequency_list


def determine_one_country_score(country_to_score, countries_frequency_list):
    results_dict = {}
    for country, frequency_list in countries_frequency_list.items():
        for (name, score) in frequency_list:
            if(name == country_to_score):
                results_dict[country] = score
    return results_dict


def determine_countries_score(countries, countries_frequency_list):
    result_dict = {}
    for country in countries:
        result_dict[country] = determine_one_country_score(
            country.lower(), countries_frequency_list)
    return result_dict


def determine_country_points_from_score(country_scores):
    sorted_tuples = sorted(country_scores.items(),
                           key=lambda item: item[1])[:10]
    sorted_tuples.reverse()
    return {country: SCORES[i] for i, (country, score) in enumerate(sorted_tuples)}


def determine_countries_points_from_score(countries_scores):
    result_dict = {}
    for country, country_scores in countries_scores.items():
        result_dict[country] = determine_country_points_from_score(
            country_scores)
    return result_dict


def determine_winner(countries_points):
    result_dict = {}
    for points_from_country, points in countries_points.items():
        print(points_from_country, points)
        for points_to_country, point in points.items():
            if points_to_country not in result_dict:
                result_dict[points_to_country] = point
            else:
                result_dict[points_to_country] += point
    return result_dict


def make_json(dict, path, filename):
    with open(os.path.join(path, f'{filename}.json'), "w", newline="\n") as outfile:
        json.dump(dict, outfile, indent=4)


def sort_winners(dict):
    sorted_tuples = sorted(dict.items(),
                           key=lambda item: item[1])
    sorted_tuples.reverse()
    return {country: score for (country, score) in sorted_tuples}


countries_to_look_for_lower = [x.lower() for x in COUNTRIES_TO_LOOK_FOR_SEMI1]
country_frequency_list = analyze_countries(
    COUNTRIES_TO_ANALYZE_SEMI1, countries_to_look_for_lower, VIDEO_TYPES_TO_INCLUDE)
print(country_frequency_list)


countries_score = determine_countries_score(
    COUNTRIES_TO_ANALYZE_SEMI1, country_frequency_list)
countries_points = determine_countries_points_from_score(countries_score)
print(countries_points)
winner_dict = determine_winner(countries_points)
# print(winner_dict)
print(sort_winners(winner_dict))


#print(determine_points(country_frequency_list['San Marino']))
#make_json(determine_points_country_list(country_frequency_list), DATA_FOLDER, 'pointsFromCountryToCountry')
#make_json(countries_result, DATA_FOLDER, 'results')

# analyze_file(TEST_DATA_PATH)
