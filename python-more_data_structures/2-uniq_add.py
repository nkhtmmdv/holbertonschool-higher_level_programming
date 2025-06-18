#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    unique_elements = []
    for elem in my_list:
        if elem not in unique_elements:
            unique_elements.append(elem)
            result+=elem
    return result
