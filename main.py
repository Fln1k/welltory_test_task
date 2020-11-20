import os
import sys
import json
import jsonschema
import logging


def read(path):
    with open(path) as file:
        return json.load(file)


def log(message):
    with open(log_file, 'a') as file:
        file.write(f"{message}")


json_path = sys.argv[1]
schema_path = sys.argv[2]
log_file = sys.argv[3]
for json_file in os.listdir(json_path):
    log(f"<ul>json file: {json_file}")
    for schema_file in os.listdir(schema_path):
        log(f"<ul>schema file: {schema_file}")
        errors = jsonschema.Draft7Validator(read(f"{schema_path}/{schema_file}")).iter_errors(
            read(f"{json_path}/{json_file}"))
        if list(errors):
            for error in sorted(errors, key=lambda e: e.path):
                log(f"<ul>{str(error.message)}</ul>")
        log("</ul>")
    log("</ul>")
