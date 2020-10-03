import sys

from itertools import permutations, tee


def main():
    try:
        size = int(sys.argv[1])

    except IndexError:
        print("Usage:\n\tpython prime_pairs.py <size>")
        raise SystemExit

    # Get the numbers 1 to size
    numbers = range(1, size+1)

    # Create a tuple of primes less than or equal to size + size-1
    primes = tuple(prime_sieve(size + (size-1)))

    solutions = (
        permutation
        for permutation in permutations(numbers)
        if all((a+b) in primes for a, b in paired(permutation)))

    count = 0
    try:
        while True:
            print(next(solutions))
            count += 1

    except StopIteration:
        print(f"For a problem of size {size}, there were {count} solutions.")


def prime_sieve(max):
    """Sieve of Eratosthenes as a generator"""

    primes_so_far = []

    for i in range(2, max+1):
        # If x is not divisible by any prime found so far
        if not any(i % p == 0 for p in primes_so_far):
            primes_so_far.append(i)
            yield i


def paired(iterable):
    """Returns an iterator of every consecutive pair from an iterable"""

    # Get two copies of permutation as iterators
    p1, p2 = tee(iterable)
    # Advance second permutation iterator by one
    next(p2)

    return zip(p1, p2)


if __name__ == "__main__":
    main()
