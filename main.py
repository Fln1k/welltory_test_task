import os
import sys
import json
import jsonschema
import logging


def read(path):
    with open(path) as file:
        return json.load(file)


json_path = sys.argv[1]
schema_path = sys.argv[2]
logging.basicConfig(filename="README.md")

for json_file in os.listdir(json_path):
    for schema_file in os.listdir(schema_path):
        errors = jsonschema.Draft7Validator(read(f"{schema_path}/{schema_file}")).iter_errors(read(f"{json_path}/{json_file}"))
        for error in errors:
            logging.error(f"<br> json file: {json_file} <br>"
                          f"schema file: {schema_file} <br>"
                          f"error_message: {str(error.message)} <br>")