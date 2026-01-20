tupla = (5, 8, 3, 3, 1, 6, 2)

num = int(input("Cuál de estos números deseas modificar por 0?: "))

lista = list(tupla)

for i in range(len(lista)):
    if lista[i] == num:
        lista[i] = 0

nueva_tupla = tuple(lista)
print(nueva_tupla)
