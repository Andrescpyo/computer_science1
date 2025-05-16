
import os
import networkx as nx
import matplotlib.pyplot as plt
from tree import BinaryTree, Node

class BinaryTreeVisualizer:
    """Visualizes a binary search tree using matplotlib and networkx."""

    @staticmethod
    def plot(tree: BinaryTree, filename: str = "binary_tree.png") -> None:
        """Generates and saves a PNG visualization of the binary tree.

        Args:
            tree (BinaryTree): The binary tree to visualize.
            filename (str): The filename for the output PNG image.
        """
        G = nx.DiGraph()
        pos = {}
        labels = {}
        x_counter = [0]

        def add_nodes(node: Node, depth: int = 0) -> None:
            """Adds nodes and edges to the graph recursively.

            Args:
                node (Node): The current node being added.
                depth (int): The depth of the node in the tree.
            """
            if node is None:
                return

            add_nodes(node.left, depth + 1)

            node_id = id(node)
            pos[node_id] = (x_counter[0], -depth)
            labels[node_id] = str(node.value)
            G.add_node(node_id)

            if node.left:
                G.add_edge(node_id, id(node.left))
            if node.right:
                G.add_edge(node_id, id(node.right))

            x_counter[0] += 1

            add_nodes(node.right, depth + 1)

        add_nodes(tree.root)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, filename)

        plt.figure(figsize=(10, 6))
        nx.draw(
            G,
            pos,
            labels=labels,
            with_labels=True,
            arrows=False,
            node_size=1000,
            node_color="#D0E3FA",
            font_size=12
        )
        plt.title("Binary Search Tree")
        plt.axis("off")
        plt.savefig(full_path, bbox_inches="tight")
        # plt.show()
