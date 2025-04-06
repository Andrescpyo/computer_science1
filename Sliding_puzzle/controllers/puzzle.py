import heapq

class PuzzleController:

    @staticmethod
    def solve_puzzle(puzle: str) -> str | None:
        """
        Resuelve un puzzle numérico deslizable representado por una cadena.

        Args:
            puzle (str): Cadena de texto representando el estado inicial del puzzle.
                           Ejemplo: "123456789ABCDFE0" para un puzzle 4x4.
                           Los números del 1 al 9 se representan directamente,
                           A=10, B=11, C=12, D=13, E=14, F=15. '0' representa el espacio vacío.

        Returns:
            str | None: Una cadena de movimientos (U, D, L, R) para resolver el puzzle,
                          o None si no se encuentra una solución.
        """
        n = int(len(puzle)**0.5)  # Determinar la dimensión del puzzle (asumiendo cuadrado)
        if n * n != len(puzle):
            raise ValueError("La cadena del puzzle no representa un tablero cuadrado.")

        initial_state = PuzzleController._string_to_tuple(puzle, n)
        target_state_str = "".join(str(i + 1) if i < 9 else chr(ord('A') + i - 9) for i in range(n * n - 1)) + '0'
        target_state = PuzzleController._string_to_tuple(target_state_str, n)

        if not PuzzleController._is_solvable(initial_state, n):
            return "El puzzle no tiene solución."

        priority_queue = [(PuzzleController._manhattan_distance(initial_state, target_state, n), 0, initial_state, "")]
        visited = {initial_state}
        max_iterations = 100000
        iterations = 0

        while priority_queue and iterations < max_iterations:
            priority, moves, current_state, path = heapq.heappop(priority_queue)
            iterations += 1

            if iterations % 1000 == 0:
                print(f"Iteración: {iterations}, Visitados: {len(visited)}, Cola: {len(priority_queue)}, Mejor costo: {priority}")

            if current_state == target_state:
                return path

            empty_row, empty_col = PuzzleController._find_empty(current_state)

            for dr, dc, move in [(0, 1, "R"), (0, -1, "L"), (1, 0, "D"), (-1, 0, "U")]:
                new_row, new_col = empty_row + dr, empty_col + dc

                if 0 <= new_row < n and 0 <= new_col < n:
                    new_state = PuzzleController._move(current_state, empty_row, empty_col, new_row, new_col)
                    if new_state not in visited:
                        visited.add(new_state)
                        new_priority = moves + 1 + PuzzleController._manhattan_distance(new_state, target_state, n)
                        heapq.heappush(priority_queue, (new_priority, moves + 1, new_state, path + move))

        if not priority_queue and iterations == max_iterations:
            return "Búsqueda terminada por límite de iteraciones."

        return None

    @staticmethod
    def _string_to_tuple(puzle: str, n: int) -> tuple[tuple[str, ...], ...]:
        board = [tuple(puzle[i * n:(i + 1) * n]) for i in range(n)]
        return tuple(board)

    @staticmethod
    def _tuple_to_string(board: tuple[tuple[str, ...], ...]) -> str:
        return "".join("".join(row) for row in board)

    @staticmethod
    def _find_empty(board: tuple[tuple[str, ...], ...]) -> tuple[int, int]:
        n = len(board)
        for r in range(n):
            for c in range(n):
                if board[r][c] == '0':
                    return r, c
        return -1, -1

    @staticmethod
    def _move(board: tuple[tuple[str, ...], ...], r1: int, c1: int, r2: int, c2: int) -> tuple[tuple[str, ...], ...]:
        n = len(board)
        new_board_list = [list(row) for row in board]
        new_board_list[r1][c1], new_board_list[r2][c2] = new_board_list[r2][c2], new_board_list[r1][c1]
        return tuple(tuple(row) for row in new_board_list)

    @staticmethod
    def _manhattan_distance(board: tuple[tuple[str, ...], ...], target: tuple[tuple[str, ...], ...], n: int) -> int:
        distance = 0
        target_positions = {}
        for r in range(n):
            for c in range(n):
                target_positions[target[r][c]] = (r, c)

        for r in range(n):
            for c in range(n):
                piece = board[r][c]
                if piece != '0':
                    target_r, target_c = target_positions[piece]
                    distance += abs(r - target_r) + abs(c - target_c)
        return distance

    @staticmethod
    def _is_solvable(initial_state: tuple[tuple[str, ...], ...], n: int) -> bool:
        puzle_flat = [int(x, 16) if x.isdigit() or x in 'ABCDEF' else 0 for row in initial_state for x in row]
        inversions = 0
        empty_row = -1
        for i in range(len(puzle_flat)):
            if puzle_flat[i] == 0:
                empty_row = i // n + 1
                continue
            for j in range(i + 1, len(puzle_flat)):
                val_i = puzle_flat[i]
                val_j = puzle_flat[j]
                if val_j != 0 and val_i > val_j:
                    inversions += 1

        if n % 2 == 1:  # Tablero impar
            return inversions % 2 == 0
        else:  # Tablero par
            return (inversions + empty_row) % 2 == 1