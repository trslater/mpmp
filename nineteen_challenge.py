import sys

from itertools import count, accumulate, islice


def main(argv):
    n = int(argv[0])

    print(tuple(islice((
        (i, s) for i,s in enumerate(accumulate(
            p**2 for p in prime_sieve()), start=1)
        if s%i == 0), n)))


def prime_sieve():
    """Sieve of Eratosthenes as a generator"""

    primes_so_far = []

    for i in count(2):
        # If x is not divisible by any prime found so far
        if not any(i % p == 0 for p in primes_so_far):
            primes_so_far.append(i)
            yield i


if __name__ == "__main__":
    main(sys.argv[1:])
