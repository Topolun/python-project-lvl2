def generate_diff(first_file, second_file, format):
    result = compare(first_file, second_file)
    return format(result)


def compare(first, second):
    result = []
    for key, value in first.items():
        checker = second.pop(key, 'not_found')
        if checker == 'not_found':
            result.append(deleted_node(key, value))
        elif value == checker:
            result.append(unchanged_node(key, value))
        else:
            if type(value) is dict and type(checker) is dict:
                result.append(nested_node(key, compare(value, checker)))
            else:
                result.append(changed_node(key, (checker, value)))
    for key, value in second.items():
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
