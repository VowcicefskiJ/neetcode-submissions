from typing import List

class Node:
    def __init__(self, total, L, R):
        self.sum = total      # sum of the range [L, R]
        self.L = L            # left boundary of this node's range
        self.R = R            # right boundary of this node's range
        self.left = None      # child covering the left half
        self.right = None     # child covering the right half


class SegmentTree:

    def __init__(self, nums: List[int]):
        # Build the whole tree over the full range of indices.
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums, L, R):
        # Base case: a single element — this node just holds that value.
        if L == R:
            return Node(nums[L], L, R)

        # Otherwise split the range in half, build both sides,
        # and this node's sum is the sum of its two children.
        M = (L + R) // 2
        root = Node(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index: int, val: int) -> None:
        # Kick off the recursive update from the root.
        self._update(self.root, index, val)

    def _update(self, node, index, val):
        # Found the single leaf for this index — set its new value.
        if node.L == node.R:
            node.sum = val
            return

        # Decide which half the index lives in, recurse into it,
        # then refresh this node's sum from its children.
        M = (node.L + node.R) // 2
        if index <= M:
            self._update(node.left, index, val)
        else:
            self._update(node.right, index, val)
        node.sum = node.left.sum + node.right.sum

    def query(self, L: int, R: int) -> int:
        # Kick off the recursive range-sum query from the root.
        return self._query(self.root, L, R)

    def _query(self, node, L, R):
        # This node's range sits entirely inside [L, R] — take its whole sum.
        if L <= node.L and node.R <= R:
            return node.sum

        # No overlap between this node's range and [L, R] — contributes nothing.
        if node.R < L or R < node.L:
            return 0

        # Partial overlap — ask both children and add up what they return.
        return self._query(node.left, L, R) + self._query(node.right, L, R)