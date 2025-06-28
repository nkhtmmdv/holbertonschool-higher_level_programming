#!/usr/bin/python3
''' 2 '''


def append_write(filename="", text=""):
    ''' 2 '''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
