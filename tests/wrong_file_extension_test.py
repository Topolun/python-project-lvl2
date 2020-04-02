from gendiff.engine import generate_diff
from gendiff.formatters import default

def test_wrong_file_format():
    assert generate_diff(
        './tests/fixtures/advanced_before.txt',
        './tests/fixtures/advanced_after.txt',
        default
        ) == 'File extension is not JSON or YML'