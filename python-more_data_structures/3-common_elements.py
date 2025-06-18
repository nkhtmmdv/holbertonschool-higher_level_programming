#!/usr/bin/python3
def common_elements(set_1, set_2):
    unq_elem = []
    for elem in set_1:
        if elem in set_2 and elem not in unq_elem:
            unq_elem.append(elem)
    return unq_elem
