#!/usr/bin/python3
"""Lockboxes puzzles"""


def canUnlockAll(boxes):
    """Checks if all boxes can be unclocked"""
    if not boxes:
        return False

    if len(boxes) == 1:
        return True

    opened = [0]

    res = open_boxes(boxes, boxes[0], opened)

    return res


def open_boxes(boxes, keys, opened):
    """Opens boxes"""
    if len(opened) == len(boxes):
        return True

    for key in keys:
        if key not in opened and key < len(boxes):
            opened.append(key)
            return open_boxes(boxes, boxes[key], opened)

    idx = boxes.index(keys)
    key_index = opened.index(idx) - 1
    if key_index < 0:
        return False
    if key_index == 0:
        keys_found = 0
        for key in keys:
            if key not in opened:
                keys_found += 1
        if keys_found == 0:
            return False
    return open_boxes(boxes, boxes[opened[key_index]], opened)
