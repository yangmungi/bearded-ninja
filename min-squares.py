#!/bin/python
import sys
import logging

def min_squares(width, height):
    """Determine the minimum number of squares used in a rectangle."""
    if width <= 0 or height <= 0:
        return 0

    logging.debug("%s x %s" % (width, height))
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

        logging.info("%s [%s] total, %s X (%s x %s [%s]), %s x %s left" % (count, areas, diff, low, low, (areas - oa), low, hig))
    return count

if __name__ == "__main__":
    w = 3
    len_argv = len(sys.argv)
    if len_argv >= 2:
        w = int(sys.argv[1])
    
    h = 7 
    if len_argv >= 3:
        h = int(sys.argv[2])
        
    # The big test is to do this in constant time?
    for i in xrange(w): 
        min_c = min_squares(i, h)
        print "%s x %s" % (i, h), min_c
