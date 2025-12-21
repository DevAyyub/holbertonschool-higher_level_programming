#!/usr/bin/python3
""" Module to convert CSV data to JSON format """
import csv
import json


def convert_csv_to_json(csv_filename):
    """ Converts a CSV file to a JSON file named data.json """
    try:
        # Open and read the CSV file
        with open(csv_filename, 'r', encoding='utf-8') as csv_f:
            # Use DictReader to automatically map headers to keys
            csv_reader = csv.DictReader(csv_f)
            data = [row for row in csv_reader]

        # Write the resulting list of dictionaries to data.json
        with open('data.json', 'w', encoding='utf-8') as json_f:
            json.dump(data, json_f, indent=4)
        
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
