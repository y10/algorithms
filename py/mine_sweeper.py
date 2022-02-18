from classes.utils import isTrue, print2DArray

def mine_sweeper(bombs, num_rows, num_cols):
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]

    def isBomb(r,c):
        return field[r][c] == -1

    def setBomb(r,c):
        if not isBomb(r,c):
            field[r][c] +=1

    for b in bombs:
        r, c = b[0], b[1]
        field[r][c] = -1
        
        if (r > 0):
            if (c > 0):
                setBomb(r-1, c-1)
            setBomb(r-1, c)
            if (c < num_cols-1):
                setBomb(r-1, c+1)

        if (c > 0):
            setBomb(r, c-1)
        setBomb(r, c)
        if (c < num_cols-1):
            setBomb(r, c+1)
        
        if (r < num_rows-1):
            if (c > 0):
                setBomb(r+1, c-1)
            setBomb(r+1, c)
            if (c < num_cols-1):
                setBomb(r+1, c+1)

    return field

def mine_sweeper_test(bombs, num_rows, num_cols, expected):    
    def execute():
        field = mine_sweeper(bombs, num_rows, num_cols)
        print2DArray(field)
        for r in range(num_rows):
            for c in range(num_cols):
                if (field[r][c] != expected[r][c]):
                    return False
        return True


    isTrue(lambda: execute())
    
    
mine_sweeper_test([[0, 2], [2, 0]], 3, 3, [
    [0, 1, -1], 
    [1, 2, 1], 
    [-1, 1, 0]
])

mine_sweeper_test([[1, 1]], 3, 3, [
    [1, 1, 1], 
    [1, -1, 1], 
    [1, 1, 1]
]) 

mine_sweeper_test([[0, 0], [0, 1], [1, 2]], 3, 4, [
    [-1, -1, 2, 1], 
    [2, 3, -1, 1], 
    [0, 1, 1, 1]
])

mine_sweeper_test([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5, [
    [1, 2, 2, 1, 0], 
    [1, -1, -1, 2, 0],
    [1, 3, -1, 2, 0], 
    [0, 1, 2, 2, 1], 
    [0, 0, 1, -1, 1]
]) 
