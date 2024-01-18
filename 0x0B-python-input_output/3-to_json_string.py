#!/usr/bin/python3
"""Defines a function that returns a JSON"""
import json


def to_json_string(my_obj):
    """Returns a JSON"""
    return json.dumps(my_obj)
