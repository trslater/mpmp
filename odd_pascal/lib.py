"""MPMP 16 Lib
"""


import math

from itertools import islice, starmap, product, tee


def percent_odd(m):
    return 2*3**(math.log(m, 2))/m/(m + 1)


def print_sierpinski(pt, m):
    for row in (islice(pt, m) for _ in range(m)):
        for num in row:
            if is_odd(num):
                print("* ", end="")

            else:
                print("  ", end="")

        print()


def pt(m):
    return starmap(math.comb, product(*tee(range(m))))


def paired(iterable):
    """Returns an iterator of every consecutive pair from an iterable"""

    # Get two copies of permutation as iterators
    p1, p2 = tee(iterable)
    # Advance second permutation iterator by one
    next(p2)

    return zip(p1, p2)


def is_odd(num):
    return num % 2 == 1


# print(f"{100*percent_odd(128)}%")

    # d = 16

    # print(3**math.log(d, 2))
    # print(3**math.log(1, 2))
    # print(3**math.log(2, 2))
    # print(3**math.log(3, 2))
    # print(3**math.log(4, 2))
    # print(3**math.log(5, 2))
    # print(3**math.log(6, 2))
    # print(3**math.log(7, 2))
    # print(3**math.log(8, 2))
    # print(f"{100*2*3**math.log(d, 2)/d/(d + 1)}%")

    # print(count_occurances(3003))
    # for row in pt_skew(20, 8):
    #     for num in row:
    #         if is_odd(num):
    #             print(f" {num:>6}*", end="")

    #         else:
    #             print(f" {num:>6} ", end="")


    #     print()

    # for row in pt(d):
    #     for num in row:
    #         if is_odd(num):
    #             print("* ", end="")

    #         else:
    #             print("  ", end="")

    #     for num in row:
    #         print(f" {num:>5} ", end="")

    #     print()
