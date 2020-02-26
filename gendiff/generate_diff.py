from os.path import splitext
from gendiff.parsers import yaml, json


def find_differences(first_file, second_file):
    _, first_extension = splitext(first_file)
    if first_extension == '.json':
        return json.recieve_json(first_file, second_file)
    elif first_extension == '.yml':
        return yaml.recieve_yaml(first_file, second_file)
    else:
        print('Wrong data')
