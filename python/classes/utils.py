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