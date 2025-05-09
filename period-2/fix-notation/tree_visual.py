
from graphviz import Digraph

class TreeNode:
    """Node for binary expression tree."""
    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTreeVisualizer:
    @staticmethod
    def build_tree_from_postfix(postfix: str) -> TreeNode:
        stack = []
        for char in postfix:
            if char.isalnum():
                stack.append(TreeNode(char))
            else:
                right = stack.pop()
                left = stack.pop()
                node = TreeNode(char)
                node.left = left
                node.right = right
                stack.append(node)
        return stack[-1]

    @staticmethod
    def generate_image(root: TreeNode, filename: str = "expression_tree") -> None:
        dot = Digraph()
        ExpressionTreeVisualizer._add_nodes_edges(dot, root)
        dot.render(filename, format="png", cleanup=True)

    @staticmethod
    def _add_nodes_edges(dot: Digraph, node: TreeNode, count: dict = None) -> str:
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
