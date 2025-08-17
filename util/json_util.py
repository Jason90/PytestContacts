import os
import json
from jsonschema import validate, ValidationError
from util import file_util

# Utility functions for JSON schema validation
def load_schema(file_name):
    try:
        file_path=os.path.join( "data", "schema", file_name)
        content=file_util.read(file_path)
        
        return json.loads(content)
    except FileNotFoundError:
        raise FileNotFoundError(f"Schema file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"The schema file format is incorrect: {file_path}")

# Validate JSON data against a schema
def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        raise AssertionError(f"JSON validation error: {e.message}")
    return True