## Script to validate the law files conform to schema

import sys

# to read schema
import json
from pathlib import Path

# to validate schema 
from jsonschema import Draft202012Validator

# to read yaml
import yaml

# globals
SCHEMA_FILE = "data/schema.json"
LAWS_DIR = sys.argv[1] if len(sys.argv) > 1 else "data/laws"
validation_failed = False 

# load schema and init validator
schema_path = Path(SCHEMA_FILE)
schema = json.loads(schema_path.read_text(encoding="utf-8"))
validator = Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)

if not any(Path(LAWS_DIR).glob("*.yaml")):
    print("No .yaml files found in", LAWS_DIR)
    sys.exit(1)

# iterate the yml files and print all errors found
for path in sorted(Path(LAWS_DIR).glob("*.yaml")):
    print("Validating: ", path.name)
    law = yaml.safe_load(path.read_text(encoding="utf-8"))
    for error in validator.iter_errors(law):
        print(error.json_path, error.message)
        validation_failed = True

if validation_failed:
    print("Schema validation failed...")
    sys.exit(1)
else:
    print("All validations passed!")
    sys.exit(0)