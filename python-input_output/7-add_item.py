#!/usr/bin/python3
"""
Adds all command-line arguments to a Python list and saves them to add_item.json.
Uses load_from_json_file and save_to_json_file.
"""

import sys
from pathlib import Path

load_module = __import__('6-load_from_json_file')
load_from_json_file = load_module.load_from_json_file

save_module = __import__('5-save_to_json_file')
save_to_json_file = save_module.save_to_json_file

file_name = "add_item.json"

# Load existing list or start with empty
if Path(file_name).exists():
    items = load_from_json_file(file_name)
else:
    items = []

# Append all command-line arguments
items.extend(sys.argv[1:])

# Save back to JSON file
save_to_json_file(items, file_name)
