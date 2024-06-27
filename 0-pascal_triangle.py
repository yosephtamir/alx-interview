#!/usr/bin/python3
'''A script to draw pascal triangle'''


def pascal_triangle(n):
    '''
    used to draw pascal triangle based on given parameter(n)
    Returns:
      List of lists of integers representing the Pascal’s triangle
    '''
    lists = []
    if n == 0:
        return lists
    for i in range(n):
        lists.append([])
        lists[i].append(1)
        if (i > 0):
            for j in range(1, i):
                lists[i].append(lists[i - 1][j - 1] + lists[i - 1][j])
            lists[i].append(1)
    return lists
