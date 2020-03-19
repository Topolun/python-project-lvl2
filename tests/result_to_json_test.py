from gendiff.generate_diff import find_differences
import json

def test_answer():
    assert find_differences('./tests/fixtures/advanced_before.json', './tests/fixtures/advanced_after.json', format='json') == json.load(open('./tests/fixtures/advanced_file_result_json.json'))
