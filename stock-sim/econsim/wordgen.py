import random
import string

def generate_word(length):
    """ Generates a stock name. """
    return reduce(
        lambda x, y: x + y,
        map(
            lambda x: random.choice(string.ascii_uppercase),
            xrange(length),
        ),
    )

    
