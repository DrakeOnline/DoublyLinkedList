# |========================================================|
# |    Title:      Main.py                                 |
# |    Author:     Drake G. Cummings                       |
# |    Purpose:    Driver file for Doubly Linked List      |
# |    Date:       March 11th, 2021                        |
# |========================================================|

# Imports
from DoublyLinkedList import DoublyLinkedList

# For printing
divider = "_________________________________"

# Driver code
print()
print(divider)

print("print test:")
test = DoublyLinkedList(7)
print(test)

print(divider)
print()

# append_left test
print("append_left test:")
test.append_left(41)
print(test)

print(divider)
print()

# append_right test
print("append_right test:")
test.append_right(8)
test.append_right(24)
test.append_right(19)
test.append_right(20)
print(test)

print(divider)
print()

# pop_left test
print("pop_left test:")
test.pop_left()
print(test)

print(divider)
print()

# pop_right test
print("pop_right test:")
test.pop_right()
print(test)

print(divider)
print()


# contains test
print(test)
print(f"contains 7: {test.contains(7)}")
print(f"contains 999: {test.contains(999)}")

print(divider)
print()
