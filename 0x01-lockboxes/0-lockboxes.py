#!/usr/bin/python3
"""Lockboxes puzzles"""


def canUnlockAll(boxes):
    """Checks if all boxes can be unclocked"""
    if not boxes:
        return False

    if len(boxes) == 1:
        return True

    len_boxes = len(boxes)

    opened = [False] * len_boxes
    opened[0] = True

    keys = boxes[0]

    while keys:
        if all(opened):
            return True
        new_keys = []
        for key in keys:
            if key >= 0 and key < len_boxes and opened[key] is False:
                opened[key] = True
                new_keys.extend(boxes[key])
        keys = [i for i in set(new_keys)]

    return all(opened)
