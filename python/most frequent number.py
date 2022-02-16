from collections import defaultdict
from queue import PriorityQueue
from typing import List
from classes.utils import testit

class Solution:
    def mostFrequentNumber(self, given_list:List[int]) -> int:
        
        nums = defaultdict(lambda: 0)
        
        for num in given_list:
            nums[num] += 1

        q = PriorityQueue()
        for num in nums:
            q.put((-nums[num], num))

        if not (q.empty()):
            return q.get()[1]

        return None

testit(lambda:Solution().mostFrequentNumber([]), None)
testit(lambda:Solution().mostFrequentNumber([0]), 0)
testit(lambda:Solution().mostFrequentNumber([1, 3, 1, 3, 2, 1]), 1)
testit(lambda:Solution().mostFrequentNumber([3, 3, 1, 3, 2, 1]), 3)
testit(lambda:Solution().mostFrequentNumber([0, -1, 10, 10, -1, 10, -1, -1, -1, 1]), -1)

 
