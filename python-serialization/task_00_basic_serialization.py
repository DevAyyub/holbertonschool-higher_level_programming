#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize_from_file(filename):
    """Deserialize a JSON file to a Python dictionary."""
    with open(filename, 'r') as f:
        return json.load(f)
