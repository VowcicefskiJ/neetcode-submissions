from typing import List

class MinHeap:

    def __init__(self):
        # One dummy value at index 0 so real data starts at index 1.
        # This makes the parent/child math clean:
        #   left child = 2*i, right child = 2*i+1, parent = i//2
        self.heap = [0]

    def push(self, val: int) -> None:
        # Add to the end, then "bubble up" while it's smaller than its parent.
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def pop(self) -> int:
        # Smallest is always at index 1. Move the last item to the top,
        # then "bubble down" to the smaller child until it's in place.
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()   # last item becomes the new root
        i = 1
        while 2 * i < len(self.heap):
            left, right = 2 * i, 2 * i + 1
            smaller = left
            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smaller = right
            if self.heap[i] <= self.heap[smaller]:
                break
            self.heap[i], self.heap[smaller] = self.heap[smaller], self.heap[i]
            i = smaller
        return res

    def top(self) -> int:
        # Smallest is at index 1 — just peek, don't remove.
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        # Build the heap in O(n): put everything in, then bubble down
        # every non-leaf node, starting from the last one working backward.
        nums = [0] + nums
        self.heap = nums
        i = (len(self.heap) - 1) // 2   # last node that has children
        while i >= 1:
            j = i
            while 2 * j < len(self.heap):
                left, right = 2 * j, 2 * j + 1
                smaller = left
                if right < len(self.heap) and self.heap[right] < self.heap[left]:
                    smaller = right
                if self.heap[j] <= self.heap[smaller]:
                    break
                self.heap[j], self.heap[smaller] = self.heap[smaller], self.heap[j]
                j = smaller
            i -= 1