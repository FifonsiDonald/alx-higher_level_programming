#!/usr/bin/python3
"""Defines a function thats Save Object to a file"""



def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, 
    using a JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
