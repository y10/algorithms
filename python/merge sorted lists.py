# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# 23 on leetcode, bruteforce, Divide AN CONQURE, MIN-HEAP 

import heapq
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

    def mergeListsDivideAndConquer(self, lists:List[ListNode]):
        return self.mergeListsDivideAndConquer1(lists)

    def mergeListsDivideAndConquer1(self, lists:List[ListNode]):

        k = len(lists)
        interval = 1
        while interval < k:
            for i in range(0, k - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if k > 0 else None

    def mergeListsDivideAndConquer2(self, lists:List[ListNode]):

        if(len(lists) == 0):
            return None
        
        if(len(lists) == 1):
            return lists[0]

        m = int((len(lists)+1)/2)
        l = self.mergeListsDivideAndConquer(lists[0:m])
        r = self.mergeListsDivideAndConquer(lists[m:])

        return self.mergeTwoLists(l, r)

    def mergeListsDivideAndConquer3(self, lists:List[ListNode], l:int, r:int):

        if(l > r):
            return None
        
        if(l == r):
            return lists[l]

        mid = int((l+r)/2)
        left = self.mergeListsDivideAndConquer3(lists, l, mid)
        right = self.mergeListsDivideAndConquer3(lists, mid+1, r)

        return self.mergeTwoLists(left, right)        

    def mergeListsPriorityQueue(self, lists: List[ListNode]):

        if not (lists):
            return None

        q = []
        for node in lists:
            if node:
                heapq.heappush(q, (node.val, node))

        head = node = ListNode(0)
        while q:
            (v, top) = heapq.heappop(q)
            node.next = top
            node = node.next
            top = top.next
            if (top):
                heapq.heappush(q, (top.val, top))

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

mesureit(lambda:Soultion().mergeListsPriorityQueue(ListNode.deserializeLists('./assets/sorted linked lists.txt')).toArray())
mesureit(lambda:Soultion().mergeListsDivideAndConquer(ListNode.deserializeLists('./assets/sorted linked lists.txt')).toArray())
mesureit(lambda:Soultion().mergeListsBrutally(ListNode.deserializeLists('./assets/sorted linked lists.txt')).toArray())





