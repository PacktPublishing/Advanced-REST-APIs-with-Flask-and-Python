import os
import json

STRINGS_FOLDER = "strings"
SOURCE_TRANSLATION = "en-gb.json"
source_strings = {}


with open(f"strings/{source}") as f:
    source_strings = json.load(f)


def check_contains_all_strings(source, source_name, compared, compared_name):
    for key in source.keys():
        if key not in compared.keys():
            print(f"{key} was present in {source_name} but not in {compared_name}.")


for filename in os.listdir(STRINGS_FOLDER):
    if SOURCE_TRANSLATION in filename:
        continue
    
    with open(f"{STRINGS_FOLDER}/{filename}") as file:
        strings = json.load(file)
        check_contains_all_strings(
            source_strings,
            SOURCE_TRANSLATION,
            strings,
            filename
        )
