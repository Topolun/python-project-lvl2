import argparse
from gendiff import formatters
import json
import yaml
import os


def get_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(
        '-f', '--format', type=choose_formatter,
        default='default', help='set format of output'
        )
    parser.add_argument(
        'first_file', type=load_file, help='first file for check'
        )
    parser.add_argument(
        'second_file', type=load_file, help='second file for check'
        )
    args = parser.parse_args()
    return args


def load_file(file):
    _, extension = os.path.splitext(file)
    if extension == '.json':
        with open(file) as result:
            return json.load(result)
    elif extension == '.yml' or extension == '.yaml':
        with open(file) as result:
            return yaml.safe_load(result)
    else:
        message = "'{}' is incorrect file extension. Please choose {}".format(
            extension, '.json or .yml or .yaml')
        raise argparse.ArgumentTypeError(message)


def choose_formatter(string):
    function = FORMATTERS.get(string)
    if function is None:
        message = "'{}' is incorrect formatter. Please choose from: {}".format(
            string, tuple(FORMATTERS.keys())
        )
        raise argparse.ArgumentTypeError(message)
    return function


FORMATTERS = {
    'default': formatters.default,
    'plain': formatters.plain,
    'json': formatters.json
    }
