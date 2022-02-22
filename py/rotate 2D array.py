import copy
import math
from classes.utils import isTrue, print2DArray

# 1  x  3  4
# 5  6  7  x
# x 10 11 12
# 13 14 x 16

def rotate(array, n):
    if n == 1:
        return array

    def cells(offset, n):
        size = n - offset*2
        end = offset + size - 1 
        
        for index in range(offset, end):
            i = index - offset
            
            yield offset, offset+i
            yield offset+i, end
            yield end, end-i
            yield end-i, offset
        
    for offset in range(int(n/2)):
        
        itr = cells(offset, n)
        x = next(itr, None)
        while(x):
            (r1, c1) = x
            (r2, c2) = next(itr)
            (r3, c3) = next(itr)
            (r4, c4) = next(itr)
            
            x = next(itr, None)

            last = array[r4][c4]                

            array[r4][c4] = array[r3][c3]
            array[r3][c3] = array[r2][c2]
            array[r2][c2] = array[r1][c1]
            array[r1][c1] = last 

    return array

def neardy_rotate(given_array, n):
    def rotate_sub(i, j, n):
        return j, n - 1 - i

    for i in range(math.ceil(n/2)):
        for j in range(math.floor(n/2)):
            tmp = [-1] * 4
            (current_i, current_j) = (i, j)
            for k in range(4):
                tmp[k] = given_array[current_i][current_j]
                (current_i, current_j) = rotate_sub(current_i, current_j, n)
            for k in range(4):
                given_array[current_i][current_j] = tmp[(k - 1) % 4]
                (current_i, current_j) = rotate_sub(current_i, current_j, n)
    return given_array

def inefective_rotate(array, n):

    def points(offset, n):
        for c in range(offset, (n-1) - offset):
            yield (offset, c)
        for r in range(offset, (n-1) - offset):
            yield (r, (n-1) - offset)
        for c in range((n-1) - offset, offset, -1):
            yield ((n-1) - offset, c)
        for r in range((n-1) - offset, offset, -1):
            yield (r, offset)

    for offset in range(int(n/2)):
        for i in range((n -1) - (offset*2)):
            p = None
            for (r, c) in points(offset, n):
                if (p == None):
                    p = array[r][c]
                array[r][c], p = p, array[r][c]

            if (p != None):
                array[offset][offset] = p      
            
    return array

def deepcopy_rotate(given_array, n):
    rotated = copy.deepcopy(given_array)
    for r in range(n):
        for c in range(n):
           rotated[r][c] = given_array[n-(c+1)][r]

    return rotated

def test(fn, given_array, n, expected):    
    def execute():
        field = fn(given_array, n)
        #print2DArray(field)
        for r in range(n):
            for c in range(n):
                if (field[r][c] != expected[r][c]):
                    return False
        return True


    isTrue(lambda: execute())

def generate_field(n):
    array = [0]
    def next():
        array[0] += 1
        return array[0]

    return [[next() for c in range(n)] for r in range(n)]

def generate_rotated_field(n):
    field = generate_field(n)
    return deepcopy_rotate(field, n)


# # NOTE: The following input values will be used for testing your solution.
# test(rotate, [[1, 2],
#              [3, 4]
#             ], 2, [
#              [3, 1],
#              [4, 2]
#             ])

# test(rotate, [
#      [1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]
#      ], 3, [
#      [7, 4, 1],
#      [8, 5, 2],
#      [9, 6, 3]
# ])

# test(rotate, [
#       [1, 2, 3, 4],
#       [5, 6, 7, 8],
#       [9, 10, 11, 12],
#       [13, 14, 15, 16]
#      ], 4, [
#       [13, 9, 5, 1],
#       [14, 10, 6, 2],
#       [15, 11, 7, 3],
#       [16, 12, 8, 4]
#  ])

# test(rotate, [
#       [1, 2, 3, 4, 5],
#       [6, 7, 8, 9, 10],
#       [11,12,13,14,15],
#       [16,17,18,19,20],
#       [21,22,23,24,25],
#      ], 5, [
#      [21, 16, 11, 6, 1],
#      [22, 17, 12, 7, 2],
#      [23, 18, 13, 8, 3],
#      [24, 19, 14, 9, 4],
#      [25, 20, 15, 10,5]
#  ])

test(rotate, generate_field(1000), 1000, generate_rotated_field(1000))
test(neardy_rotate, generate_field(1000), 1000, generate_rotated_field(1000))
test(inefective_rotate, generate_field(100), 100, generate_rotated_field(100))
test(deepcopy_rotate, generate_field(100), 100, generate_rotated_field(100))