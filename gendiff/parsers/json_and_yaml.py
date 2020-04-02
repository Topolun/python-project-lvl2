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
