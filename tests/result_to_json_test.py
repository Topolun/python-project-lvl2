from gendiff.engine import generate_diff
import json
from gendiff.formatters import json as format_json
from gendiff.parsers import load_file

def test_compare_json_files_json_format():
    with open('./tests/fixtures/advanced_file_result_json.json') as correct_answer:
        assert json.loads(
                generate_diff(
                load_file('./tests/fixtures/advanced_before.json'),
                load_file('./tests/fixtures/advanced_after.json'),
                format_json
                )
            ) == json.load(correct_answer)
