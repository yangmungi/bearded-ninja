#!/bin/python

def min_squares(width, height):
    """Determine the minimum number of squares used in a rectangle."""
    print "%s x %s" % (width, height)
    mod_r = height
    low = width

    count = 0
    areas = 0

    while mod_r != 0:
        iterable = [low, mod_r]
        low = min(iterable)
        hig = max(iterable)

        oc = count
        oa = areas

        count += hig / low
        mod_r = hig % low

        diff = count - oc
        areas += low * low * diff

        print "%s [%s] total, %s X (%s x %s [%s]), %s x %s left" % (count, areas, diff, low, low, (areas - oa), low, hig)

if __name__ == "__main__":
    min_squares(112, 3)
