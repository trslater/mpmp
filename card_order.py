import itertools
import math


def main():
    # for i in range(9):
    #     print(i, min(
    #         max(longest_asc(p), longest_desc(p))
    #         for p in itertools.permutations(range(i))))

    # s = []
    k = 10
    perms = itertools.permutations(range(k))

    all_perms = set()
    forward_perms = set()

    for p in perms:
        len_before = len(all_perms)
        all_perms.add(tuple(p))
        all_perms.add(tuple(reversed(p)))

        # If a unique perm up to mirror symmertry was added, i.e., 2 were added
        if len(all_perms) - len_before == 2:
            forward_perms.add(p)

    print(min(longest_asc(p) for p in forward_perms))

    # print(tuple(forward_perms))

    # half_perms = []
    # for p in perms:
        # if tuple(reversed(p)) not in half_perms:
            # half_perms.append(p)



    # for p in :
    #     print(p)
    #     d = longest_desc(p)
    #     print(p, (a, d), a + d)


    # print(min(
    #     max(longest_asc(p), longest_desc(p))
    #     for p in itertools.permutations(range(9))))


def longest_asc(a):
    return lcs(a, tuple(i for i in range(len(a))))


def longest_desc(a):
    return lcs(a, tuple(i for i in reversed(range(len(a)))))


def lcs(a, b):
    m = len(a)
    n = len(b)

    l = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                l[i+1][j+1] = l[i][j] + 1

            else:
                l[i+1][j+1] = max(l[i][j+1], l[i+1][j])

    return l[m][n]


if __name__ == "__main__":
    main()
