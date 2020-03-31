from gendiff.generate_diff import find_differences

def test_compare_simple_json_files_default_format():
    with open('./tests/fixtures/flat_file_result.txt') as correct_answer:
        assert find_differences(
            './tests/fixtures/before.json',
            './tests/fixtures/after.json'
            ) == correct_answer.read()