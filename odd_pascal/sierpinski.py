"""Print Koch Snowflake CLI

Generates the Koch Snowflake based on Pascal's Triangle's odds.
"""


import sys

from . import lib


def main(argv):
    num_rows = int(argv[0])

    lib.print_koch(lib.pt(num_rows))


if __name__ == "__main__":
    main(sys.argv[1:])
