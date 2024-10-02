#!/bin/python
"""
https://en.wikipedia.org/wiki/Integer_partition
"""

import sys


def departition(base, parent=None):
    num = base

    part = []
    while num > 0:
        sub_part = [num]

        sub_part_sum = sum(sub_part)
        diff = base - sub_part_sum

        if parent is None or num <= parent:
            if sub_part_sum < base:
                de_part = departition(diff, num)
                for de_sub_part in de_part:
                    sub_part = sub_part + de_sub_part
                    part.append(sub_part)
                    sub_part = [num]
            else:
                part.append(sub_part)
        num -= 1
    return part


if __name__ == "__main__":
    if len(sys.argv) == 2:
        base = int(sys.argv[1])
    else:
        base = 7

    sizes = []

    for i in range(base):
        departitions = departition(i)
        sizes.append(len(departitions))
        for depart in departitions:
            print(depart)
        print()
    print(sizes)
