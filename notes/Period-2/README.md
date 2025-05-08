# Ciencias de la computación I

A continuación se encuentran los temas de segundo corte.

- **[Notación -fija](#Notación--fija)** 
    - [Notación infija](#notación-infija)
    - [Notación posfija](#notación-posfija)
    - [Conversión de infija a posfija](#conversión-de-infija-a-posfija)
    - [Notación prefija](#notación-prefija)

## Notación -fija
En matemáticas y ciencias de la computación, las notaciones infija, posfija y prefija son formas de escribir expresiones aritméticas. Cada una tiene reglas distintas sobre el orden de los operandos y los operadores, lo cual influye en cómo se evalúan y procesan las expresiones, especialmente en estructuras como árboles de expresión, compiladores o calculadoras.

### Notación infija
Es la notación más común y la que usamos habitualmente en matemáticas. El operador se coloca entre los operandos. Se requiere el uso de paréntesis o reglas de precedencia para determinar el orden de evaluación.  

| Operación                            | Símbolos/Funciones        |
|--------------------------------------|---------------------------|
| Paréntesis                           | `()`                      |
| Potenciación                         | `**`                      |
| Negación y signo                     | `-`, `+` (unarios)        |
| Multiplicación, división, módulo     | `*`, `/`, `//`, `%`       |
| Suma y resta                         | `+`, `-`                  |
| Comparaciones                        | `==`, `!=`, `<`, `>`, ... |
| Lógicos AND                          | `and`                     |
| Lógicos OR                           | `or`                      |


**Ejemplo:** `3 + 4 * 2`  
**Evaluación:** Multiplicación antes que suma → `3 + (4 * 2) = 11`

### Notación posfija
También conocida como *notación postfija* o *notación polaca inversa*. En esta notación, el operador se coloca después de los operandos. No requiere paréntesis, ya que el orden de evaluación está definido por la posición de los elementos. Muy utilizada en evaluadores de expresiones como las pilas.  
**Ejemplo:** `3 4 2 * +`  
**Evaluación:** Multiplica `4 * 2 = 8`, luego suma `3 + 8 = 11`

### Notación prefija
También conocida como *notación polaca*. Aquí, el operador se coloca antes de los operandos. Al igual que la posfija, no necesita paréntesis y también se evalúa fácilmente usando estructuras como pilas o árboles de expresión.  
**Ejemplo:** `+ 3 * 4 2`  
**Evaluación:** Multiplica `4 * 2 = 8`, luego suma `3 + 8 = 11`

A continuación, una imagen con las tres notaciones:


![notacion-fija](images/notacion-fija.jpg)

### Conversión de infija a posfija
A continuación se presenta un algoritmo en pseudocódigo que convierte una expresión en notación infija a notación posfija. Utiliza una pila para manejar la jerarquía de operadores y los paréntesis:

```plaintext
PROCEDIMIENTO Convertir_Infija_a_Postfija(exp_infija)

 DEFINIR pila

 INICIAR pila como una pila vacía

 DEFINIR exp_postfija como una cadena vacía

 PARA cada símbolo en exp_infija HACER

  SI el símbolo es un operando (número o variable)
   Añadir el símbolo a exp_postfija

  SI no
   SI el símbolo es un paréntesis izquierdo "("
    Insertar el símbolo en la pila

   SI no
    SI el símbolo es un paréntesis derecho ")"
     MIENTRAS la pila no esté vacía Y el tope de la pila no sea "("
      Añadir el tope de la pila a exp_postfija
      Sacar el tope de la pila
     FIN MIENTRAS

     Sacar el tope de la pila (que debe ser "(")

    SI no
     SI el símbolo es un operador
      MIENTRAS la pila no esté vacía Y el operador actual tiene menor o igual precedencia que el operador en el tope de la pila
       Añadir el tope de la pila a exp_postfija
       Sacar el tope de la pila
      FIN MIENTRAS

      Insertar el símbolo en la pila
     FIN SI
    FIN SI
   FIN SI
  FIN SI

 FIN PARA

 MIENTRAS la pila no esté vacía
  Añadir el tope de la pila a exp_postfija
  Sacar el tope de la pila
 FIN MIENTRAS

 RETORNAR exp_postfija

FIN PROCEDIMIENTO
```
