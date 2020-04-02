from gendiff.engine import generate_diff
from gendiff.formatters import default


def test_compare_yml_files_default_format():
    with open('./tests/fixtures/advanced_file_result.txt') as correct_answer:
        assert generate_diff(
            './tests/fixtures/advanced_before.yml',
            './tests/fixtures/advanced_after.yml',
            default
            ) == correct_answer.read()
