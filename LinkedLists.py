# A linked list is a linear data structure where elements are stored in nodes,
# and each node contains a reference/link to the next node in the sequence. This structure
# allows for efficient insertions and deletions since you only need to update the links between the nodes,
# rather than shifting the entire elements like in an array.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head == 0:
            self.head = new_node
            return
