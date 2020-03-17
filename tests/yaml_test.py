from gendiff.generate_diff import find_differences

def test_answer():
    assert find_differences('./tests/fixtures/before.yml', './tests/fixtures/after.yml') == open('./tests/fixtures/flat_file_result.txt').read()
