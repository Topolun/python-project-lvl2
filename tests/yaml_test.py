from gendiff.engine import generate_diff
from gendiff.formatters import default

def test_compare_simple_yml_files_default_format():
    with open('./tests/fixtures/flat_file_result.txt') as correct_answer:
        assert generate_diff(
            './tests/fixtures/before.yml',
            './tests/fixtures/after.yml',
            default
            ) == correct_answer.read()
