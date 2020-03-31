from gendiff.generate_diff import find_differences
import json

def test_compare_json_files_json_format():
    with open('./tests/fixtures/advanced_file_result_json.json') as correct_answer:
        assert find_differences(
            './tests/fixtures/advanced_before.json',
            './tests/fixtures/advanced_after.json',
            format='json'
            ) == json.load(correct_answer)
