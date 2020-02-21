import yaml


def recieve_yaml(first_file, second_file):
    first = yaml.safe_load(open(first_file))
    second = yaml.safe_load(open(second_file))
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
