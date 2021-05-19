import json
"""
    Just some basic data and functions to create files that contain the datasets of countries that
"""

countriesSemi1 = ["Lithuania", "Slovenia", "Russia", "Sweden", "Australia", "North Macedonia", "Ireland",
                  "Cyprus", "Norway", "Croatia", "Belgium", "Israel", "Romania", "Azerbaijan", "Ukraine", "Malta"]
countriesSemi2 = ["San Marino", "Esonia", "Czech Republic", "Greece", "Austria", "Poland", "Moldova", "Iceland",
                  "Serbia", "Georgia", "Albania", "Portugal", "Bulgaria", "Finalnd", "Latvia", "Switzerland", "Denmark"]

countriesFinal = ["Belgium", "Cyprus", "Israel", "Malta", "Russia", "Spain", "United Kingdom",
                  "Azerbaijan", "France", "Germany", "Italy", "Lithuania", "Norway", "Sweden", "Ukraine", "Netherlands"]

allCountries = ["Lithuania", "Slovenia", "Russia", "Sweden", "Australia", "North Macedonia", "Ireland",
                "Cyprus", "Norway", "Croatia", "Belgium", "Israel", "Romania", "Azerbaijan", "Ukraine", "Malta", "San Marino", "Estonia", "Czech Republic", "Greece", "Austria", "Poland", "Moldova", "Iceland",
                "Serbia", "Georgia", "Albania", "Portugal", "Bulgaria", "Finalnd", "Latvia", "Switzerland", "Denmark", "France", "Germany", "Italy", "Spain", "Netherlands", "United Kingdom"]


def make_dictionary(countries):
    return {'countries': {country: {"videos": {'music-video': '', 'rehersal-1': '', 'rehersal-2': '', 'semi-final': '', 'look-lab': '', 'music-first': ''}}
                          for country in countries}}


def make_json(dict, filename):
    with open(f'{filename}.json', "w", newline="\n") as outfile:
        json.dump(dict, outfile, indent=4)


# print(len(allCountries))
make_json(make_dictionary(allCountries), 'allCountriesYTLinks')
