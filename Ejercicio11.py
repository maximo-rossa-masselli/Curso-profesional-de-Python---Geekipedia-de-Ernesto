lista = ["A", "B", "b", "c", "E", "E", "f"]
elim = input("Introduce el elemento que deseas eliminar: ")

for i in range(len(lista) - 1, -1, -1):
    if lista[i].lower() == elim.lower():
        lista.pop(i)

print(lista)
