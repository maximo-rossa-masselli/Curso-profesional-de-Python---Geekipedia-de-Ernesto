cant = int(input("Cuántas matrices vamos a sumar?: "))
rows = int(input("Cuántas filas tendran las matrices?: "))
cols = int(input("Cuántas columnas tendrán las matrices?: "))

matrices = []
resultante = []

# CARGADO DE LAS MATRICES
for m in range(cant):
    matrices.append([])
    print(f"Matriz {m}")
    for f in range(rows):
        matrices[m].append([])
        for c in range(cols):
            matrices[m][f].append(int(input(f"Agregue un elemento a la matriz {m} fila {f} columna {c}: ")))

# RESULTANTE CARGANDO
for f in range(rows):
    resultante.append([])
    for c in range(cols):
        resultante[f].append(0)

# SUMA DE LAS MATRICES
for m in range(cant):
    for f in range(rows):
        for c in range(cols):
            resultante[f][c] += matrices[m][f][c]

# MUESTRA DE LAS MATRICES

for m in range(cant):
    for f in range(rows):
        print(matrices[m][f])
    print(" + ")

print(" = ")
for i in range(rows):
    print(resultante[i])
