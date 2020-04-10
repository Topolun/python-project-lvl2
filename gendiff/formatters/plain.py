from gendiff import engine


def format(data, path=''):
    result = ''
    if isinstance(data, list):
        for item in data:
            status = item[engine.STATUS]
            key = item[engine.KEY]
            value = item[engine.VALUE]
            if status == engine.NODE_NEW or status == engine.NODE_DELETED:
                way = "Property '{}{}' {}\n".format(
                    path, key, insert_description(status, value)
                    )
            elif status == engine.NODE_CHANGED:
                way = "Property '{}{}' {}\n".format(
                    path, key, insert_description(status, value)
                    )
            else:
                new_path = path + '{}.'.format(key)
                way = format(value, new_path)
            result += way
    return result


def insert_description(status, value):
    if status == engine.NODE_DELETED:
        return 'was removed'
    elif status == engine.NODE_CHANGED:
        return "was changed. From '{}' to '{}'".format(
            check_result(value[1]), check_result(value[0])
            )
    return "was added with value: '{}'".format(check_result(value))


def check_result(data):
    if isinstance(data, list) or isinstance(data, dict):
        return 'complex value'
    return data
