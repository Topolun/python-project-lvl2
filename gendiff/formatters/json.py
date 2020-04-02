def format(items, unpack=''):
    result = {}
    for item in items:
        action = item['Action']
        key = item['Key']
        value = item['Value']
        if action == '+':
            result['added'] = add_to_dict('added', result, key, value)
        elif action == '-':
            result['deleted'] = add_to_dict('deleted', result, key, value)
        elif action == '+-':
            result['added'] = add_to_dict('added', result, key, value[0])
            result['deleted'] = add_to_dict('deleted', result, key, value[1])
        elif action == '=':
            result[key] = value
        else:
            result[key] = format(value)
    return result


def add_to_dict(key_name, dictionary, key, value):
    result = dictionary.setdefault(key_name, {})
    result[key] = value
    return result
