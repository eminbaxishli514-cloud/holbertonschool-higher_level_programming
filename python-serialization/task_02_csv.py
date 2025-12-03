#!/usr/bin/python3
"""
Module to convert CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON and save it to data.json.

    Args:
        csv_filename (str): The input CSV filename.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        data_list = []

        with open(csv_filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append(dict(row))

        with open("data.json", 'w', encoding='utf-8') as jsonfile:
            json.dump(data_list, jsonfile, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
