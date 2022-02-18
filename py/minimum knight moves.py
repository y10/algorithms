from typing import List, Tuple
from classes.utils import mesureit, testit

class Solution:
    def __init__(self):
        self.dic = {}

    def nextMoves(self, x: int, y: int):
    
        def generate():
            yield  x-1, y-2
            yield  x-2, y-1
            yield  x-2, y+1
            yield  x-1, y+2

            yield  x+1, y+2
            yield  x+2, y+1
            yield  x+2, y-1
            yield  x+1, y-2

        for (nx, ny) in generate():
            if not f"{nx},{ny}" in self.dic:
                yield nx, ny
            else:
                pass
    
    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [(0, 0)]

        l = 0
        while(moves):
            l += 1
            p = moves.pop()
            for (nx, ny) in self.nextMoves(p[0], p[1]):
                if (nx == x and ny == y):
                    return l
                else:
                    self.dic[f"{nx},{ny}"] = 1
                    moves.append((nx,ny))

        return -1

testit(lambda:Solution().minKnightMoves(0, 1), 1)
testit(lambda:Solution().minKnightMoves(2, 1), 1)
testit(lambda:Solution().minKnightMoves(5, 5), 4)