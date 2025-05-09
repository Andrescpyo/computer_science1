
class SlidingPuzzle:
    """Represents a 4x4 sliding puzzle."""

    def __init__(self, puzzle: str):
        """Initializes a SlidingPuzzle instance with a given state.

        Args:
            puzzle (str): A 16-character string representing the puzzle state.

        Raises:
            ValueError: If the puzzle is invalid.
        """
        self.set_puzzle(puzzle)
        self.target = "123456789ABCDEF0"
        self.move_map = self._build_move_map()

    def set_puzzle(self, puzzle: str):
        """Validates and sets the puzzle state.

        Args:
            puzzle (str): The puzzle state to validate and set.

        Raises:
            ValueError: If the puzzle does not contain 16 characters,
                        contains invalid characters,
                        lacks the '0' tile,
                        or contains duplicate characters.
        """
        allowed_chars = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'}

        if len(puzzle) != 16:
            raise ValueError("The puzzle must contain exactly 16 characters.")
        if any(c not in allowed_chars for c in puzzle):
            raise ValueError("The puzzle contains invalid characters.")
        if '0' not in puzzle:
            raise ValueError("The puzzle must include the '0' character.")
        if len(set(puzzle)) != 16:
            raise ValueError("All characters in the puzzle must be unique.")

        self.puzzle = puzzle
        self.zero_pos = self.puzzle.index('0')

    def _build_move_map(self) -> dict:
        """Generates a map of valid moves for each position on the board.

        Returns:
            dict: A dictionary mapping each position (0-15) to a list of valid
                  positions where the empty space ('0') can be moved.
        """
        moves = {}
        for pos in range(16):
            row, col = pos // 4, pos % 4
            valid = []
            if row > 0:
                valid.append(pos - 4)
            if row < 3:
                valid.append(pos + 4)
            if col > 0:
                valid.append(pos - 1)
            if col < 3:
                valid.append(pos + 1)
            moves[pos] = valid
        return moves

    def is_solvable(self) -> bool:
        """Checks whether the current puzzle configuration is solvable.

        Returns:
            bool: True if the puzzle is solvable, False otherwise.
        """
        inversions = 0
        s = self.puzzle.replace('0', '')
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if int(s[i], 16) > int(s[j], 16):
                    inversions += 1
        zero_row = self.zero_pos // 4
        blank_row_from_bottom = 4 - zero_row
        return (inversions % 2 == 0 and blank_row_from_bottom % 2 == 1) or \
               (inversions % 2 == 1 and blank_row_from_bottom % 2 == 0)
