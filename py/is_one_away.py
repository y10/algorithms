# Implement your function below.
from classes.utils import isTrue, isFalse


def is_one_away(s1, s2):

    def is_one_change(s1, s2):
        for i in range(len(s1)):
            if (s1[i] != s2[i]):
                s1 = s1[:i] + s2[i] + s1[i+1:]
                break
        return s1 == s2    

    def is_one_insert_or_delete(s1, s2):
        if abs(len(s1) - len(s2)) > 1:
            return False

        if len(s1) > len(s2):            
            s1, s2 = s2, s1

        for i in range(max(len(s1), len(s2))):
            if (i < len(s1) and i < len(s2) and s1[i] != s2[i]):
                s1 = s1[:i] + s2[i] + s1[i:]
                break
            elif (i == len(s1) and i < len(s2)):
                s2 = s2[:i]
                break

        return s1 == s2 

    if len(s1) != len(s2):
        return is_one_insert_or_delete(s1, s2)

    return is_one_change(s1, s2)

# NOTE: The following input values will be used for testing your solution.

isFalse(lambda: is_one_away("abcde", "abc"))  # should return False
isFalse(lambda: is_one_away("abc", "abcde"))  # should return False


isTrue(lambda: is_one_away("abcde", "abcd"))   # should return True
isTrue(lambda: is_one_away("abde", "abcde"))  # should return True
isTrue(lambda: is_one_away("a", "a"))  # should return True
isTrue(lambda: is_one_away("abcdef", "abqdef")) # should return True
isTrue(lambda: is_one_away("abcdef", "abccef"))  # should return True
isTrue(lambda: is_one_away("abcdef", "abcde"))  # should return True

isFalse(lambda: is_one_away("aaa", "abc")) # should return False
isFalse(lambda: is_one_away("abc", "bcc"))  # should return False