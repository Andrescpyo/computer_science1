
class sliding_puzzle:

    def __init__(self, puzzle: str):

        self.__set_puzzle(puzzle)

    def __set_puzzle(self, puzzle: str):

        if len(puzzle) != 16:
            raise ValueError("Puzzle must be 16 numbers long, including 0")
        
        self.puzzle = puzzle
