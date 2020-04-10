import json


def format(item):
    return json.dumps(prepare_for_json(item))


def prepare_for_json(items):
    result = {}
    for item in items:
        action = item['STATUS']
        key = item['KEY']
        value = item['VALUE']
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
            result[key] = prepare_for_json(value)
    return result


def add_to_dict(key_name, dictionary, key, value):
    result = dictionary.setdefault(key_name, {})
    result[key] = value
    return result
