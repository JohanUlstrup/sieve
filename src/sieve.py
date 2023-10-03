"""Computing primes."""


def sieve(n: int) -> list[int]:
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 0
    candidates = list(range(2, n + 1))
    primes = []

    # FIXME: fill out this bit
    while candidates:
        current_prime = candidates[0]
        primes.append(current_prime)

        # Remove all multiples of the current prime from candidates
        candidates = [x for x in candidates if x % current_prime != 0]
        

    return primes

#In this modified code, we use a for loop to iterate through the candidates list, and we don't check explicitly for the termination condition because we rely on the list length. The loop will continue until there are no more candidates left in the list. The rest of the algorithm remains the same.



# Example usage:
n = 15
result = sieve(n)
print(result)





