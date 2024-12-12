#!/usr/bin/python3
"""Mock interview prime game module"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds"""
    def sieve_of_eratosthenes(max_n):
        """Create a sieve to determine primes up to max_n."""
        sieve = [True] * (max_n + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime
        for i in range(2, int(max_n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, max_n + 1, i):
                    sieve[j] = False
        return sieve

    def count_primes_up_to(n, sieve):
        """Count the number of primes up to n using the sieve."""
        return sum(sieve[:n + 1])

    # Determine the largest n for precomputing primes
    max_n = max(nums)
    sieve = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count the number of primes up to n
        num_primes = count_primes_up_to(n, sieve)

        # Maria wins if the number of primes is odd; Ben wins if even
        if num_primes % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
