import json
from jsonschema import validate, ValidationError

# Utility functions for JSON schema validation
def load_schema(schema_path):
    try:
        with open(schema_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Schema file not found: {schema_path}")
    except json.JSONDecodeError:
        raise ValueError(f"The schema file format is incorrect: {schema_path}")

# Validate JSON data against a schema
def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        raise AssertionError(f"JSON validation error: {e.message}")
    return True