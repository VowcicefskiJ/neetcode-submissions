from typing import List, Optional


# Represents one node in the linked list
class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next: Optional[ListNode] = None


class LinkedList:

    def __init__(self):
        # The first node in the linked list
        self.head: Optional[ListNode] = None

        # The last node allows insertTail() to run in O(1) time
        self.tail: Optional[ListNode] = None

    def get(self, index: int) -> int:
        # Negative indexes are considered out of bounds
        if index < 0:
            return -1

        current = self.head

        # Move through the list until reaching the requested index
        for _ in range(index):
            if current is None:
                return -1
            current = current.next

        # The index is out of bounds if no node was found
        if current is None:
            return -1

        return current.val

    def insertHead(self, val: int) -> None:
        # Create a new node
        new_node = ListNode(val)

        # The new node points to the current head
        new_node.next = self.head
        self.head = new_node

        # If the list was empty, the new node is also the tail
        if self.tail is None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        # Create a new node
        new_node = ListNode(val)

        # If the list is empty, the new node becomes both head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # Attach the new node after the current tail
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        # Negative indexes are invalid
        if index < 0:
            return False

        # Remove the head node
        if index == 0:
            if self.head is None:
                return False

            self.head = self.head.next

            # If the list is now empty, clear the tail
            if self.head is None:
                self.tail = None

            return True

        current = self.head

        # Stop at the node immediately before the node being removed
        for _ in range(index - 1):
            if current is None:
                return False
            current = current.next

        # The requested index does not exist
        if current is None or current.next is None:
            return False

        node_to_remove = current.next
        current.next = node_to_remove.next

        # Update the tail if the last node was removed
        if node_to_remove == self.tail:
            self.tail = current

        return True

    def getValues(self) -> List[int]:
        values = []
        current = self.head

        # Traverse from head to tail and collect every value
        while current is not None:
            values.append(current.val)
            current = current.next

        return values