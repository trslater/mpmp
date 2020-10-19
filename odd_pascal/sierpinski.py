"""Print Sierpinski's Triangle CLI

Generates the Sierpinski's Triangle based on Pascal's Triangle's odds.
"""


import sys

from . import lib


def main(argv):
    num_rows = int(argv[0])

    lib.print_sierpinski(lib.pt(num_rows))


if __name__ == "__main__":
    main(sys.argv[1:])
