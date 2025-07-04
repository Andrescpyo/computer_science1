
from typing import Any, Optional

class AVLNode:
    """Node for AVL Tree.

    Attributes:
        key (Any): Key used for comparison.
        value (dict): Associated value stored in the node.
        height (int): Height of the node.
        left (Optional[AVLNode]): Left child.
        right (Optional[AVLNode]): Right child.
    """

    def __init__(self, key: Any, value: dict):
        """Initializes an AVLNode.

        Args:
            key (Any): Key of the node.
            value (dict): Value associated with the node.
        """
        self.key = key
        self.value = value
        self.height = 1
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None


class AVLTree:
    """AVL Tree implementation supporting insertion, deletion, and search."""

    def __init__(self):
        """Initializes an empty AVL Tree."""
        self.root: Optional[AVLNode] = None

    def _get_height(self, node: Optional[AVLNode]) -> int:
        """Returns the height of the given node.

        Args:
            node (Optional[AVLNode]): Node to evaluate.

        Returns:
            int: Height of the node; 0 if None.
        """
        return node.height if node else 0

    def _get_balance(self, node: Optional[AVLNode]) -> int:
        """Calculates the balance factor of a node.

        Args:
            node (Optional[AVLNode]): Node to evaluate.

        Returns:
            int: Balance factor (left height - right height).
        """
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _rotate_right(self, y: AVLNode) -> AVLNode:
        """Performs a right rotation on the given node.

        Args:
            y (AVLNode): Root of the unbalanced subtree.

        Returns:
            AVLNode: New root after rotation.
        """
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1

        return x

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        """Performs a left rotation on the given node.

        Args:
            x (AVLNode): Root of the unbalanced subtree.

        Returns:
            AVLNode: New root after rotation.
        """
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1

        return y

    def _insert(self, node: Optional[AVLNode], key: Any, value: dict) -> AVLNode:
        """Recursively inserts a key-value pair into the subtree.

        Args:
            node (Optional[AVLNode]): Current node.
            key (Any): Key to insert.
            value (dict): Value associated with the key.

        Returns:
            AVLNode: Root node of the updated subtree.

        Raises:
            ValueError: If a duplicate key is inserted.
        """
        if not node:
            return AVLNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            raise ValueError("Duplicate keys are not allowed in AVL Tree.")

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insert(self, key: Any, value: dict) -> None:
        """Inserts a key-value pair into the AVL Tree.

        Args:
            key (Any): Key to insert.
            value (dict): Value associated with the key.
        """
        self.root = self._insert(self.root, key, value)

    def _min_value_node(self, node: AVLNode) -> AVLNode:
        """Finds the node with the minimum key in the subtree.

        Args:
            node (AVLNode): Root of the subtree.

        Returns:
            AVLNode: Node with the minimum key.
        """
        current = node
        while current.left:
            current = current.left
        return current

    def _delete(self, node: Optional[AVLNode], key: Any) -> Optional[AVLNode]:
        """Recursively deletes a node with the given key.

        Args:
            node (Optional[AVLNode]): Current node.
            key (Any): Key to delete.

        Returns:
            Optional[AVLNode]: Root of the updated subtree.
        """
        if not node:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._delete(node.right, temp.key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def delete(self, key: Any) -> None:
        """Deletes a node with the specified key.

        Args:
            key (Any): Key of the node to delete.
        """
        self.root = self._delete(self.root, key)

    def _search(self, node: Optional[AVLNode], key: Any) -> Optional[dict]:
        """Recursively searches for a key in the tree.

        Args:
            node (Optional[AVLNode]): Current node.
            key (Any): Key to search for.

        Returns:
            Optional[dict]: Associated value if found, else None.
        """
        if not node:
            return None
        if key == node.key:
            return node.value
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def search(self, key: Any) -> Optional[dict]:
        """Searches for a key in the AVL Tree.

        Args:
            key (Any): Key to search for.

        Returns:
            Optional[dict]: Value associated with the key, or None if not found.
        """
        return self._search(self.root, key)

    def _inorder(self, node: Optional[AVLNode], result: list) -> None:
        """Performs in-order traversal to collect node values.

        Args:
            node (Optional[AVLNode]): Current node.
            result (list): List to store traversal result.
        """
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    def get_all(self) -> list:
        """Returns all values in the AVL Tree in in-order.

        Returns:
            list: List of all node values in sorted order.
        """
        result = []
        self._inorder(self.root, result)
        return result
