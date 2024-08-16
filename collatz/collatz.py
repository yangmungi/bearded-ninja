import pprint
"""
93 -> 280 -> 140 -> 70
40 -> 20
Maybe numbers ending in 0 are special?

91 -> 274 -> 137 -> 412 -> 206 -> 103 -> 310 -> 155
74 -> 37 -> 112 -> 56
12 -> 6
"""
ones_index = {}

for i in xrange(0, 99):
    i_tens = i / 10
    i_ones = i % 10


    i_tens_description = 'odd' if i_tens % 2 == 1 else 'even'

    if i % 2 == 1:
        description = 'odd'
        result = i * 3 + 1
    else:
        description = 'even'
        result = i / 2

    tens = (result % 100) / 10
    ones = result % 10

    if not i_ones in ones_index:
        ones_index[i_ones] = {}


    ones_index[i_ones][i_tens] = result

    result_tens_description = 'odd' if tens % 2 == 1 else 'even'
    result_description = 'odd' if ones % 2 == 1 else 'even'

    print "%d %d %s %s -> %d %d %s %s" % (i_tens, i_ones, i_tens_description, description, tens, ones, result_tens_description, result_description)

pprint.pprint(ones_index)

