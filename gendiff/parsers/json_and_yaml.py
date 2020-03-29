import json
import yaml
from os.path import splitext


def load_file(file):
    _, first_extension = splitext(file)
    if first_extension == '.json':
        with open(file) as result:
            return json.load(result)
    elif first_extension == '.yml':
        with open(file) as result:
            return yaml.safe_load(result)
    else:
        return False


def compare(first, second):
    result = []
    for key, value in first.items():
        checker = second.pop(key, 'not_found')
        if checker == 'not_found':
            result.append(deleting(key, value))
        elif value == checker:
            result.append(add_equal(key, value))
        else:
            if type(value) is dict and type(checker) is dict:
                result.append(add_not_equal(key, compare(value, checker)))
            else:
                result.append(add_changes(key, checker, value))
    for key, value in second.items():
        result.append(add_new(key, value))
    return result


def add_new(key, value):
    return {'Action': '+', 'Key': key, 'Value': value}


def deleting(key, value):
    return {'Action': '-', 'Key': key, 'Value': value}


def add_equal(key, value):
    return {'Action': '=', 'Key': key, 'Value': value}


def add_not_equal(key, value):
    return {'Action': '!=', 'Key': key, 'Value': value}


def add_changes(key, value1, value2):
    changes = (value1, value2)
    return {'Action': '+-', 'Key': key, 'Value': changes}
