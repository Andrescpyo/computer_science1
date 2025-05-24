from math import log2
from typing import Optional, List

class Node:
    """Represents a node in a binary search tree."""

    def __init__(self, value: int):
        """Initializes a Node with the given value.

        Args:
            value (int): The value to store in the node.
        """
        self.value: int = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BinaryTree:
    """Implements a binary search tree with basic operations."""

    def __init__(self):
        """Initializes an empty binary search tree."""
        self.root: Optional[Node] = None
        self.grade: int = 2

    def __str__(self) -> str:
        """Generates a string representation of the tree in in-order traversal.
        Returns:
            str: A string representation of the tree's values in in-order.
        """
        return " ".join(str(num) for num in self.inorder_traversal())

    @property
    def height(self) -> int:
        """int: The height of the tree, measured as the number of levels."""
        return self._get_height(self.root)

    @property
    def nodes(self) -> int:
        """int: The total number of nodes in the tree."""
        return self._count_nodes(self.root)

    @property
    def balanced_height(self) -> int:
        """int: The minimal possible height of a perfectly balanced tree.

        This represents the theoretical minimum height achievable by a complete
        binary tree with the same number of nodes. For an empty tree, returns 0.
        """
        n = self.nodes
        if n == 0:
            return 0
        return int(log2(n) + 1)

    def _get_height(self, node: Optional[Node]) -> int:
        """Calculates the height of the subtree rooted at the given node.

        Args:
            node (Optional[Node]): The root node of the subtree.

        Returns:
            int: Height of the subtree. Returns 0 if the node is None.
        """
        if node is None:
            return 0
        left = self._get_height(node.left)
        right = self._get_height(node.right)
        height = max(left, right) + 1
        return height

    def insert(self, value: int) -> None:
        """Inserts a value into the binary tree.

        Args:
            value (int): The value to insert.
        """
        self.root = self._insert_recursive(self.root, value)

    def insert_list(self, values: List[int]) -> None:
        """Inserts a list of values into the binary tree.

        Args:
            values (List[int]): A list of integers to insert. Values are inserted
                in the order they appear in the list.
        """
        for value in values:
            self.insert(value)

    def _insert_recursive(self, node: Optional[Node], value: int) -> Node:
        """Recursively inserts a value into the subtree rooted at the given node.

        Args:
            node (Optional[Node]): The root node of the current subtree.
            value (int): The value to insert.

        Returns:
            Node: The root node of the modified subtree.
        """
        if node is None:
            return Node(value)
        if value <= node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        return node

    def _count_nodes(self, node: Optional[Node]) -> int:
        """Counts the number of nodes in the subtree rooted at the given node.

        Args:
            node (Optional[Node]): The root node of the subtree.

        Returns:
            int: Number of nodes in the subtree. Returns 0 if the node is None.
        """
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def search(self, value: int) -> bool:
        """Checks if a value exists in the tree.

        Args:
            value (int): The value to search for.

        Returns:
            bool: True if the value is found, False otherwise.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: Optional[Node], value: int) -> bool:
        """Recursively searches for a value in the subtree rooted at the given node.

        Args:
            node (Optional[Node]): The root node of the current subtree.
            value (int): The value to search for.

        Returns:
            bool: True if the value is found in the subtree, False otherwise.
        """
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def delete(self, value: int) -> None:
        """Deletes a node with the specified value from the tree.

        Args:
            value (int): The value of the node to delete.
        """
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node: Optional[Node], value: int) -> Optional[Node]:
        """Recursively deletes a node with the given value from the BST.

        Args:
            node (Optional[Node]): The current node in the recursive traversal.
            value (int): The value to delete from the tree.

        Returns:
            Optional[Node]: The updated node after deletion.
        """
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            temp = self._max_value_node(node.left)
            node.value = temp.value
            node.left = self._delete_recursive(node.left, temp.value)
        return node

    def _max_value_node(self, node: Node) -> Node:
        """Finds the node with the maximum value in the subtree rooted at the given node.

        Args:
            node (Node): The root of the subtree.

        Returns:
            Node: The node with the maximum value in the subtree.
        """
        current = node
        while current.right is not None:
            current = current.right
        return current

    def inorder_traversal(self) -> List[int]:
        """Generates an in-order traversal of the tree.

        Returns:
            List[int]: A list of values in in-order (ascending) sequence.
        """
        result: List[int] = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node: Optional[Node], result: List[int]) -> None:
        """Recursively performs in-order traversal of the subtree.

        Args:
            node (Optional[Node]): The current root node of the subtree.
            result (List[int]): List to accumulate the traversal results.
        """
        if node is not None:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)
