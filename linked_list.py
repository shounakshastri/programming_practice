class Node:
    def __init__(self, data):
        self.data = data # Value of the data
        self.next = None # pointer to the next node. None if last

class LinkedList:
    def __init__(self):
        self.head = None # Points to the first node

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current=current.next
            current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map, str(elements)))
