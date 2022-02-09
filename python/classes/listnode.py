from random import Random
from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if (isinstance(other, ListNode)):
            return self.val == other.val
        return False

    def toString(self):
        return str(self.val)

    def toArray(self):
        return list(self.toIterator())

    def toIterator(self):
        node = self
        while (node):
            yield node.val
            node = node.next

    @staticmethod
    def create(list:List[int]):
        prev = None
        for i in list[::-1]:
            prev = ListNode(i, prev)         
        return prev

    @staticmethod
    def generate(k = 1000, l = 500, i = 1000):
        list = []
        rnd = Random()
        for _ in range(k):
            innerlist = []
            for _ in range(rnd.randrange(0, l)):
                innerlist.append(rnd.randrange(i*-1, i))
            innerlist.sort()
            list.append(ListNode.create(innerlist))
        return list
