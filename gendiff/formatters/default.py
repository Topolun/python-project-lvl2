def format(items, level=0):
    result = '{\n'
    offset = '    ' * level
    for item in items:
        result_of_compare = add_symbols(item['STATUS'])
        key = item['KEY']
        value = item['VALUE']
        if type(value) is list:
            result += '{}{}{}: {}'.format(
                offset, result_of_compare, key, format(value, level + 1)
                )
        elif type(value) is dict:
            result += '{}{}{}: {}'.format(
                offset, result_of_compare, key, print_dict(value, level + 1)
                )
        else:
            if type(value) is tuple:
                result += '{}  + {}: {}\n'.format(offset, key, value[0])
                result += '{}  - {}: {}'.format(offset, key, value[1])
            else:
                result += '{}{}{}: {}'.format(
                    offset, result_of_compare, key, value
                    )
        result += '\n'
    result += offset + '}'
    return result


def print_dict(dictionary, level):
    result = '{\n'
    offset = '    ' * level
    for key, value in dictionary.items():
        if type(value) is dict:
            result += '{}    {}: {}'.format(
                offset, key, print_dict(value, level + 1)
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
