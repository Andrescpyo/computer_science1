
from controllers.puzzle import PuzzleController

if __name__ == "__main__":
    PUZZLE = "123456789ABCDFE0"
    solution = PuzzleController.solve_puzzle(PUZZLE)
