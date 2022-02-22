# Implement your function below.
from classes.node import Node
from classes.utils import testit

def nth_from_last(head:Node, n):

    if not head:
        return None

    left = right = head

    for i in range(n):
        if not (right):
            return None
        right = right.child

    while(right):
        right = right.child
        left = left.child
    
    return left.value

def nth_from_last_inefficeint(head:Node, n):

    q = []

    if not head:
        return None

    print(head.toString())

    node = head
    while(node):
        q.append(node.value)
        node = node.child

    if len(q) < n:
        return None
    
    return q[len(q)-n]

# NOTE: The following input values will be used for testing your solution.
current = Node(1)
for i in range(2, 8):
    current = Node(i, current)
head = current
# head = 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)

current2 = Node(4)
for i in range(3, 0, -1):
    current2 = Node(i, current2)
head2 = current2
# head2 = 1 -> 2 -> 3 -> 4 -> (None)



testit(lambda: nth_from_last(head, 1), 1)
testit(lambda: nth_from_last(head, 5), 5)
testit(lambda: nth_from_last(head2, 2), 3)
testit(lambda: nth_from_last(head2, 4), 1)
testit(lambda: nth_from_last(head2, 5), None)
testit(lambda: nth_from_last(None, 1), None)
