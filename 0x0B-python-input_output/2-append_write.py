#!/usr/bin/python3
"""Writes a file-appending function."""



def append_write(filename="", text=""):
    """If the file doesn’t exist, it creates it"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
