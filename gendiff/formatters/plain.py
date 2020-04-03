def format(data, path=''):
    result = ''
    if type(data) == list:
        for item in data:
            action = item['STATUS']
            key = item['KEY']
            value = item['VALUE']
            if action == '+' or action == '-':
                way = "Property '{}{}' {}\n".format(
                    path, key, insert_description(action, value)
                    )
            elif action == '+-':
                way = "Property '{}{}' {}\n".format(
                    path, key, insert_description(action, value)
                    )
            else:
                a = path + '{}.'.format(key)
                way = format(value, a)
            result += way
    return result


def insert_description(action, value):
    if action == '-':
        return 'was removed'
    elif action == '+-':
        return "was changed. From '{}' to '{}'".format(
            check_result(value[1]), check_result(value[0])
            )
    return "was added with value: '{}'".format(check_result(value))


def check_result(data):
    if type(data) == list or type(data) == dict:
        return 'complex value'
    return data
