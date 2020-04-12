from gendiff import engine


def format(items, level=0):
    result = '{\n'
    offset = '    ' * level
    for item in items:
        status = item[engine.STATUS]
        result_of_compare = add_symbols(status)
        key = item[engine.KEY]
        value = item[engine.VALUE]
        if status == engine.NODE_NESTED:
            result += '{}{}{}: {}'.format(
                offset, result_of_compare, key, format(value, level + 1)
                )
        elif isinstance(value, dict):
            result += '{}{}{}: {}'.format(
                offset, result_of_compare, key, print_dict(value, level + 1)
                )
        elif status == engine.NODE_CHANGED:
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
        if isinstance(value, dict):
            result += '{}    {}: {}'.format(
                offset, key, print_dict(value, level + 1)
                )
        else:
            result += '{}    {}: {}'.format(offset, key, value)
        result += '\n'
    result += offset + '}'
    return result


def add_symbols(data):
    if data == engine.NODE_NEW:
        return '  + '
    elif data == engine.NODE_DELETED:
        return '  - '
    else:
        return '    '
