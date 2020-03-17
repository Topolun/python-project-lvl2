def compare(first, second):
    a = []
    for key, value in first.items():
        checker = second.pop(key, 'not_found')
        if checker == 'not_found':
            a.append(deleting(key, value))
        elif value == checker:
            a.append(add_equal(key, value))
        else:
            if type(value) is dict and type(checker) is dict:
                a.append(add_not_equal(key, compare(value, checker)))
            else:
                a.append(add_new(key, checker))
                a.append(deleting(key, value))
    for key, value in second.items():
        a.append(add_new(key, value))
    return a


def add_new(key, value):
    return {'Action': '+', 'Key': key, 'Value': value}


def deleting(key, value):
    return {'Action': '-', 'Key': key, 'Value': value}


def add_equal(key, value):
    return {'Action': '=', 'Key': key, 'Value': value}


def add_not_equal(key, value):
    return {'Action': '!=', 'Key': key, 'Value': value}
