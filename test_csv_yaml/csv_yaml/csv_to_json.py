import csv
import json
from contextlib import ExitStack

"""
将csv文件转换成json
"""
profileList = []


def FromCsvToJson(csv_path):
    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)  ##########################
        for row in reader:
            profileList.append(dict(row))
        return profileList


if __name__ == '__main__':
    print(FromCsvToJson(r'F:\2\python\pytestProject\test_csv_yaml\csv_yaml\data.csv'))