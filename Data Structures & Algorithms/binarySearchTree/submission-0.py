from typing import List, Optional


# Represents one key-value pair in the binary search tree
class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class TreeMap:

    def __init__(self):
        # The root is None when the tree is empty
        self.root: Optional[TreeNode] = None

    def insert(self, key: int, val: int) -> None:
        # If the tree is empty, create the root node
        if self.root is None:
            self.root = TreeNode(key, val)
            return

        current = self.root

        while True:
            # Move left when the key is smaller
            if key < current.key:
                if current.left is None:
                    current.left = TreeNode(key, val)
                    return

                current = current.left

            # Move right when the key is larger
            elif key > current.key:
                if current.right is None:
                    current.right = TreeNode(key, val)
                    return

                current = current.right

            # If the key already exists, update its value
            else:
                current.val = val
                return

    def get(self, key: int) -> int:
        current = self.root

        # Search for the key using BST ordering
        while current is not None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.val

        # The key was not found
        return -1

    def getMin(self) -> int:
        # An empty tree has no minimum value
        if self.root is None:
            return -1

        current = self.root

        # The smallest key is the leftmost node
        while current.left is not None:
            current = current.left

        return current.val

    def getMax(self) -> int:
        # An empty tree has no maximum value
        if self.root is None:
            return -1

        current = self.root

        # The largest key is the rightmost node
        while current.right is not None:
            current = current.right

        return current.val

    def remove(self, key: int) -> None:
        # Replace the root with the updated tree
        self.root = self._removeNode(self.root, key)

    def _removeNode(
        self,
        node: Optional[TreeNode],
        key: int
    ) -> Optional[TreeNode]:

        # The key does not exist in the tree
        if node is None:
            return None

        # Search for the node that contains the key
        if key < node.key:
            node.left = self._removeNode(node.left, key)

        elif key > node.key:
            node.right = self._removeNode(node.right, key)

        else:
            # Case 1: The node has no left child
            if node.left is None:
                return node.right

            # Case 2: The node has no right child
            if node.right is None:
                return node.left

            # Case 3: The node has two children
            # Find the smallest node in the right subtree
            successor = node.right

            while successor.left is not None:
                successor = successor.left

            # Copy the successor's key and value into this node
            node.key = successor.key
            node.val = successor.val

            # Remove the original successor node
            node.right = self._removeNode(
                node.right,
                successor.key
            )

        return node

    def getInorderKeys(self) -> List[int]:
        keys: List[int] = []

        # Inorder traversal produces keys in ascending order
        self._inorderTraversal(self.root, keys)

        return keys

    def _inorderTraversal(
        self,
        node: Optional[TreeNode],
        keys: List[int]
    ) -> None:

        if node is None:
            return

        # Visit left subtree, current key, then right subtree
        self._inorderTraversal(node.left, keys)
        keys.append(node.key)
        self._inorderTraversal(node.right, keys)