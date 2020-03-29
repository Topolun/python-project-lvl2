from gendiff.generate_diff import find_differences

def test_answer():
    with open('./tests/fixtures/advanced_file_result.txt') as correct_answer:
        assert find_differences(
            './tests/fixtures/advanced_before.yml',
            './tests/fixtures/advanced_after.yml'
            ) == correct_answer.read()
