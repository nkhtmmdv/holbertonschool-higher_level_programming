#!/usr/bin/python3
''' 1 '''


def write_file(filename="", text=""):
    ''' 1 '''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
