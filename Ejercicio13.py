filas = int(input("Cuántas filas tendrá la matriz?: "))
cols = int(input("Cuántas columnas tendrá la matriz?: "))
matrix = []

for i in range(filas):
    matrix.append([])
    for j in range(cols):
        matrix[i].append(int(input(f"Agrega un elemento a la fila {i}: ")))

for row in matrix:
    print(row)
