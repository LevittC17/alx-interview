#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given
    amount total.
    """

    if total <= 0:
        return 0

    if not coins or None in coins:
        return -1

    # Sort coins in descending order
    coins.sort(reverse=True)

    # Initialize a list to store the minimum number of coins
    # for each value
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update the min_coins list for each value from coin to total
        for value in range(coin, total + 1):
            if coin > value:
                # No need to continue if the coin is greater than the value
                break
            min_coins[value] = min(min_coins[value],
                                   min_coins[value - coin] + 1)

    # If the value at total is still infinity, it means the total cannot be met
    if min_coins[total] == float('inf'):
        return -1

    return min_coins[total]
