# Project: Binary Search Tree (BST) Implementation and Analysis

This project provides a comprehensive implementation of a `Binary Search Tree (BST)` in Python. It includes core operations like insertion, deletion, and searching, alongside advanced functionalities to analyze the structural properties of the tree, such as its height, node count, and whether it qualifies as a Full, Complete, or Perfect binary tree. A visualization tool is also integrated to graphically represent the trees.

## 🌳 Binary Tree Definitions:
Understanding these specific tree types is crucial for analyzing their structure:

### `Binary Search Tree (BST): `
A **Binary Search Tree** is a specific type of binary tree where nodes are ordered to allow for efficient data retrieval, insertion, and deletion.

**Key Properties:**

- Each node contains a value.

- All values in a node's left subtree are less than or equal to the node's value.

- All values in a node's right subtree are greater than the node's value.

### `Full Binary Tree: `
A **Full Binary Tree** is a tree in which **every node has either zero or two children.** No node has only one child.

**Example:**
``` 
       A
     /   \
    B     C
         / \
        D   E 
```
### `Complete Binary Tree: `
A **Complete Binary Tree** is a binary tree where **all levels are completely filled except possibly the last level**, and all nodes in the last level are as **far left as possible.**

**Example:**
``` 
       A
     /   \
    B     C
   / \   /
  D   E F
```
### `Perfect Binary Tree :`
A **Perfect Binary Tree** is a specific type of binary tree that is both a Full Binary Tree and has **all its leaves at the same depth (or level)**.

**Key Property:** For a perfect binary tree of height $H$ (number of levels), the total number of nodes $N$ is always $2^H - 1$.

**Example:**
``` 
       A
     /   \
    B     C
   / \   / \
  D   E F   G
```

## 🚀 Getting Started: 

To run this project, make sure you have Python installed (version 3.6 or newer). You'll need to install the following libraries:

```bash
pip install networkx matplotlib
```

Once the dependencies are installed, you can execute the main program:

```bash
python main.py
```

Running the script will generate PNG images of the trees in the same directory as your project files, showcasing various tree states.

## 📂 Project Structure:

The project is organized into three distinct files:

- `main.py:` This is the primary script that demonstrates the usage of the `BinaryTree` and `BinaryTreeVisualizer` classes. It handles tree creation, manipulation, property display, and generation of different tree examples.

- `tree.py:` Contains the `Node` and `BinaryTree` class implementations. This file houses all the logic for the binary search tree operations and structural analysis methods.

- `tree_visual.py:` Provides the `BinaryTreeVisualizer` class, which uses `networkx` and `matplotlib` to generate and save visual representations of the binary trees. 

## 📝 Project Description:

## `tree.py`
This file defines the core Node and BinaryTree classes, encapsulating all the logic for BST operations and structural property checks.

### `Node` Class:
A simple class representing a node within the binary search tree. Each node stores a value and has references to its left and right children (which can be None).

```python
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
```

### `BinaryTree` Class:

The `BinaryTree` class is the core implementation of the binary search tree. It provides methods for inserting, deleting, and searching nodes, as well as advanced structural analysis methods like height, node count, and tree properties.

#### `insert(value: int) -> None:`

Inserts a new node with the given value into the binary tree. If the tree is empty, the new node becomes the root. Otherwise, it is inserted as a child of the appropriate node based on the value's relationship to the current tree.

```python
def insert(self, value: int) -> None:
        """Inserts a value into the binary tree.

        Args:
            value (int): The value to insert.
        """
        self.root = self._insert_recursive(self.root, value)
```

#### `insert_list(values: List[int]) -> None:`

Inserts a list of values into the binary tree. Each value is inserted as a separate node, following the same insertion logic as `insert()`.

```python
    def insert_list(self, values: List[int]) -> None:
        """Inserts a list of values into the binary tree.

        Args:
            values (List[int]): A list of integers to insert. Values are inserted
                in the order they appear in the list.
        """
        for value in values:
            self.insert(value)
```

#### `delete(value: int) -> None:`

Deletes a node with the given value from the binary tree. If the node is found, it is removed and its subtree is recursively deleted. If the node is not found, a `ValueError` is raised.

```python
    def delete(self, value: int) -> None:
        """Deletes a node with the specified value from the tree.

        Args:
            value (int): The value of the node to delete.
        """
        self.root = self._delete_recursive(self.root, value)
```

#### `search(value: int) -> bool:`

Searches for a node with the given value in the binary tree. If the node is found, it is returned as a boolean value. If the node is not found, the method returns `False`.

```python
    def search(self, value: int) -> bool:
        """Checks if a value exists in the tree.

        Args:
            value (int): The value to search for.

        Returns:
            bool: True if the value is found, False otherwise.
        """
        return self._search_recursive(self.root, value)
```

#### `inorder_traversal() -> List[int]:`

Generates an in-order traversal of the binary tree. The traversal is returned as a list of values, where each value corresponds to the node's value.

```python
    def inorder_traversal(self) -> List[int]:
        """Generates an in-order traversal of the tree.

        Returns:
            List[int]: A list of values in in-order (ascending) sequence.
        """
        result: List[int] = []
        self._inorder_helper(self.root, result)
        return result
```

#### `height: int`

The height of the binary tree, calculated as the maximum number of edges from the root to any leaf node.

#### `nodes: int`

The total number of nodes in the binary tree.

#### `grade: int`

The degree of the binary tree, which is the number of edges between the root and any leaf node.

#### `balanced_height: float`

The balanced height of the binary tree, calculated as the height of the largest subtree.

### `is_full() -> bool:`
Checks if the binary tree is a full binary tree. A full binary tree is a tree in which every node has either 0 or 2 children.

```python
    def is_full(self) -> bool:
        """Checks if the tree is a full binary tree.

        A full binary tree is a tree in which every node has either 0 or 2 children.
        """
        return self._is_full_recursive(self.root)
```

### `is_complete() -> bool:`
Checks if the binary tree is a complete binary tree. A complete binary tree is a binary tree in which all levels are completely filled except possibly the last level, and all nodes in the last level are as far left as possible.

```python
    def is_complete(self) -> bool:
        """Checks if the tree is a complete binary tree.

        A complete binary tree is a binary tree in which all levels are
        completely filled except possibly the last level, and all nodes
        in the last level are as far left as possible.
        """
        if self.root is None:
            return True

        queue = deque()
        queue.append(self.root)
        found_first_null = False

        while queue:
            node = queue.popleft()

            if node is None:
                found_first_null = True
            else:
                if found_first_null:
                    return False # Found a non-null node after a null node (gap)
                queue.append(node.left)
                queue.append(node.right)
        return True
```

### `is_perfect() -> bool:`
Checks if the binary tree is a perfect binary tree. A perfect binary tree is a binary tree in which all interior nodes have two children and all leaves are at the same depth or level.

```python
    def is_perfect(self) -> bool:
        """Checks if the tree is a perfect binary tree.

        A perfect binary tree is a binary tree in which all interior nodes have
        two children and all leaves are at the same depth or level.
        """
        h = self.height
        n = self.nodes
        # For a perfect binary tree, the number of nodes n should be 2^h - 1
        return n == (2**h) - 1
```

## `tree_visual.py`
This file provides the visualization capabilities for the binary trees. It uses `networkx` and `matplotlib` to generate and save visual representations of the trees.

### `BinaryTreeVisualizer` Class:

The `BinaryTreeVisualizer` class provides a static method for generating and saving visual representations of binary trees. It uses `networkx` and `matplotlib` to create PNG images of the trees.

#### `plot(tree: BinaryTree, filename: str = "binary_tree.png") -> None:`

Generates and saves a PNG image of the binary tree. The image is saved in the same directory as the script, with the specified filename.

```python
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
```

## `main.py`
This script serves as a comprehensive demonstration of the project's features. It showcases:

- Initial tree creation and population.

- Display of various tree characteristics (height, nodes, grade, balanced height).

- In-order traversal outputs.

- Initial graphical visualizations of the trees.

- Demonstration of node deletion and its impact on tree structure.

- Demonstration of node insertion.

- Detailed analysis of tree types (is_full, is_complete, is_perfect) for different tree states, including explicitly constructed examples to highlight each definition.

## 📈 Final Conclusion:

This project successfully delivers a robust and well-structured Binary Search Tree (BST) implementation in Python. We've covered the fundamental operations that make BSTs such an efficient data structure for organizing and retrieving information: node insertion, deletion, and searching.

Beyond basic operations, the added value of this work lies in its ability to analyze the tree's structural properties. The is_full(), is_complete(), and is_perfect() functions not only demonstrate a deep understanding of the theoretical definitions of these binary tree types but also provide practical tools for evaluating the efficiency and balance of any generated tree. The graphical visualization of the trees complements this analysis, offering an intuitive perspective of their shape and aiding in debugging and comprehension.

Overall, this project serves as an excellent foundation for understanding the principles of binary search trees and their variants, highlighting how their internal structure directly influences their behavior and utility in various computational applications.

## ✒️ Authors and Codes:

- Andres Cerdas Padilla / 20231020053
- Juan Esteban Bedoya Lautero / 20231020057