# |========================================================|
# |    Title:      DoublyLinkedList.py                     |
# |    Author:     Drake G.Cummings                        |
# |    Purpose:    Creating a DoublyLinkedList             |
# |    Date:       March 11th, 2021                        |
# |========================================================|

class DoublyLinkedList:
    # # Members
    head = None

    # Constructor
    def __init__(self, nodeValue):
        self.head = Node(nodeValue)

    # Class Utilites
    def __str__(self):
        printout = ""
        node = self.head
        while node != None:

            # Add to printout string depending on if it's the first
            if printout == "":
                printout += f"{node.value} "
            else:
                printout += f" <-> {node.value} "

            # Print possible previous value
            if node.prev:
                printout += f"| prev value: {node.prev.value} "
            else:
                printout += f"| prev value: None "
            # Print possible next value
            if node.next:
                printout += f"| next value: {node.next.value}"
            else:
                printout += f"| next value: None "

            # Change node to next in line
            node = node.next
        return printout

    # Methods
    def append_left(self, value):
        # Create new node
        newHead = Node(value)
        # Assign new node's next to head
        newHead.next = self.head
        # Add prev
        self.head.prev = newHead
        # Set new node as head
        self.head = newHead

    def append_right(self, value):
        tail = self.get_tail()
        # Set tail's next to new node
        tail.next = Node(value)
        tail.next.prev = tail

    def pop_left(self):
        self.head = self.head.next
        self.head.prev = None

    def pop_right(self):
        # Nullify node's next
        self.get_second_from_tail().next = None

    def contains(self, value):
        contains = False

        # Check head
        node = self.head
        if node.value == value:
            return True

        # Check the rest
        while node.next != None:
            node = node.next
            if node.value == value:
                return True

        return False

    def get_tail(self):
        # Search for node without a next node
        node = self.head
        while node.next != None:
            node = node.next

        return node

    def get_second_from_tail(self):
        # Get length of linked list
        count = 1
        node = self.head
        while node.next != None:
            node = node.next
            count += 1

        # Get second-to-last node
        node = self.head
        for x in range(0, count - 2):
            node = node.next
        return node


class Node:
    # Members
    value = None
    next  = None
    prev  = None

    # Methods
    def __init__(self, nodeValue):
        self.value = nodeValue
        self.next  = None

    def __repr__(self):
        return f"Value: {self.value}"
