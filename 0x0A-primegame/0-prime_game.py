#!/usr/bin/python3

"""
Primer Game
"""

def isWinner(x, nums):
    """
    Determines the winner of each round of the prime game.

    Args:
    - x (int): Number of rounds.
    - nums (list): Array of integers representing the end range for each round.

    Returns:
    - str or None: Name of the player that won the most rounds.
                   Returns None if the winner cannot be determined.

    Constraints:
    - x and n will not be larger than 10000.
    - Cannot import any packages.

    Example:
    >>> isWinner(3, [4, 5, 1])
    'Ben'
    """
    def is_prime(num):
        """
        Checks if a number is prime.

        Args:
        - num (int): The number to check.

        Returns:
        - bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        """
        Generates a list of prime numbers up to n.

        Args:
        - n (int): The end range.

        Returns:
        - list: List of prime numbers.
        """
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def remove_multiples(remaining, prime):
        """
        Removes multiples of a prime number from the remaining numbers.

        Args:
        - remaining (list): List of remaining numbers.
        - prime (int): Prime number to remove multiples of.

        Returns:
        - list: Updated list of remaining numbers.
        """
        return [num for num in remaining if num % prime != 0]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = get_primes(n)
        remaining = list(range(1, n + 1))

        maria_turn = True
        while primes:
            prime = primes.pop(0)
            if maria_turn:
                ben_wins += 1
            else:
                maria_wins += 1
            remaining = remove_multiples(remaining, prime)
            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
