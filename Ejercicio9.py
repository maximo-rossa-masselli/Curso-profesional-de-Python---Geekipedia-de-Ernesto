frase = input("Ingrese una frase: ")
corte = input("Con qué letra desea terminar?: ")

nueva = ""
for c in frase:
    if c.lower() == corte.lower():
        break
    if c not in("AEIOUaeiou"):
        nueva += c

print(nueva)