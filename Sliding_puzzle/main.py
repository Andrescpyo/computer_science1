from controllers.puzzle import PuzzleController

if __name__ == "__main__":
    PUZZLE = "123457689ABCDFE0"
    solution = PuzzleController.solve_puzzle(PUZZLE)
    if solution is not None:
        if isinstance(solution, str):
            print(f"Solución encontrada")  # Mostrar mensajes como "El puzzle no tiene solución." o "Búsqueda terminada por límite..."
        else:
            print(f"Solución no encontrada: {solution}")
    else:
        print("No se encontró solución.")