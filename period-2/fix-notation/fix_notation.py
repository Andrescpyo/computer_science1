
import re

class FixNotation:
    """Provides methods to convert infix expressions into postfix and prefix notations."""

    @staticmethod
    def tokenize(expression: str) -> list:
        """Splits an infix expression into tokens.

        Args:
            expression (str): The mathematical expression in infix notation.

        Returns:
            list: A list of tokens (numbers, variables, operators, parentheses).
        """
        tokens = re.findall(r'\d+|[a-zA-Z]+|[+\-*/^()]', expression.replace(' ', ''))
        return tokens

    @staticmethod
    def to_postfix(infix: str) -> str:
        """Converts an infix expression into postfix (RPN) notation.

        Args:
            infix (str): The input infix expression.

        Returns:
            str: A string representing the postfix notation of the expression.
        """
        tokens = FixNotation.tokenize(infix)

        def tree_gen(tokens: list) -> list:
            stack = []
            output = []
            precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
            for token in tokens:
                if token.isalnum():
                    output.append(token)
                elif token == '(':
                    stack.append(token)
                elif token == ')':
                    while stack and stack[-1] != '(':
                        output.append(stack.pop())
                    if stack:
                        stack.pop()
                else:
                    while (stack and stack[-1] != '(' and
                           precedence.get(token, 0) <= precedence.get(stack[-1], 0)):
                        output.append(stack.pop())
                    stack.append(token)
            while stack:
                output.append(stack.pop())
            return output

        postfix = tree_gen(tokens)
        return ' '.join(postfix)

    @staticmethod
    def to_prefix(infix: str) -> str:
        """Converts an infix expression into prefix notation.

        Args:
            infix (str): The input infix expression.

        Returns:
            str: A string representing the prefix notation of the expression.
        """
        postfix = FixNotation.to_postfix(infix).split()

        def build_tree(postfix_tokens):
            stack = []
            for token in postfix_tokens:
                if token.isalnum():
                    stack.append((token, None, None))
                else:
                    right = stack.pop()
                    left = stack.pop()
                    stack.append((token, left, right))
            return stack[0]

        def preorder(node):
            if node is None:
                return []
            value, left, right = node
            return [value] + preorder(left) + preorder(right)

        tree_root = build_tree(postfix)
        prefix_tokens = preorder(tree_root)
        return ' '.join(prefix_tokens)
