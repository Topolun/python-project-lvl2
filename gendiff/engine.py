from gendiff.parsers import load_file


def generate_diff(first_file, second_file, format):
    first = load_file(first_file)
    second = load_file(second_file)
    if not first or not second:
        return 'File extension is not JSON or YML'
    result = compare(first, second)
    return format(result)


def compare(first, second):
    result = []
    for key, value in first.items():
        checker = second.pop(key, 'not_found')
        if checker == 'not_found':
            result.append(deleting(key, value))
        elif value == checker:
            result.append(add_equal(key, value))
        else:
            if type(value) is dict and type(checker) is dict:
                result.append(add_not_equal(key, compare(value, checker)))
            else:
                result.append(add_changes(key, checker, value))
    for key, value in second.items():
        result.append(add_new(key, value))
    return result


def add_new(key, value):
    return {'Action': '+', 'Key': key, 'Value': value}


def deleting(key, value):
    return {'Action': '-', 'Key': key, 'Value': value}


def add_equal(key, value):
    return {'Action': '=', 'Key': key, 'Value': value}


def add_not_equal(key, value):
    return {'Action': '!=', 'Key': key, 'Value': value}


def add_changes(key, value1, value2):
    changes = (value1, value2)
    return {'Action': '+-', 'Key': key, 'Value': changes}
