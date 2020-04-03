def generate_diff(first_file, second_file, format):
    result = compare(first_file, second_file)
    return format(result)


def compare(first, second):
    result = []
    keys_for_first = set(first.keys())
    keys_for_second = set(second.keys())
    for key, value in first.items():
        if key not in keys_for_second:
            result.append(deleted_node(key, value))
        elif value == second[key]:
            result.append(unchanged_node(key, value))
        else:
            if type(value) is dict and type(second[key]) is dict:
                result.append(nested_node(key, compare(value, second[key])))
            else:
                result.append(changed_node(key, (second[key], value)))
    for key, value in second.items():
        if key not in keys_for_first:
            result.append(new_node(key, value))
    return result


def make_node(status):
    return lambda key, value: {'STATUS': status, 'KEY': key, 'VALUE': value}


NODE_NEW = '+'
NODE_DELETED = '-'
NODE_UNCHANGED = '='
NODE_CHANGED = '+-'
NODE_NESTED = '!='

deleted_node = make_node(NODE_DELETED)
new_node = make_node(NODE_NEW)
unchanged_node = make_node(NODE_UNCHANGED)
changed_node = make_node(NODE_CHANGED)
nested_node = make_node(NODE_NESTED)
