import json as json1
import yaml as yaml1
from os.path import splitext
from gendiff.parsers import compare
from gendiff.formatters import render_plain
from gendiff.formatters import render


def extract_files(first_file, second_file):
    _, first_extension = splitext(first_file)
    if first_extension == '.json':
        first = json1.load(open(first_file))
        second = json1.load(open(second_file))
        return first, second
    elif first_extension == '.yml':
        first = yaml1.safe_load(open(first_file))
        second = yaml1.safe_load(open(second_file))
        return first, second


def find_differences(first_file, second_file, format='standart'):
    first, second = extract_files(first_file, second_file)
    result = compare(first, second)
    if format == 'plain':
        return render_plain(result)
    return render(result)
