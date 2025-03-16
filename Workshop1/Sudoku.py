import math

class Sudoku:
    def __init__(self, tamano):
        if not math.isqrt(tamano)**2 == tamano :
            raise ValueError("El tamaño del Sudoku debe ser un cuadrado perfecto (4, 9, 16, etc.)")
        self.tamano = tamano
        self.tablero = [[0 for _ in range(tamano)] for _ in range(tamano)]

    def es_valido(self, fila, columna, numero):
        # Verifica la fila
        for x in range(self.tamano):
            if self.tablero[fila][x] == numero:
                return False

        # Verifica la columna
        for x in range(self.tamano):
            if self.tablero[x][columna] == numero:
                return False

        # Verifica la subcuadrícula
        tamano_subcuadricula = int(math.sqrt(self.tamano))
        subcuadricula_fila = fila // tamano_subcuadricula * tamano_subcuadricula
        subcuadricula_columna = columna // tamano_subcuadricula * tamano_subcuadricula

        for i in range(tamano_subcuadricula):
            for j in range(tamano_subcuadricula):
                if self.tablero[subcuadricula_fila + i][subcuadricula_columna + j] == numero:
                    return False

        return True

    def resolver(self, soluciones):
        for fila in range(self.tamano):
            for columna in range(self.tamano):
                if self.tablero[fila][columna] == 0:
                    for numero in range(1, self.tamano + 1):
                        if self.es_valido(fila, columna, numero):
                            self.tablero[fila][columna] = numero

                            self.resolver(soluciones)  # Continúa buscando

                            self.tablero[fila][columna] = 0  # Reestablece para probar otras opciones
                    return  # No se encontró un número válido en esta rama
        # Si llegamos aquí, es una solución válida
        soluciones.append([fila[:] for fila in self.tablero])

    def imprimir(self, tablero = None):
        if tablero is None:
            tablero = self.tablero
        for fila in tablero:
            print(fila)

# Ejemplo de Sudoku 4x4
num = 4
sudoku = Sudoku(num) # Crea un Sudoku 4x4 vacío

# Inicializa el tablero con valores específicos
sudoku.tablero = [
    [1, 0, 0, 0],
    [0, 0, 0, 4],
    [0, 3, 0, 0],
    [0, 0, 0, 0]
]

soluciones = []
sudoku.resolver(soluciones)

if soluciones:
    print(f"Se encontraron {len(soluciones)} soluciones:")
    for i, solucion in enumerate(soluciones):
        print(f"\nSolución {i + 1}:")
        Sudoku(num).imprimir(solucion) #creamos una instancia temporal para imprimir, y asi no modificar el tablero original.
else:
    print("No se encontraron soluciones")