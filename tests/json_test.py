from gendiff.generate_diff import find_differences

def test_answer():
    assert find_differences('./tests/fixtures/before.json', './tests/fixtures/after.json') == open('./tests/fixtures/flat_file_result.txt').read()