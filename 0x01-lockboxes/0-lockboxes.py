#!/usr/bin/python3
'''
Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
'''


def canUnlockAll(boxes):
    ''''
    Used to anlock all the boxes:
    * boxes -> a list of lists
    Returns True if all boxes can be opened, else returns False
    '''
    length = len(boxes)
    keys = [0]

    for key in keys:
        for newKey in boxes[key]:
            if newKey not in keys and newKey < length:
                keys.append(newKey)
    if len(keys) == length:
        return True
    return False



boxes = [[1], [2], [3], [4],[]]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))