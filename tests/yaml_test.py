from gendiff.parsers import recieve_yaml
from gendiff.generate_diff import find_differences

def test_answer():
    assert recieve_yaml('./tests/fixtures/before.yml', './tests/fixtures/after.yml') == '{\n  host: hexlet.io\n+ timeout: 20\n- timeout: 50\n- proxy: 123.234.53.22\n+ verbose: True\n}'
    assert find_differences('./tests/fixtures/before.yml', './tests/fixtures/after.yml') == '{\n  host: hexlet.io\n+ timeout: 20\n- timeout: 50\n- proxy: 123.234.53.22\n+ verbose: True\n}'
