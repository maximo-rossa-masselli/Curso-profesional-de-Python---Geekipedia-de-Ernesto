cant = int(input("Cuántos elementos contendrá la lista?: "))
lista = []
for i in range(cant):
    num = int(input("Introduce un entero: "))
    lista.append(num)
print("Lista :", lista)
print("Suma: ", sum(lista))