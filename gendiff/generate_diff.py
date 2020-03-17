import json as json1
import yaml as yaml1
from os.path import splitext
from gendiff.parsers import compare


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


def find_differences(first_file, second_file):
    first, second = extract_files(first_file, second_file)
    result = compare(first, second)
    return render(result)


def render(items, otstup=0):
    result = '{\n'
    offset = '    ' * otstup
    for item in items:
        result_of_compare = add_symbols(item['Action'])
        key = item['Key']
        value = item['Value']
        if type(value) is list:
            result += '{}{}{}: {}'.format(
                offset, result_of_compare, key, render(value, otstup + 1)
                )
        elif type(value) is dict:
            result += '{}{}{}: {}'.format(
                offset, result_of_compare, key, print_dict(value, otstup + 1)
                )
        else:
            result += '{}{}{}: {}'.format(
                offset, result_of_compare, key, value
                )
        result += '\n'
    result += offset + '}'
    return result


def print_dict(dictionary, otstup):
    result = '{\n'
    offset = '    ' * otstup
    for key, value in dictionary.items():
        if type(value) is dict:
            result += '{}    {}: {}'.format(
                offset, key, print_dict(value, otstup + 1)
                )
        else:
            result += '{}    {}: {}'.format(offset, key, value)
        result += '\n'
    result += offset + '}'
    return result


def add_symbols(data):
    if data == '+':
        return '  + '
    elif data == '-':
        return '  - '
    else:
        return '    '
