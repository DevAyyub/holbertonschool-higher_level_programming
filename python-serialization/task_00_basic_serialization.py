#!/usr/bin/python3
""" Module for basic serialization """
import json


def serialize_and_save_to_file(data, filename):
    """ Serializes a dictionary and saves it to a JSON file """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize_from_file(filename):
    """ Loads a JSON file and deserializes it to a dictionary """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
