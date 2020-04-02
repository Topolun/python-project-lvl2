from gendiff.engine import generate_diff
from gendiff.formatters import plain


def test_compare_json_files_plain_format():
    with open('./tests/fixtures/advanced_file_result_plain.txt') as correct_answer:
        assert generate_diff(
            './tests/fixtures/advanced_before.json',
            './tests/fixtures/advanced_after.json',
            plain
            ) == correct_answer.read()
