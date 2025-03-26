def is_valid_number(s):
    return len(s) == 1 or s[0] != '0'

def sum_string(s):
    def backtrack(start, prev1, prev2):
        if start == len(s):
            return True
        # Calculamos el siguiente número esperado
        next_sum = prev1 + prev2
        next_str = str(next_sum)
        print(f"first: {prev1}")
        print(f"second: {prev2}")
        # Verificamos si el siguiente número está presente desde la posición 'start'
        if s.startswith(next_str, start):
            return backtrack(start + len(next_str), prev2, next_sum)
        return False
    
    n = len(s)
    # Probamos todas las posibles combinaciones para los dos primeros números
    for i in range(1, n):
        for j in range(i+1, n):
            first = s[:i]
            second = s[i:j]
            # Validamos que los números no tengan ceros a la izquierda
            if not is_valid_number(first) or not is_valid_number(second):
                continue
            # Convertimos a enteros y verificamos el resto de la cadena
            if backtrack(j, int(first), int(second)):
                return True
    return False

# Ejemplo de prueba
initial_string = "1111112223"
print(sum_string(initial_string))