from gendiff.generate_diff import find_differences

def test_wrong_file_format():
    assert find_differences(
        './tests/fixtures/advanced_before.txt',
        './tests/fixtures/advanced_after.txt'
        ) == 'File extension is not JSON or YML'