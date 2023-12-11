#!/usr/bin/python3

"""
Primer Game
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Args:
    - x (int): Number of rounds.
    - nums (list): List of integers representing the end range for each round.

    Returns:
    - str or None: Name of the player that won the most rounds.
                   Returns None if the winner cannot be determined.

    Example:
    >>> find_winner(3, [4, 5, 1])
    'Ben'
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)

    is_prime = [True for _ in range(max(max_num + 1, 2))]

    # Sieve of Eratosthenes to find prime numbers
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            is_prime[j] = False

    is_prime[0] = is_prime[1] = False

    prime_count = 0
    for i in range(len(is_prime)):
        if is_prime[i]:
            prime_count += 1
        is_prime[i] = prime_count

    # Count the number of rounds player 1 wins
    player1_wins = sum(is_prime[x] % 2 == 1 for x in nums)

    # Determine the winner based on the number of rounds won
    if player1_wins * 2 == len(nums):
        return None
    elif player1_wins * 2 > len(nums):
        return "Maria"
    else:
        return "Ben"
