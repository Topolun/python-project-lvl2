from gendiff.engine import generate_diff
from gendiff.formatters import default
from gendiff.cli import load_file


def test_compare_json_files_default_format():
    with open('./tests/fixtures/advanced_file_result.txt') as correct_answer:
        assert generate_diff(
            load_file('./tests/fixtures/advanced_before.json'),
            load_file('./tests/fixtures/advanced_after.json'),
            default
            ) == correct_answer.read()
