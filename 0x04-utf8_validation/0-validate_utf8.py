#!/usr/bin/python3
"""
Method determins if a given data set represents UTF8 encoding
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Function returns true if data is valid UTF8 encoding otherwise false.
    """
    bytes_n = 0
    for byte in data:
        mask = 1 << 7
        if bytes_n == 0:
            while byte & mask:
                bytes_n += 1
                mask >>= 1
            if bytes_n == 0:
                continue
            if bytes_n == 1 or bytes_n > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        bytes_n -= 1
    return bytes_n == 0
