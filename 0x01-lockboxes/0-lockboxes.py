#!/usr/bin/python3
"""Method that determines if all boxes can be opened."""


def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    """The first box is unlocked by default"""

    keys = boxes[0]
    for key in keys:
        if key < n and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])

    # Check if all boxes are unlocked
    return all(unlocked)
