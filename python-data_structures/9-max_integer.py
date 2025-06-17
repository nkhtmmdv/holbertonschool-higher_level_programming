#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    max_int = my_list[0]
    for elem in my_list:
        if elem > max_int:
            max_int = elem
    return max_int
