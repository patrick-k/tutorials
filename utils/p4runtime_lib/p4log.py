import json

"""
N01422638 - CIS6930 Advanced Networking

p4log helper functions.  Consider integrating these with existing P4InfoHelper class?
"""

def byteify(input=None):
    if isinstance(input, dict):
        return { byteify(key): byteify(value) for key, value in input.iteritems() }
    elif isinstance(input, list):
        return [ byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def program_p4log(bmv2_json_file_path=None):
    if bmv2_json_file_path is None:
        print('[p4log] - Init error, no P4 config JSON found\n')
        return

    print('[p4log] - Reading config from %s\n', bmv2_json_file_path)
    p4log_map = {}
    with open(bmv2_json_file_path, 'r') as conf_file:
        data = byteify(json.load(conf_file))
        for header in data['header_types']:
            print('[p4log] - Parsing header %s\n', header['name'])
            p4log_map[header['name']] = header['fields']

    print('[p4log] - Log schemas initialized successfully\n')
    return p4log_map
