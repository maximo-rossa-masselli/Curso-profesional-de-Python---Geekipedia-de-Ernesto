frase = input("Introduce una frase: ")
borrada = input("Introduce la palabra a borrar: ")

inicio = frase.find(borrada)
fin = inicio + len(borrada)
print(frase[:inicio] + frase[fin:])