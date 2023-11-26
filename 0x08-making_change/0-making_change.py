#!/usr/bin/python3

"""
Module for Making Change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a
    given amount total
    """
    # Check if the total is 0 or less
    if total <= 0:
        return 0

    # Handle base case: If there are no coins, or total is not possible with given coins
    if not coins or min(coins) > total:
        return -1

    # Initialize a table to store results
    dp_table = [float('inf')] * (total + 1)
    dp_table[0] = 0  # Base case: 0 coins needed for total of 0

    # Iterate through coins and amounts, updating the table
    for coin in coins:
        for amount in range(coin, total + 1):
            dp_table[amount] = min(dp_table[amount], dp_table[amount - coin] + 1)

    # Return the result for the original total
    return dp_table[total] if dp_table[total] != float('inf') else -1
