# Use this class to create linked lists.
class Node:
    def __init__(self, value, child=None):
        self.value = value
        self.child = child

    # The string representation of this node.
    # Will be used for testing.
    def __str__(self):
        return str(self.value)
    
    # NOTE: Feel free to use the following function for testing.
    # It converts the given linked list into an easy-to-read string format.
    # Example: 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)
    def toString(head):
        current = head
        str_list = []
        while current:
            str_list.append(str(current.value))
            current = current.child
        str_list.append('(None)')
        return ' -> '.join(str_list)

