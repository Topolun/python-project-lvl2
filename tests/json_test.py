from gendiff.engine import generate_diff
from gendiff.formatters import default
from gendiff.parsers import load_file


def test_compare_simple_json_files_default_format():
    with open('./tests/fixtures/flat_file_result.txt') as correct_answer:
        assert generate_diff(
            load_file('./tests/fixtures/before.json'),
            load_file('./tests/fixtures/after.json'),
            default
            ) == correct_answer.read()