import json


def recieve_json(first_file, second_file):
    first = json.load(open(first_file))
    second = json.load(open(second_file))
    result = '{\n'
    for key, value in first.items():
        checker = second.pop(key, 'not_found')
        if checker == 'not_found':
            result += '- {}: {}\n'.format(key, value)
        elif first.get(key) == checker:
            result += '  {}: {}\n'.format(key, value)
        else:
            result += '+ {}: {}\n'.format(key, checker)
            result += '- {}: {}\n'.format(key, value)
    for key, value in second.items():
        result += '+ {}: {}\n'.format(key, value)
    return result + '}'
