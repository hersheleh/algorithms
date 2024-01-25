class ListNode:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.sentinel = self.head

    def insert_next(self, element):
        new_element = ListNode(element)

        if (self.size == 0):
            self.head = new_element
            self.tail = new_element
        else:
            self.tail.next_node = new_element
            self.tail = new_element
        
    
    
