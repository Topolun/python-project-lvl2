from gendiff import engine


def format(data, path=''):
    result = ''
    for key in data:
        status = data[key][engine.STATUS]
        value = data[key][engine.VALUE]
        if status == engine.NODE_UNCHANGED:
            continue
        elif status == engine.NODE_NEW or status == engine.NODE_DELETED:
            way = "Property '{}{}' {}\n".format(
                path, key, insert_description(status, value)
                )
        elif status == engine.NODE_CHANGED:
            way = "Property '{}{}' {}\n".format(
                path, key, insert_description(
                    status, value, data[key][engine.OLD_VALUE]
                    )
                )
        elif status == engine.NODE_UNCHANGED:
            continue
        else:
            new_path = path + '{}.'.format(key)
            way = format(value, new_path)
        result += way
    return result


def insert_description(status, value, old_value=None):
    if status == engine.NODE_DELETED:
        return 'was removed'
    elif status == engine.NODE_CHANGED:
        return "was changed. From '{}' to '{}'".format(
            check_result(old_value), check_result(value)
            )
    return "was added with value: '{}'".format(check_result(value))


def check_result(data):
    if isinstance(data, list) or isinstance(data, dict):
        return 'complex value'
    return data
