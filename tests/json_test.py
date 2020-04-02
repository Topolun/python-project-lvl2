from gendiff.engine import generate_diff
from gendiff.formatters import default


def test_compare_simple_json_files_default_format():
    with open('./tests/fixtures/flat_file_result.txt') as correct_answer:
        assert generate_diff(
            './tests/fixtures/before.json',
            './tests/fixtures/after.json',
            default
            ) == correct_answer.read()