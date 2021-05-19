import organizeData
import re
from collections import Counter
countriesList = organizeData.load_countries_list(
    organizeData.COUNTRIES_LIST_FILENAME)

TEST_DATA_PATH = "D:\GitHub Repositories\Eurovision data\Data\San Marino_rehersal2.csv"
TEST_DATA_PATH2 = "D:\GitHub Repositories\Eurovision data\Data\San Marino_musicVideo.csv"

listOfCountryNames = ["Lithuania", "Slovenia", "Russia", "Sweden", "Australia", "North Macedonia", "Ireland",
                      "Cyprus", "Norway", "Croatia", "Belgium", "Israel", "Romania", "Azerbaijan", "Ukraine", "Malta", "San Marino", "Estonia", "Czech Republic", "Greece", "Austria", "Poland", "Moldova", "Iceland",
                      "Serbia", "Georgia", "Albania", "Portugal", "Bulgaria", "Finalnd", "Latvia", "Switzerland", "Denmark", "France", 'Germany', 'Italy', 'Spain', 'Netherlands']
listOfCountryNames = [x.lower() for x in listOfCountryNames]


def analyze_file(file_path):
    words = open(TEST_DATA_PATH2, "r", encoding='utf-16').read().split()
    words = [word.lower()
             for word in words if word.lower() in listOfCountryNames]
    print(Counter(words).most_common(150))


analyze_file(TEST_DATA_PATH)
