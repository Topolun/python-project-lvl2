from gendiff.engine import generate_diff
import json
from gendiff.formatters import json as format_json

def test_compare_json_files_json_format():
    with open('./tests/fixtures/advanced_file_result_json.json') as correct_answer:
        assert generate_diff(
            './tests/fixtures/advanced_before.json',
            './tests/fixtures/advanced_after.json',
            format_json
            ) == json.load(correct_answer)
