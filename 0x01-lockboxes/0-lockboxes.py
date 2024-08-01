#!/usr/bin/env python3
"""Lockboxes puzzles"""


def canUnlockAll(boxes):
    """Checks if all boxes can be unclocked"""
    opened = [0]

    res = open_boxes(boxes, boxes[0], opened)

    return res


def open_boxes(boxes, keys, opened):
    """Opens boxes"""
    if len(opened) == len(boxes):
        return True

    if len(keys) == 0:
        return False

    for key in keys:
        if key not in opened and key < len(boxes):
            opened.append(key)
            return open_boxes(boxes, boxes[key], opened)
    return True
