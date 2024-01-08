#!/usr/bin/python3

"""
0x01. Lockboxes
Algorithm, Python
"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.
    """
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    keys = set([0])  # Set to store keys that can unlock boxes
    opened_boxes = set([0])  # Set to store boxes that have been opened

    while keys:
        current_key = keys.pop()
        current_box = boxes[current_key]

        for key in current_box:
            if key < n and key not in opened_boxes:
                keys.add(key)
                opened_boxes.add(key)

    return len(opened_boxes) == n
