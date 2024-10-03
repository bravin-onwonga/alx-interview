#!/usr/bin/python3
""" Finds the winner of a contest
--- More Information ---
Maria and Ben are playing a game.
Given a set of consecutive integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and removing that number
and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game,
where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.
"""


def who_won(maria_wins, ben_wins):
    """
    Finds who won
    Returns:
        Maria if maria has more wins
        Ben if Ben has more wins
        None if tied
    """
    if (maria_wins > ben_wins):
        return "Maria"
    elif (ben_wins > maria_wins):
        return "Ben"
    return None


def isWinner(x, nums):
    """
    Determines the winner of a contest
    Params:
        x - number of rounds
        nums - is an array of n
    Return:
        name of the player that won the most rounds
        None - If the winner cannot be determined
    Assume:
        n and x will not be larger than 10000
    """
    if not x or not nums:
        return None
    round = 0
    maria_wins = 0
    ben_wins = 0

    memo = {}

    while (round < x):
        if round >= len(nums):
            return who_won(maria_wins, ben_wins)
        n = nums[round]

        if n < 2:
            ben_wins += 1

        elif (memo.get(n)):
            primes = memo[n]
            if len(primes) % 2 == 0:
                ben_wins += 1
            else:
                maria_wins += 1

        else:
            max_prime = 0

            if memo:
                max_prime = max(zip(memo.keys()))[0]

            if (max_prime and n < max_prime):
                keys = sorted(memo.keys())
                for i in range(len(keys)):
                    if keys[i] < n and keys[i + 1] > n:
                        largest_saved = keys[i + 1]
                        break
                primes = [num for num in memo[largest_saved] if num <= n]
                memo[n] = primes
                if len(primes) % 2 == 0:
                    ben_wins += 1
                else:
                    maria_wins += 1
            else:
                primes = []
                my_lst = [True for i in range(n+1)]
                p = 2
                while (p * p <= n):
                    if my_lst[p]:
                        for i in range(p * p, n + 1, p):
                            my_lst[i] = False
                    p += 1
                for i in range(2, n + 1):
                    if my_lst[i]:
                        primes.append(i)
                memo[n] = primes
        round += 1
    return who_won(maria_wins, ben_wins)
