
import os
from graphviz import Digraph

class TreeNode:
    """Represents a node in a binary expression tree.

    Attributes:
        value (str): The value of the node (operator or operand).
        left (TreeNode): The left child node.
        right (TreeNode): The right child node.
    """

    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None


class ExpressionTreeVisualizer:
    """Generates a visual representation of a binary expression tree."""

    @staticmethod
    def build_tree_from_postfix(postfix_expr: str) -> TreeNode:
        """Builds an expression tree from a postfix expression.

        Args:
            postfix_expr (str): The postfix expression with tokens separated by spaces.

        Returns:
            TreeNode: The root node of the constructed expression tree.
        """
        tokens = postfix_expr.split()
        stack = []
        for token in tokens:
            if token.isalnum():
                stack.append(TreeNode(token))
            else:
                right = stack.pop()
                left = stack.pop()
                node = TreeNode(token)
                node.left = left
                node.right = right
                stack.append(node)
        return stack[-1]

    @staticmethod
    def generate_image(root: TreeNode, filename: str = "expression_tree"):
        """Generates and saves a PNG image of the expression tree.

        Args:
            root (TreeNode): The root node of the tree to visualize.
            filename (str): Name of the output file (without extension).
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, filename)

        dot = Digraph()
        ExpressionTreeVisualizer._add_nodes_edges(dot, root)
        dot.render(full_path, format="png", cleanup=True)

    @staticmethod
    def _add_nodes_edges(dot: Digraph, node: TreeNode, count: dict = None) -> str:
        """Recursively adds nodes and edges to the Graphviz graph.

        Args:
            dot (Digraph): The Graphviz object to add nodes and edges to.
            node (TreeNode): The current node in the expression tree.
            count (dict): A counter dictionary to generate unique node IDs.

        Returns:
            str: The unique identifier of the current node.
        """
        if count is None:
            count = {"id": 0}

        node_id = str(count["id"])
        dot.node(node_id, node.value)
        current_id = count["id"]
        count["id"] += 1

        if node.left:
            left_id = ExpressionTreeVisualizer._add_nodes_edges(dot, node.left, count)
            dot.edge(str(current_id), left_id)

        if node.right:
            right_id = ExpressionTreeVisualizer._add_nodes_edges(dot, node.right, count)
            dot.edge(str(current_id), right_id)

        return str(current_id)
