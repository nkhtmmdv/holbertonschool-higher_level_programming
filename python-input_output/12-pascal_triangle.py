#!/usr/bin/python3
''' 12 '''


def pascal_triangle(n):
    ''' 12 '''
    if n <= 0:
        return []
    pas = [[1]]
    for i in range(1, n):
        prev = pas[-1]
        new = [1]
        for j in range(1, i):
            new.append(prev[j - 1] + prev[j])
        new.append(1)
        pas.append(new)
    return pas
