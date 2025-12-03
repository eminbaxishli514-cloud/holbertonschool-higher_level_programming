#!/usr/bin/python3
"""
Basic Serialization Module.

This module provides functions to serialize a Python dictionary
to a JSON file and deserialize a JSON file back to a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The name of the output JSON file.
                        If the file exists, it will be replaced.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it to a Python dictionary.

    Args:
        filename (str): The name of the input JSON file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
