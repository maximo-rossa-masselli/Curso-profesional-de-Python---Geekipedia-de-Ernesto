nombres = ("Ana", "Gerardo", "María", "Carlos", "Valentina")
num = int(input("Introduce un número entero entre 0 y 4: "))

while num < 0 or num > 4:
    print("Error! Número inválido, vuelve a intentar...")
    num = int(input("Introduce un número entero entre 0 y 4: "))

print(f"El nombre es {nombres[num]}")
