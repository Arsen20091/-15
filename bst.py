"""Basic binary search tree (BST) implementation."""

from __future__ import annotations

from typing import Any, Optional, Tuple


class TreeNode:
    """A node of a binary search tree."""

    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class BinarySearchTree:
    """Binary search tree with core operations."""

    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None

    def insert(self, key: Any, value: Any) -> None:
        """Insert key/value pair into BST. Updates value for existing key."""
        if self.root is None:
            self.root = TreeNode(key, value)
            return

        current = self.root
        while current is not None:
            if key < current.key:
                if current.left is None:
                    current.left = TreeNode(key, value)
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = TreeNode(key, value)
                    return
                current = current.right
            else:
                current.value = value
                return

    def search(self, key: Any) -> Optional[Any]:
        """Return value by key or None if key is absent."""
        current = self.root
        while current is not None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.value
        return None

    def delete(self, key: Any) -> None:
        """Delete node by key if it exists."""
        self.root = self._delete(self.root, key)

    def _delete(self, node: Optional[TreeNode], key: Any) -> Optional[TreeNode]:
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
            return node
        if key > node.key:
            node.right = self._delete(node.right, key)
            return node

        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        successor = self._min_node(node.right)
        node.key, node.value = successor.key, successor.value
        node.right = self._delete(node.right, successor.key)
        return node

    def _min_node(self, node: TreeNode) -> TreeNode:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def height(self) -> int:
        """Return tree height in nodes (empty tree height is 0)."""
        return self._height(self.root)

    def _height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def is_balanced(self) -> bool:
        """Check if tree is height-balanced."""
        balanced, _ = self._check_balance(self.root)
        return balanced

    def _check_balance(self, node: Optional[TreeNode]) -> Tuple[bool, int]:
        if node is None:
            return True, 0

        left_balanced, left_height = self._check_balance(node.left)
        right_balanced, right_height = self._check_balance(node.right)

        is_current_balanced = (
            left_balanced
            and right_balanced
            and abs(left_height - right_height) <= 1
        )
        return is_current_balanced, 1 + max(left_height, right_height)
