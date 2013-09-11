#!/bin/python

import sys
import math

if len(sys.argv) <= 1:
    print "Need vector size."
    quit()

vec = range(int(sys.argv[1]))

def swap(vec, index_fr, index_to):
    temp = vec[index_to]
    vec[index_to] = vec[index_fr]
    vec[index_fr] = temp

def solve(entire, len_entire, solved_index, counter):
    if len_entire == solved_index + 1:
        print entire
        return counter + 1

    next_index = solved_index + 1

    counter = solve(entire, len_entire, next_index, counter)

    for i in xrange(next_index, len_entire):
        swap(entire, solved_index, i)
        counter = solve(entire, len_entire, next_index, counter)
        #swap(entire, solved_index, i)

    return counter

print solve(vec, len(vec), 0, 0)
print math.factorial(int(sys.argv[1]))
