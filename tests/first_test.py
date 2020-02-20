from gendiff import recieve_json

def test_answer():
    assert recieve_json('before.json', 'after.json') == '{\n  host: hexlet.io\n+ timeout: 20\n- timeout: 50\n- proxy: 123.234.53.22\n+ verbose: True\n}'
