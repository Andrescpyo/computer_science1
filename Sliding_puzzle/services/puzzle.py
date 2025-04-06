
class SlidingPuzzle:

    """Represents a 4x4 sliding puzzle initialized from a 16-character string."""

    def __init__(self, puzzle: str):
        """Initializes the SlidingPuzzle instance.

        Args:
            puzzle (str): A 16-character string representing the puzzle state.
                          Must include all hexadecimal digits from 0 to F (uppercase),
                          each appearing exactly once, and must contain the '0' character
                          representing the empty space.

        Raises:
            ValueError: If the puzzle string does not meet validation rules.
        """
        self.set_puzzle(puzzle)

    def set_puzzle(self, puzzle: str):
        """Validates and sets the puzzle string.

        Args:
            puzzle (str): The puzzle string to be validated and stored.

        Raises:
            ValueError: If the string is not exactly 16 characters,
                        contains invalid characters,
                        does not contain '0',
                        or contains duplicate characters.
        """
        allowed_chars = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'}

        if len(puzzle) != 16:
            raise ValueError("The puzzle must have exactly 16 characters")

        for c in puzzle:
            if c not in allowed_chars:
                raise ValueError(f"Invalid character: '{c}'. Only 0-9 digits and \
                                 capital A-F letters are allowed")

        if '0' not in puzzle:
            raise ValueError("The puzzle must include the '0' character")

        if len(set(puzzle)) != 16:
            raise ValueError("All characters must be unique")

        self.puzzle = puzzle

    def solve(self):
        pass
