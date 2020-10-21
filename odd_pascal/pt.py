"""Pascal's Triangle Printer CLI

Simply generates and prints Pascal's Triangle.
"""


import sys

from itertools import islice, chain, tee

from . import lib


def main(argv):
    m = int(argv[0])

    # Make 2 identical triangles
    pt1, pt2 = tee(lib.pt(m))

    # Use first to calc min with in digits required
    width = len(str(max(pt1)))

    for row in (islice(pt2, m) for _ in range(m)):
        for num in row:
            # Print each number width+1 wide, aligned right
            print(f"{num:>{width+1}}", end="")

        print()


if __name__ == "__main__":
    main(sys.argv[1:])
