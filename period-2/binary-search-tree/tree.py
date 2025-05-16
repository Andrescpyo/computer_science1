
from typing import Optional, List

class Node:
    """Represents a node in a binary search tree."""

    def __init__(self, value: int):
        """Initializes a Node.

        Args:
            value (int): The value to store in the node.
        """
        self.value: int = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BinaryTree:
    """Implements a binary search tree."""

    def __init__(self):
        """Initializes an empty binary search tree."""
        self.root: Optional[Node] = None

    def insert(self, value: int) -> None:
        """Inserts a value into the binary tree.

        Args:
            value (int): The value to insert.
        """
        self.root = self._insert_recursive(self.root, value)

    def insert_list(self, values: List[int]) -> None:
        """Inserts a list of values into the binary tree.

        Args:
            values (List[int]): A list of integer values to insert.
        """
        for value in values:
            self.insert(value)

    def _insert_recursive(self, node: Optional[Node], value: int) -> Node:
        """Recursively inserts a value starting from a given node.

        Args:
            node (Optional[Node]): The current node in recursion.
            value (int): The value to insert.

        Returns:
            Node: The modified subtree with the new node inserted.
        """
        if node is None:
            return Node(value)

        if value <= node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)

        return node

    def search(self, value: int) -> bool:
        """Searches for a value in the binary tree.

        Args:
            value (int): The value to search for.

        Returns:
            bool: True if found, False otherwise.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: Optional[Node], value: int) -> bool:
        """Recursively searches for a value in the tree.

        Args:
            node (Optional[Node]): The current node in recursion.
            value (int): The value to search.

        Returns:
            bool: True if found, False otherwise.
        """
        if node is None:
            return False

        if node.value == value:
            return True

        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def delete(self, value: int) -> None:
        """Deletes a node with the specified value from the tree.

        Args:
            value (int): The value to delete.
        """
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node: Optional[Node], value: int) -> Optional[Node]:
        """Recursively deletes a node from the tree.

        Args:
            node (Optional[Node]): The current node in recursion.
            value (int): The value to delete.

        Returns:
            Optional[Node]: The modified subtree with the node removed.
        """
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)

        return node

    def _min_value_node(self, node: Node) -> Node:
        """Finds the node with the minimum value in a subtree.

        Args:
            node (Node): The root of the subtree.

        Returns:
            Node: The node with the smallest value.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, node: Optional[Node]) -> str:
        """Returns the in-order traversal of the tree as a string.

        Args:
            node (Optional[Node]): The root node to start traversal from.

        Returns:
            str: Space-separated in-order traversal of the tree.
        """
        result: List[str] = []
        self._inorder_helper(node, result)
        return " ".join(result)

    def _inorder_helper(self, node: Optional[Node], result: List[str]) -> None:
        """Recursive helper for in-order traversal.

        Args:
            node (Optional[Node]): The current node in traversal.
            result (List[str]): Accumulator for the traversal result.
        """
        if node is not None:
            self._inorder_helper(node.left, result)
            result.append(str(node.value))
            self._inorder_helper(node.right, result)
