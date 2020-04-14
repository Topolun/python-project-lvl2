STATUS = 'STATUS'
KEY = 'KEY'
VALUE = 'VALUE'
OLD_VALUE = 'OLD_VALUE'

NODE_NEW = 'added'
NODE_DELETED = 'deleted'
NODE_UNCHANGED = 'unchanged'
NODE_CHANGED = 'replaced'
NODE_NESTED = 'changed'


def generate_diff(first_file, second_file, format):
    result = compare(first_file, second_file)
    return format(result)


def compare(first, second):
    result = {}
    keys_for_first = first.keys()
    keys_for_second = second.keys()
    for key, value in first.items():
        if key not in keys_for_second:
            result[key] = key_deleted(value)
        elif value == second[key]:
            result[key] = key_unchanged(value)
        elif isinstance(value, dict) and isinstance(value, dict):
            result[key] = key_changed(compare(value, second[key]))
        else:
            result[key] = key_replaced(second[key], value)
    for key, value in second.items():
        if key not in keys_for_first:
            result[key] = key_added(value)
    return result


def make_key(status):
    def add_a_key_value(value, old_value=False):
        if old_value:
            return {
                STATUS: status, VALUE: value, OLD_VALUE: old_value
                }
        return {STATUS: status, VALUE: value}
    return add_a_key_value


key_added = make_key(NODE_NEW)
key_deleted = make_key(NODE_DELETED)
key_unchanged = make_key(NODE_UNCHANGED)
key_replaced = make_key(NODE_CHANGED)
key_changed = make_key(NODE_NESTED)
