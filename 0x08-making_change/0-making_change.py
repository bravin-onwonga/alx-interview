#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number
of coins needed to meet a given amount total.

Prototype: def makeChange(coins, total)
Assume:
    the value of a coin will always be an integer greater than 0
    you have an infinite number of each denomination of coin in the list
"""


def makeChange(coins, total):
    """ Calculates number of minimum number coins
    Params:
        coins - list of the values of the coins in your possession
        total - amount
    Return:
        - fewest number of coins needed to meet total
        - if total is 0 or less, return 0
        - if total cannot be met by any number of coins you have, return -1
    """
    coins.sort(reverse=True)
    number_coins = 0

    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1

    i = 0

    while (i < len(coins)):
        coin = coins[i]
        if (total == 0):
            return number_coins
        if (total < coin and i == (len(coins) - 1)):
            return -1
        div = total // coin
        if div > 0:
            number_coins += div
            total = total - (coin * div)
        i += 1
    if (total == 0):
        return number_coins
    return -1
