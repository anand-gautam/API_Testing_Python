import json
import jsonschema
from jsonschema import validate


def get_schema(source_file):
    with open (source_file, 'r') as schema_file:
        schema = json.load(schema_file)
    return schema

def validate_json_schema(source_file, json_data):
    execute_schema = get_schema(source_file)
    try:
        validate(instance=json_data, schema=execute_schema)
    except jsonschema.exceptions.ValidationError as e:
        print(e)
        e = "Invalid JSON"
        return False, e
    msg = "Valid JSON"
    return True, msg

