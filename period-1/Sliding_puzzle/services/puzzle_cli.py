
class PrinterService:
    """Service responsible for printing solver progress and output to the console."""

    def print_initial(self, state: str, target: str):
        """Prints the initial state and goal of the puzzle."""
        print("=== Inicio de ejecución ===")
        print(f"Estado inicial: {state}")
        print(f"Objetivo: {target}\n")

    def print_progress(self, iteration, queue_size, visited_count, mem_usage):
        """Prints the progress of the solving process."""
        print(f"\nIteración: {iteration:,} | Cola: {queue_size:,} | Visitados: {visited_count:,}")
        print(f"Memoria usada: ~{mem_usage // (1024*1024)} MB")

    def print_no_solution(self):
        """Prints a message indicating that no solution exists."""
        print("\nNo existe solución (puzzle inválido o no resoluble)")

    def print_limit_reached(self, iterations):
        """Prints a message when the iteration limit has been reached."""
        print(f"\nLímite de {iterations:,} iteraciones alcanzado")

    def print_memory_limit(self, limit):
        """Prints a message when the memory limit has been reached."""
        print(f"\nLímite de memoria ({limit//(1024*1024)} MB) alcanzado")

    def print_final_state(self, state: str):
        """Prints the last state reached."""
        print(f"\nSolucionado hasta: {state}")

    def print_iteration(self, iteration: int, state: str, path: list, cost: int, visited: int, heap):
        """Prints the details of a specific iteration."""
        print(f"\n=== Iteración {iteration} ===")
        print(f"Estado actual: {state}")
        print(f"Camino: {'→'.join(path) if path else 'Inicio'}")
        print(f"Costo: {cost} | Visitados: {visited}")
        self._print_heap(heap)

    def _print_heap(self, heap):
        """Prints the top elements of the priority queue."""
        print("\n[Cola] Mejor costo:", heap[0][0] if heap else 'N/A')
        print("Elementos en cola:")
        for i, (cost, state, _, p) in enumerate(heap[:3]):
            print(f"{i+1}. Costo {cost} | Movs {len(p)} → {state[:4]}...")
        if len(heap) > 3:
            print(f"... {len(heap)-3} nodos más ...")

    def print_generated_move(self, move: str, state: str):
        """Prints the newly generated move."""
        print(f" + {move}: Nuevo estado {state[:4]}...")

    def print_pruned_move(self, move: str):
        """Prints a pruned move that was already visited."""
        print(f" - {move}: Estado ya visitado (poda)")

    def print_solution(self, path, iterations):
        """Prints the final solution and number of iterations."""
        print(f"\n¡Solución en {iterations:,} iteraciones!")
        print(f"Movimientos: {len(path)}\nSecuencia: {' '.join(path)}")

    def print_already_solved(self):
        """Prints a message when the puzzle is already solved."""
        print("¡El puzzle ya está resuelto!")

    def print_iteration_limit_reached(self, max_iterations: int):
        """Prints a detailed message when the iteration limit is reached."""
        print(f"\nLímite de {max_iterations} iteraciones alcanzado")
        print("Posibles causas:")
        print("- El puzzle es demasiado complejo")
        print("- No tiene solución")
        print("- Aumenta el límite de iteraciones si es necesario")

    def print_separator(self):
        """Prints a visual separator line."""
        print("\n" + "=" * 50)
