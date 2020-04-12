import json
from gendiff import engine


def format(item):
    return json.dumps(prepare_for_json(item))


def prepare_for_json(items):
    result = {}
    for item in items:
        status = item[engine.STATUS]
        key = item[engine.KEY]
        value = item[engine.VALUE]
        if status == engine.NODE_NEW:
            result[key] = key_added(value)
        elif status == engine.NODE_DELETED:
            result[key] = key_deleted(value)
        elif status == engine.NODE_CHANGED:
            result[key] = key_replaced(value[0], value[1])
        elif status == engine.NODE_UNCHANGED:
            result[key] = key_unchanged(value)
        else:
            result[key] = key_changed(prepare_for_json(value))
    return result


def make_key(status):
    def add_a_key_value(value, old_value=False):
        if old_value:
            return {
                'STATUS': status, 'NEW_VALUE': value, "OLD_VALUE": old_value
                }
        return {'STATUS': status, 'VALUE': value}
    return add_a_key_value


key_added = make_key(engine.NODE_NEW)
key_deleted = make_key(engine.NODE_DELETED)
key_unchanged = make_key(engine.NODE_UNCHANGED)
key_replaced = make_key(engine.NODE_CHANGED)
key_changed = make_key(engine.NODE_NESTED)
