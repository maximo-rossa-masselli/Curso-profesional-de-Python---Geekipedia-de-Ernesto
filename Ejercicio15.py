texto = input("Ingrese un texto: ")
texto.lower()

diccionario = {}
for c in texto:
    valor = diccionario.setdefault(c, 0)
    diccionario[c] = valor + 1

print(diccionario)
