# Represents one node in the double-ended queue
class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.prev = None
        self.next = None


class Deque:

    def __init__(self):
        # Front of the queue
        self.head = None

        # End of the queue
        self.tail = None

    def isEmpty(self) -> bool:
        # The queue is empty when there is no head node
        return self.head is None

    def append(self, value: int) -> None:
        # Create the new node
        new_node = ListNode(value)

        # If the queue is empty, the new node becomes
        # both the head and the tail
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            return

        # Connect the new node after the current tail
        new_node.prev = self.tail
        self.tail.next = new_node

        # Update the tail
        self.tail = new_node

    def appendleft(self, value: int) -> None:
        # Create the new node
        new_node = ListNode(value)

        # If the queue is empty, the new node becomes
        # both the head and the tail
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            return

        # Connect the new node before the current head
        new_node.next = self.head
        self.head.prev = new_node

        # Update the head
        self.head = new_node

    def pop(self) -> int:
        # Return -1 if the queue is empty
        if self.isEmpty():
            return -1

        # Save the tail's value before removing it
        value = self.tail.value

        # If there is only one node, empty the queue
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return value

        # Move the tail backward by one node
        self.tail = self.tail.prev
        self.tail.next = None

        return value

    def popleft(self) -> int:
        # Return -1 if the queue is empty
        if self.isEmpty():
            return -1

        # Save the head's value before removing it
        value = self.head.value

        # If there is only one node, empty the queue
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return value

        # Move the head forward by one node
        self.head = self.head.next
        self.head.prev = None

        return value