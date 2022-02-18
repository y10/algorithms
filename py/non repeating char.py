# Implement your function below.
from collections import defaultdict
from classes.utils import testit

def non_repeating(given_string):

    uniqueChars = defaultdict(lambda:0)

    for c in given_string:
        uniqueChars[c] += 1

    for c in uniqueChars:
        if uniqueChars[c] == 1:
            return c
        
    return None

# NOTE: The following input values will be used for testing your solution.
testit(lambda: non_repeating("abcab"), "c") # should return 'c'
testit(lambda: non_repeating("abab"), None) # should return None
testit(lambda: non_repeating("aabbbc"), 'c') # should return 'c'
testit(lambda: non_repeating("aabbdbc"), 'd') # should return 'd'