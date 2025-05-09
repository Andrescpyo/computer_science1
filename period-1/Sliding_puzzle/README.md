# Branch and Bound Solver for 4x4 Sliding Puzzles

This project implements a branch and bound algorithm to solve 4x4 sliding puzzles. The solution leverages a priority queue to explore puzzle states by increasing move cost while avoiding revisiting states that have already been processed with a lower cost. The algorithm is optimized to handle memory constraints and iteration limits.

## Overview

- **Puzzle Representation:**  
  The puzzle is represented as a 16-character string using hexadecimal digits (`0-9, A-F`), where `0` denotes the blank space. The target configuration is `"123456789ABCDEF0"`.

- **Branch and Bound Strategy:**  
  The solver uses a **branch and bound** technique to efficiently explore possible moves:
  - **Branching:** Each state (or node) branches into new states by moving the blank space in allowed directions (up, down, left, right).
  - **Bounding:** The priority queue keeps track of states with their associated cost. States are pruned if they have been reached with a lower or equal cost before, thereby reducing unnecessary exploration.

- **Memory & Iteration Limits:**  
  To ensure performance and avoid resource exhaustion, the algorithm includes limits for the maximum number of iterations and memory usage. Progress is periodically printed, and the final reached state is reported if limits are hit.

## Key Components

### 1. `SlidingPuzzle` Class

The `SlidingPuzzle` class manages the puzzle's initialization, validation, and allowed moves. Below is an explanation of its main functions:

- **`set_puzzle`:**  
  Validates the puzzle string to ensure it has 16 unique hexadecimal characters and that the blank space (`0`) is present.

  ```python
  def set_puzzle(self, puzzle: str):
      allowed_chars = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'}
      if len(puzzle) != 16:
          raise ValueError("El puzzle debe tener 16 caracteres")
      if any(c not in allowed_chars for c in puzzle):
          raise ValueError("Caracteres inválidos")
      if '0' not in puzzle:
          raise ValueError("El puzzle debe contener '0'")
      if len(set(puzzle)) != 16:
          raise ValueError("Caracteres duplicados")
          
      self.puzzle = puzzle
      self.zero_pos = self.puzzle.index('0')

- **`_build_move_map`:**  
  Constructs a mapping of each cell position to its valid adjacent moves. This precomputed map speeds up state exploration during the search.
  ```python
  def _build_move_map(self):
      moves = {}
      for pos in range(16):
          row, col = pos // 4, pos % 4
          valid = []
          if row > 0: valid.append(pos - 4)  # Up
          if row < 3: valid.append(pos + 4)  # Down
          if col > 0: valid.append(pos - 1)  # Left
          if col < 3: valid.append(pos + 1)  # Right
          moves[pos] = valid
      return moves

- **`is_solvable`:**  
  Determines if a puzzle configuration can be solved by counting the inversions (pairs of tiles that are in the wrong order) and considering the blank row position from the bottom. This is crucial for avoiding fruitless searches.
  ```python
  def is_solvable(self) -> bool:
    inversions = 0
    s = self.puzzle.replace('0', '')
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if int(s[i], 16) > int(s[j], 16):
                inversions += 1
    zero_row = self.zero_pos // 4
    blank_row_from_bottom = 4 - zero_row  # 1-based from the bottom
    return (inversions % 2 == 0 and blank_row_from_bottom % 2 == 1) or \
           (inversions % 2 == 1 and blank_row_from_bottom % 2 == 0)

### 2. `SolverService` Class

The `SolverService` class implements the branch and bound search:

- **State Representation:**  
  Puzzle states are converted from a string to an integer using hexadecimal representation. This allows efficient bit-level operations.

- **Priority Queue:**  
  States are inserted into a priority queue with their associated move cost. The queue ensures that the next state processed has the lowest cost so far.


- **Branching and Bounding:**  
  For every iteration:

  - The current state is checked against the target.

  -  The allowed moves (using the `move_map` from `SlidingPuzzle`) generate new states.

  - States already visited with a lower cost are skipped (bounding).
- **Resource Constraints:**  
  The service monitors memory usage and iteration count. If limits are reached, it prints the current progress and the latest state configuration reached.

### 3. `PrinterService` Class
The `PrinterService` handles output:
- **Progress Reporting:**  
  It prints updates every fixed number of iterations, showing the current iteration, queue size, visited count, and approximate memory usage.

- **Final State Reporting:**  
  When the iteration or memory limit is reached, it prints the last reached configuration (formatted in hexadecimal), which helps understand how far the search progressed.

## Implementation Highlights
- **State Conversion Functions:**  
  Converting states from strings to integers (`_state_to_int`) and vice versa (`_int_to_state`) allows for compact and efficient state manipulation.
- **Swapping Tiles:**  
  The `_swap` function uses bitwise operations to swap the blank with an adjacent tile, facilitating quick state transitions.
- **Move Direction Mapping:**  
  The _move_to_dir function translates index shifts into human-readable directions (`'U'`, `'D'`, `'L'`, `'R'`).

## Conclusions

- **Efficiency:**
  The branch and bound approach, combined with the use of a priority queue, ensures that only promising states are explored. This reduces the number of iterations and memory overhead.

-**Resource Management:**
  By setting iteration and memory limits, the algorithm avoids potential runaway processes, providing feedback on progress and the last processed configuration.

-**Modularity:**
  The clear separation of responsibilities (puzzle management, search logic, and printing) makes the code easy to understand, test, and extend.

This project serves as a strong example of using algorithmic techniques like branch and bound to solve combinatorial puzzles, efficiently managing both search space and computational resources.

## ✒️ Authors and Codes:

- Andres Cerdas Padilla  / 20231020053
- Juan Esteban Bedoya Lautero / 20231020057







