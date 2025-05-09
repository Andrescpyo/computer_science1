
from heapq import heappush, heappop
from sys import getsizeof
from services.puzzle import SlidingPuzzle


class SolverService:
    """Service class responsible for solving sliding puzzles."""

    def __init__(self, max_iterations: int = 1_000_000, mem_limit_mb: int = 2048):
        """Initializes the solver with iteration and memory limits.

        Args:
            max_iterations (int): Maximum number of iterations before stopping.
            mem_limit_mb (int): Maximum memory usage in megabytes.
        """
        self.max_iterations = max_iterations
        self.mem_limit = mem_limit_mb * 1024 ** 2

    def solve(self, puzzle: SlidingPuzzle, printer) -> list | None:
        """Solves the given sliding puzzle.

        Args:
            puzzle (SlidingPuzzle): The initial puzzle to solve.
            printer (Any): Object responsible for printing progress and results.

        Returns:
            list | None: List of moves if a solution was found; otherwise, None.
        """
        queue = PriorityQueue()
        initial = self._state_to_int(puzzle.puzzle)
        target = self._state_to_int(puzzle.target)
        queue.push(0, initial, [])
        visited = {}
        iteration = 0

        printer.print_initial(puzzle.puzzle, puzzle.target)
        last_state = initial

        while not queue.empty() and iteration < self.max_iterations:
            current_cost, state, path = queue.pop()
            last_state = state

            if state == target:
                printer.print_solution(path, iteration)
                return path

            if state in visited and visited[state] <= current_cost:
                continue

            visited[state] = current_cost
            zero_pos = self._find_zero(state)

            for move in puzzle.move_map[zero_pos]:
                new_state = self._swap(state, zero_pos, move)
                new_cost = current_cost + 1
                queue.push(new_cost, new_state, path + [self._move_to_dir(zero_pos, move)])

            iteration += 1

            if iteration % 1000 == 0:
                mem_usage = getsizeof(queue) + getsizeof(visited)
                printer.print_progress(iteration, len(queue.heap), len(visited), mem_usage)

            if getsizeof(queue) + getsizeof(visited) > self.mem_limit:
                printer.print_memory_limit(self.mem_limit)
                printer.print_final_state(self._int_to_state(last_state))
                return None

        printer.print_limit_reached(iteration)
        printer.print_final_state(self._int_to_state(last_state))
        return None

    def _state_to_int(self, state_str: str) -> int:
        """Encodes the puzzle state string into a 64-bit integer.

        Args:
            state_str (str): The puzzle string (16 hexadecimal characters).

        Returns:
            int: Encoded integer representation of the puzzle state.
        """
        value = 0
        for c in state_str:
            val = int(c, 16)
            value = (value << 4) | val
        return value

    def _int_to_state(self, state: int) -> str:
        """Decodes an integer puzzle state into a string.

        Args:
            state (int): The encoded puzzle state.

        Returns:
            str: A 16-character hexadecimal string representing the puzzle.
        """
        return f"{state:016X}"

    def _find_zero(self, state: int) -> int:
        """Finds the position of the '0' (empty space) in the puzzle.

        Args:
            state (int): Encoded puzzle state.

        Returns:
            int: Position of the empty space (0-15).
        """
        for pos in range(16):
            shift = (15 - pos) * 4
            if (state >> shift) & 0xF == 0:
                return pos
        return -1

    def _move_to_dir(self, old_pos: int, new_pos: int) -> str:
        """Returns the direction of a move from one position to another.

        Args:
            old_pos (int): Original position of the empty tile.
            new_pos (int): New position after the move.

        Returns:
            str: Direction of the move ('U', 'D', 'L', or 'R').
        """
        delta = new_pos - old_pos
        return {
            -4: 'D',
            4: 'U',
            -1: 'R',
            1: 'L'
        }[delta]

    def _swap(self, state: int, i: int, j: int) -> int:
        """Swaps two tile positions in the encoded puzzle state.

        Args:
            state (int): Current puzzle state.
            i (int): First tile index.
            j (int): Second tile index.

        Returns:
            int: New puzzle state with the tiles swapped.
        """
        shift_i = (15 - i) * 4
        shift_j = (15 - j) * 4

        val_i = (state >> shift_i) & 0xF
        val_j = (state >> shift_j) & 0xF

        state &= ~(0xF << shift_i)
        state &= ~(0xF << shift_j)

        state |= (val_j << shift_i)
        state |= (val_i << shift_j)

        return state


class PriorityQueue:
    """A custom priority queue for managing puzzle states."""

    def __init__(self):
        """Initializes an empty priority queue."""
        self.heap = []
        self.state_map = {}

    def push(self, cost: int, state: int, path: list):
        """Pushes a new state to the priority queue if it's not already present or cheaper.

        Args:
            cost (int): Cost of reaching the state.
            state (int): Encoded state.
            path (list): Path taken to reach this state.
        """
        if state not in self.state_map or cost < self.state_map[state]:
            heappush(self.heap, (cost, state, path))
            self.state_map[state] = cost

    def pop(self) -> tuple:
        """Pops the state with the lowest cost from the queue.

        Returns:
            tuple: A tuple (cost, state, path) of the next item.
        """
        cost, state, path = heappop(self.heap)
        del self.state_map[state]
        return cost, state, path

    def empty(self) -> bool:
        """Checks whether the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return not self.heap
