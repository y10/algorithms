# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# 23 on leetcode, bruteforce, DEVIDE AN CONQURE, MIN-HEAP 

from typing import List
from queue import PriorityQueue
from classes.listnode import ListNode
from classes.utils import mesureit

class Soultion:

    def mergeTwoListsMine(self, left: ListNode, right: ListNode):    
        if not (left):
            return right
        if not (right):
            return left

        if (left.val > right.val):
            left, right = right, left
        
        l = left
        while l.next and l.next.val <= right.val:
            l = l.next

        r = l.next
        l.next = right

        return self.mergeTwoListsMine(left, r)
        
    def mergeTwoListsRecur(self, left:ListNode, right:ListNode):
        if not (left):
            return right

        if not (right):
            return left
        
        if (left.val < right.val):
            left.next = self.mergeTwoLists2(left.next, right)
            return left
        else:
            right.next = self.mergeTwoLists2(left, right.next)
            return right

    def mergeTwoLists(self, left:ListNode, right:ListNode):        
        temp = ListNode()

        node = temp
        while(left and right):
            if left.val <= right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next

        node.next = left if left else right
        return temp.next 
        
    def mergeListsDevideAndConquer(self, lists:List[ListNode]):

        if(len(lists) == 0):
            return None
        
        if(len(lists) == 1):
            return lists[0]

        if(len(lists) == 2):
            return self.mergeTwoLists(lists[0], lists[1])

        m = int((len(lists)+1)/2)
        l = self.mergeListsDevideAndConquer(lists[0:m])
        r = self.mergeListsDevideAndConquer(lists[m:])

        return self.mergeTwoLists(l, r)

    def mergeListsPriorityQueue(self, lists: List[ListNode]):

        if not (lists):
            return None

        q = PriorityQueue()
        for i, node in enumerate(lists):
            if node:
                q.put((node.val, i, node))

        head = node = ListNode(0)
        while not q.empty():
            (v, i, l) = q.get()
            node.next = ListNode(v)
            node = node.next
            l = l.next
            if (l):
                q.put((l.val, i, l))

        return head.next

    def mergeListsBrutally(self, lists: List[ListNode]):
        if not (lists):
            return None

        values = []
        for l in lists:
            while l:
                values.append(l.val)
                l = l.next

        head = node = ListNode(0)

        for x in sorted(values):
            node.next = ListNode(x)
            node = node.next

        return head.next


arr = ListNode.generate(50)
mesureit(lambda:Soultion().mergeListsDevideAndConquer(arr).toArray())
mesureit(lambda:Soultion().mergeListsPriorityQueue(arr).toArray())
mesureit(lambda:Soultion().mergeListsBrutally(arr).toArray())





