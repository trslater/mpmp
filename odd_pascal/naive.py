"""MPMP 16: How Odd is Pascal's Triangle?

What percentage of the numbers in the first 128 rows of Pascal's triangle are
odd?

Note: "pt" used as abbreviation for "Pascal's Triangle"

[More Info](http://www.think-maths.co.uk/pascaltriangle)
"""


import sys
import itertools

from . import lib


def main(argv):
    num_rows = int(argv[0])

    # Length of a list of...
    num_odd = len(list(
        # Generator of only odd numbers...
        filter(lib.is_odd,
               # From single iterator of all numbers in Pascal's triangle
               itertools.chain.from_iterable(lib.pt(num_rows)))))

    # Use closed form for sum of first n positive integers
    num_total = num_rows*(num_rows + 1)/2

    print(f"{100*num_odd/num_total}%")


if __name__ == "__main__":
    main(sys.argv[1:])
