"""MPMP16: Naive Solution CLI

Simply counts number of odds in Pascal's Triangle and divdes by calculated
total.
"""


import sys
import itertools

from . import lib


def main(argv):
    num_rows = int(argv[0])

    # Length of a list of...
    num_odd = len(list(filter(lib.is_odd, lib.pt(num_rows))))

    # Use closed form for sum of first n positive integers
    num_total = num_rows*(num_rows + 1)/2

    print(f"{100*num_odd/num_total}%")


if __name__ == "__main__":
    main(sys.argv[1:])
