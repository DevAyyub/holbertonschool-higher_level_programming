#!/usr/bin/python3
""" Module for serializing and deserializing with XML """
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """ Serializes a dictionary to an XML file """
    # Create the root element
    root = ET.Element("data")
    
    # Iterate through dictionary and create child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    # Create the tree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """ Deserializes an XML file into a Python dictionary """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct the dictionary from XML tags and text
        return {child.tag: child.text for child in root}
    except FileNotFoundError:
        return None
    except Exception:
        return None
