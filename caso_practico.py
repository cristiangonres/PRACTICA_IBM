import random

#PRÁCTICA PYTHON CURSO IBM 
# Escribir un programa en Python que genere una matriz de tamaño NxN y
# la llene con números aleatorios entre 0 y 9. El programa deberá imprimir
# la matriz generada y luego calcular la suma de los elementos de cada fila y
# columna. Finalmente, deberá imprimir la suma de cada fila y columna.
# El programa deberá incluir las siguientes características:
# -Generación de la matriz: El programa deberá generar una matriz
# cuadrada de tamaño NxN, donde N es un número entero ingresado
# por el usuario.
# -Rellenar la matriz con números aleatorios: El programa deberá
# rellenar la matriz con números aleatorios entre 0 y 9.
# -Imprimir la matriz: El programa deberá imprimir la matriz generada
# en pantalla.
# -Calcular la suma de cada fila y columna: El programa deberá
# calcular la suma de los elementos de cada fila y columna y
# almacenarlas en dos listas.
# -Imprimir la suma de cada fila y columna: El programa deberá
# imprimir en pantalla la suma de cada fila y columna.
# Además, se sugiere que el programa incluya manejo de excepciones en
# caso de que el usuario ingrese un valor no válido para N, también que
# incluya comentarios para explicar el código y finalmente que se hagan los
# test unitarios necesarios para asegurar que el resultado es el esperado.

def generate_matrix(n):
    """Genera una matrix de tamaño NxN y la llena con números aleatorios entre 0 y 9."""
    matrix = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
    return matrix

def print_matrix(matrix):
    """Imprime la matrix generada en pantalla."""
    for row in matrix:
        print(row)

def calculate_sums(matrix):
    """Calcula la suma de los elementos de cada row y columna y las almacena en dos listas."""
    n = len(matrix)
    sums_row = [sum(row) for row in matrix]
    sums_col = [sum(matrix[row][col] for row in range(n)) for col in range(n)]
    return sums_row, sums_col

def print_sums(sums_row, sums_col):
    """Imprime en pantalla la suma de cada row y columna."""
    print("Suma de cada row:")
    print(sums_row)
    print("Suma de cada columna:")
    print(sums_col)

def main():
    # Función principal con control de excepciones para entrada de usuario
    try:
        n = int(input("Ingrese el tamaño de la matrix cuadrada (N): "))
        if n <= 0:
            raise ValueError("El valor de N debe ser un número entero positivo.")
        
        matrix = generate_matrix(n)
        print("matrix generada:")
        print_matrix(matrix)
        
        sums_row, sums_col = calculate_sums(matrix)
        print_sums(sums_row, sums_col)
        
    except ValueError as ve:
        print(f"Error: {ve}")
    
if __name__ == "__main__":
    main()


# Test unitarios para verificar funcionamiento:
def test_sum_row_col():
    # Caso de prueba 1
    matrix = [[1, 2], [3, 4]]
    sums_row, sums_col = calculate_sums(matrix)
    assert sums_row == [3, 7]
    assert sums_col == [4, 6]

    # Caso de prueba 2
    matrix = [[5, 5, 5], [0, 0, 0], [1, 1, 1]]
    sums_row, sums_col = calculate_sums(matrix)
    assert sums_row == [15, 0, 3]
    assert sums_col == [6, 6, 6]

    # Caso de prueba 3
    matrix = [[9]]
    sums_row, sums_col = calculate_sums(matrix)
    assert sums_row == [9]
    assert sums_col == [9]

if __name__ == "__main__":
    test_sum_row_col()
