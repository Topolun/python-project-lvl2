import json
import yaml
from os.path import splitext
from gendiff.parsers import compare
from gendiff.formatters import render, render_plain, render_json


def extract_files(first_file, second_file):
    _, first_extension = splitext(first_file)
    if first_extension == '.json':
        first = json.load(open(first_file))
        second = json.load(open(second_file))
        return first, second
    elif first_extension == '.yml':
        first = yaml.safe_load(open(first_file))
        second = yaml.safe_load(open(second_file))
        return first, second


def find_differences(first_file, second_file, format='standart'):
    first, second = extract_files(first_file, second_file)
    result = compare(first, second)
    if format == 'plain':
        return render_plain(result)
    elif format == 'json':
        return render_json(result)
    else:
        return render(result)
