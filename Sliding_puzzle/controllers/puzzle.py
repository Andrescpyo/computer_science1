
from services.puzzle import SlidingPuzzle
from services.puzzle_solver import SolverService
from services.puzzle_cli import PrinterService

class PuzzleController:
    """Controller class that manages the puzzle solving logic."""

    @staticmethod
    def solve_puzzle(puzzle: str) -> list:
        """Solves a sliding numerical puzzle represented by a 16-character string.

        Args:
            puzzle (str): A 16-character string representing the initial state of the puzzle.
                          Example: "123456789ABCDFE0" for a 4x4 puzzle.
                          The numbers from 1 to 9 are represented directly,
                          A = 10, B = 11, C = 12, D = 13, E = 14, F = 15. '0' represents the empty space.

        Returns:
            list: A list of moves leading from the initial to the goal state.
                  Each element in the list is a character representing a direction ('U', 'D', 'L', 'R').
                  Returns None if no solution was found within the constraints.
        """
        my_puzzle = SlidingPuzzle(puzzle)
        solver = SolverService(1000000)
        printer = PrinterService()
        solution = solver.solve(my_puzzle, printer)
        return solution
