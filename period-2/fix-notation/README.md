# Project: Conversion and Visualization of Mathematical Notations

This project provides tools for converting mathematical expressions between different notations: infix, postfix (RPN - Reverse Polish Notation), and prefix (Direct Polish Notation). It also offers the ability to generate a graphical display of the expression tree corresponding to the postfix notation.

## Project Structure

The project is divided into the following files:

- `fix_notation.py`: Contains the `FixNotation` class with methods for converting between mathematical notations.
- `tree_visual.py`: Contains the `TreeNode` and `ExpressionTreeVisualizer` classes for building and visualizing the expression tree.
- `main.py`: An example script demonstrating the use of the project's features.

## Mathematical Notation Definitions

### Infix Notation

Infix notation is the most common form of writing mathematical expressions. Operators are placed *between* the operands.

**Example:**

```
2 + 3
a * (b - c)
```

### Postfix Notation (RPN - Reverse Polish Notation)

In postfix notation, operators are placed *after* their operands. This notation eliminates the need for parentheses to specify the order of operations.

**Example:**

```
The infix expression `2 + 3` 
in postfix notation is: `2 3 +`

The infix expression `a * (b - c)` 
in postfix notation is: `a b c - *`
```
To evaluate an expression in postfix notation, a stack is used. When an operand is encountered, it is pushed onto the stack. When an operator is encountered, the top two operands are popped, the operator is applied, and the result is pushed back onto the stack. The final result is the only value remaining on the stack.

### Prefix Notation (Direct Polish Notation)

In prefix notation, operators are placed *before* their operands. Like postfix notation, it eliminates the need for parentheses.

**Example:**
```
The infix expression `2 + 3` 
in prefix notation is: `+ 2 3`

The infix expression `a * (b - c)` 
in prefix notation is: `* a - b c`
```

To evaluate an expression in prefix notation, a stack can also be used, although the expression is usually read from right to left. When an operand is encountered, it is pushed onto the stack. When an operator is encountered, the top two operands are popped (taking into account their order), the operator is applied, and the result is pushed onto the stack again.

## `fix_notation.py`

This file defines the `FixNotation` class, which provides static methods for manipulating mathematical expressions in infix notation.

### `tokenize(expression: str) -> list`

Splits an infix expression into a list of tokens (numbers, variables, operators, and parentheses).

**Args:**

- `expression (str)`: The mathematical expression in infix notation.

**Returns:**

- `list`: A list of strings representing the tokens in the expression.

**Example:**

```python
from fix_notation import FixNotation

expression = "2 + (3 * 4)"
tokens = FixNotation.tokenize(expression)
print(tokens) # Output: ['2', '+', '(', '3', '*', '4', ')']
```
### `to_postfix(expression: str) -> str`
Converts a mathematical expression from infix notation to postfix notation (Reverse Polish Notation).

**Args:**

- `infix (str):` The mathematical expression in infix notation.

**Returns:**

- `str:` A string representing the expression in postfix notation, with tokens separated by spaces.

**Example:**

```python
from fix_notation import FixNotation

infix_expression = "a * (b + c) / d"
postfix_expression = FixNotation.to_postfix(infix_expression)
print(postfix_expression) # Output: a b c + * d /
```

### `to_prefix(infix: str) -> str`

Converts a mathematical expression from infix notation to prefix notation (Direct Polish Notation).

**Args:**

- `infix (str):` The mathematical expression in infix notation.

**Returns:**

- `str:` A string representing the expression in prefix notation, with tokens separated by spaces.

**Example:**

```python
from fix_notation import FixNotation

infix_expression = "a * (b + c) / d"
prefix_expression = FixNotation.to_prefix(infix_expression)
print(prefix_expression) # Output: / * a + b c d
```

## `tree_visual.py`

This file contains the classes needed to build an expression tree from postfix notation and generate a visual representation of that tree.

### `TreeNode`

A simple class for representing a node in a binary expression tree. Each node can contain a value (operator or operand) and references to its left and right children.

### `ExpressionTreeVisualizer`

The `ExpressionTreeVisualizer` class provides static methods for building and visualizing an expression tree from postfix notation.

#### `build_tree_from_postfix(postfix_expr: str) -> TreeNode`

Builds an expression tree from postfix notation.

**Args:**

- `postfix_expr (str):` A string representing the expression in postfix notation, with tokens separated by spaces.


**Returns:**

- `TreeNode:` The root node of the constructed expression tree.

#### `generate_image(root: TreeNode, filename: str = "expression_tree")`

Generates and saves a PNG image of the expression tree.

**Args:**

- `root (TreeNode):` The root node of the expression tree.
- `filename (str):` Name of the output file (without extension).

## `dependency:`

For the visualization to work properly, you must have the graphviz package installed on your system and the graphviz Python library. You can install the library with pip:

```bash
pip install graphviz
```

Also, make sure the Graphviz executable is in your system PATH (see the troubleshooting section if you're having trouble with this).

## `main.py`

This is an example script that demonstrates how to use the `FixNotation` and `ExpressionTreeVisualizer` classes. It defines an infix expression, converts it to a postfix and prefix expression, prints the results, and then generates an image of the postfix expression tree.

To run the script, simply navigate to the project directory from your terminal and run:

```bash
python main.py
```

This will print the postfix and prefix notations to the console and save an image of the postfix expression tree as postfix_tree.png in the same directory.

## Usage:

**1. Save the files:** Make sure you have the `fix_notation.py`, `tree_visual.py`, and `main.py` files in the same directory.

**2. Install Graphviz:** If you want to use the tree visualization functionality, install `graphviz` and its Python library (pip install graphviz). Make sure the Graphviz executable is in your PATH.

**3. Run `main.py`:** To see an example of how the classes are used, run the `main.py` script and enjoy!

## ✒️ Authors and Codes:

- Andres Cerdas Padilla / 20231020053
- Juan Esteban Bedoya Lautero / 20231020057