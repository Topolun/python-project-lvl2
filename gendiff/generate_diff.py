from gendiff.parsers import compare, load_file
from gendiff.formatters import render, render_plain, render_json


def find_differences(first_file, second_file, format='default'):
    first = load_file(first_file)
    second = load_file(second_file)
    if not first or not second:
        return 'File extension is not JSON or YML'
    result = compare(first, second)
    if format == 'plain':
        return render_plain(result)
    elif format == 'json':
        return render_json(result)
    else:
        return render(result)
