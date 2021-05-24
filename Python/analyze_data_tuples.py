from collections import Counter
from genericpath import getctime
import os
import json

SCORES = [12, 10, 8, 7, 6, 5, 4, 3, 2, 1]


def count_up_all_points(all_countries_points):
    results_dict = {}
    for country_giving_points, points in all_countries_points.items():
        for (country_recieving_points, point, frequency) in points:
            if country_recieving_points not in results_dict:
                results_dict[country_recieving_points] = point
            else:
                results_dict[country_recieving_points] += point
    return list(reversed(sorted([(country, score) for country, score in results_dict.items()], key=lambda x: x[1])))


def get_countries_points(countries, countries_to_analyze, data_folder, video_types_to_include):
    results_dict = {}
    for country, country_names in countries.items():
        word_frequencies = get_a_countrys_word_frequency_in_others_videoes(
            country_names, countries_to_analyze, data_folder, video_types_to_include)
        results_dict[country] = determine_points_from_countrys_word_frequenies(
            country, word_frequencies)
        print(country, list((country, points)
              for (country, points, _) in results_dict[country][:10]))
    return results_dict


def determine_points_from_countrys_word_frequenies(country_name, word_frequencies):
    # Remove countries own name.
    word_frequencies = [x for x in word_frequencies if x[0] != country_name]
    word_frequencies = list(
        reversed(sorted(word_frequencies, key=lambda x: x[1])))
    return [(country, SCORES[i] if i < len(SCORES) else 0, frequency)
            for i, (country, frequency) in enumerate(word_frequencies)]


def find_number_of_occurences_of_words_in_file(file_path, words_to_look_for):
    # We'll see what Ill do about the encoding for the files that contain youtube data.
    words = open(file_path, "r", encoding='utf-16').read()
    return sum(words.count(word) for word in words_to_look_for)


def get_a_countrys_word_frequency_in_others_videoes(country_names, countries_to_analyze, data_folder, video_types_to_include):
    # We need to loop over all of the folders where we have data.
    # Then we need to find_number_of_occurences_of_words_in_file in each file, and add them together.
    country_frequency = []
    for country_in_finale in countries_to_analyze:
        frequency_of_words = 0
        for video_type in video_types_to_include:
            filepath = os.path.join(data_folder, country_in_finale,
                                    f'{country_in_finale}_{video_type}.csv')
            frequency_of_words = frequency_of_words + \
                find_number_of_occurences_of_words_in_file(
                    filepath, country_names)
        country_frequency.append((country_in_finale, frequency_of_words))
    return country_frequency
