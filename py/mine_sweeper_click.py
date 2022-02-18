from classes.utils import isTrue, print2DArray


def expand(field, num_rows, num_cols, r, c):
    if (r < 0): 
        return
    if (c < 0): 
        return
    if (r >= num_rows): 
        return
    if (c >= num_cols): 
        return
    if (field[r][c] != 0):
        return
    
    expand(field, num_rows, num_cols, r-1, c-1)
    expand(field, num_rows, num_cols, r-1, c)
    expand(field, num_rows, num_cols, r-1, c+1)
    expand(field, num_rows, num_cols, r, c-1)
    field[r][c] = -2
    expand(field, num_rows, num_cols, r, c+1)
    expand(field, num_rows, num_cols, r+1, c-1)
    expand(field, num_rows, num_cols, r+1, c)
    expand(field, num_rows, num_cols, r+1, c+1)

def click(given_field, num_rows, num_cols, given_r, given_c):
    field = [[given_field[r][c] for c in range(num_cols)] for r in range(num_rows)]
    expand(field, num_rows, num_cols, given_r, given_c)
    return field


def test_click(field, num_rows, num_cols, given_i, given_j, expected):    
    def execute():
        result = click(field, num_rows, num_cols, given_i, given_j)
        print2DArray(result)
        for r in range(num_rows):
            for c in range(num_cols):
                if (result[r][c] != expected[r][c]):
                    return False
        return True


    isTrue(lambda: execute())


# NOTE: The following input values will be used for testing your solution.
field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

test_click(field1, 3, 5, 2, 2, [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, -1, 1, 0]
])

test_click(field1, 3, 5, 1, 4, [
    [-2, -2, -2, -2, -2],
    [-2, 1, 1, 1, -2],
    [-2, 1, -1, 1, -2]
])


field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

test_click(field2, 4, 4, 0, 1,[
    [-1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, -1]
])

test_click(field2, 4, 4, 1, 3,[
    [-1, 1, -2, -2],
    [1, 1, -2, -2],
    [-2, -2, 1, 1],
    [-2, -2, 1, -1]
])
