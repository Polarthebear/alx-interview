#!/usr/bin/python3
"""makeChange Module"""


def makeChange(coins, total):
    """Algorithm to find the least number of coins we need to meet a
    given amount total when given a pile of coins of different values."""
    if total <= 0:
        return 0
    remainder = total
    count_coins = 0
    coin_index = 0
    coin_sort = sorted(coins, reverse=True)
    n = len(coins)
    while remainder > 0:
        if coin_index >= n:
            return -1
        if remainder - coin_sort[coin_index] >= 0:
            remainder -= coin_sort[coin_index]
            count_coins += 1
        else:
            coin_index += 1
    return count_coins
