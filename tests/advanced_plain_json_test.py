from gendiff.generate_diff import find_differences

def test_answer():
    assert find_differences('./tests/fixtures/advanced_before.json', './tests/fixtures/advanced_after.json', format='plain') == open('./tests/fixtures/advanced_file_result_plain.txt').read()
