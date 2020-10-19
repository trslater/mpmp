"""MPMP 16: Closed Form Solution CLI

A simple CLI for calculating the percentage of odd numbers in Pascal's Triangle
given the number of rows.

Note: only accurate for numbers of rows that are powers of 2.
"""


import sys

from . import lib


def main(argv):
    m = int(argv[0])

    print(f"{100*lib.percent_odd(m)}%")


if __name__ == "__main__":
    main(sys.argv[1:])
