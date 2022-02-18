from timeit import Timer

def mesureit(fn, number=1):
    t = Timer(fn)
    print(t.timeit(number))

def testit(fn, expected):
    suuccess = False

    def test():
        result = fn()
        suuccess = result == expected
        print('SUCCEEDED' if (suuccess) else 'FAILED')
        print(result)
    
    t = Timer(test)
    print(t.timeit(number=1))

    return suuccess

def isTrue(fn):
    suuccess = False

    def test():
        result = fn()
        suuccess = result
        print('SUCCEEDED' if (suuccess) else 'FAILED')
    
    t = Timer(test)
    print(t.timeit(number=1))

    return suuccess    

def isFalse(fn):
    suuccess = False

    def test():
        result = fn()
        suuccess = not result
        print('SUCCEEDED' if (suuccess) else 'FAILED')
    
    t = Timer(test)
    print(t.timeit(number=1))

    return suuccess    


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def print2DArray(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return print('[' + ',\n '.join(list_rows) + ']')