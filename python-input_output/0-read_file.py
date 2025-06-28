#!/usr/bin/python3
''' 0 '''


def read_file(filename=""):
    ''' 0 '''
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
