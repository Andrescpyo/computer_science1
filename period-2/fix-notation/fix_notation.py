class FixNotation:

    @staticmethod
    def tree_gen(infix: str) -> str:
        stack = []
        output = []
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        for char in infix:
            if char.isalnum():
                output.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if stack:
                    stack.pop()
            else:
                while (stack and stack[-1] != '(' and
                       precedence.get(char, 0) <= precedence.get(stack[-1], 0)):
                    output.append(stack.pop())
                stack.append(char)
        while stack:
            output.append(stack.pop())
        return ''.join(output)

    @staticmethod
    def to_postfix(infix: str) -> str:
        return FixNotation.tree_gen(infix)

    @staticmethod
    def to_prefix(infix: str) -> str:
        reversed_infix = ''
        for char in reversed(infix):
            if char == '(':
                reversed_infix += ')'
            elif char == ')':
                reversed_infix += '('
            else:
                reversed_infix += char

        reversed_postfix = FixNotation.tree_gen(reversed_infix)
        return reversed_postfix[::-1]
