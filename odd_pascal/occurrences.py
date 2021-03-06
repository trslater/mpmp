"""Count the Number of Occurrences of a Number CLI

A simple CLI that counts the number of occurrences of a number in Pascal's
Triangle.
"""

import sys

from itertools import chain
from collections import Counter

from . import lib


def main(argv):
    num = int(argv[0])

    print(Counter(lib.pt(num+1))[num])


if __name__ == "__main__":
    main(sys.argv[1:])