from gendiff.generate_diff import find_differences

def test_answer():
    with open('./tests/fixtures/flat_file_result.txt') as correct_answer:
        assert find_differences(
            './tests/fixtures/before.json',
            './tests/fixtures/after.json'
            ) == correct_answer.read()