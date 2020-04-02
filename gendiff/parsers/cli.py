import argparse
from gendiff import formatters


def choose_formatter(string):
    function = FORMATTERS.get(string)
    if function is None:
        message = "'{}' is incorrect formatter. Please choose from: {}".format(
            string, tuple(FORMATTERS.keys())
        )
        raise argparse.ArgumentTypeError(message)
    return function


def cli():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(
        '-f', '--format', type=choose_formatter,
        default='default', help='set format of output'
        )
    parser.add_argument('first_file', type=str, help='first file for check')
    parser.add_argument('second_file', type=str, help='second file for check')
    args = parser.parse_args()
    return args


FORMATTERS = {
    'default': formatters.default,
    'plain': formatters.plain,
    'json': formatters.json
    }
