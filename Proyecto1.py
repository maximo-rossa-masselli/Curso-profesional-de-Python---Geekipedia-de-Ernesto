import random

print("""Bienvenido a 'Adivina el número secreto'.
He seleccionado un número entre 1 y 100. Adivina cual es!""")

secreto = random.randint(1, 100)
CANTIDAD_INTENTOS = 10
contador_intentos = 1

while contador_intentos <= CANTIDAD_INTENTOS:
    print(f"\nIntento {contador_intentos}/{CANTIDAD_INTENTOS}")
    num = input("Ingresa tu adivinanza: ")
    if num.isdigit():
        num = int(num)
        if num == secreto:
            print(f"Felicidades, adivinaste el numero secreto: {secreto}")
            break
        elif secreto > num:
            print("El numero es mayor.")
        elif secreto < num:
            print("El numero es menor.")
    else:
        print("Debes ingresar un numero entero.")
    contador_intentos += 1

if contador_intentos > 10:
    print(f"\nNo adivinaste el número. Era ({secreto}). Suerte la próxima!")
