import random

print("Piensa un número entre 1 y 100. Y trataré de adivinarlo.")

cont_intentos = 0
respuesta = None
men = 1
may = 100
adivinado = False

while respuesta != 'correcto':
    if men > may:
        print("Mentiroso....")
        break

    cont_intentos += 1
    num = random.randint(men, may)
    print(f"\nEs {num} tu número?")
    respuesta = input("Ingresa 'mayor' , 'menor' o 'correcto': ").lower()

    if respuesta == 'correcto':
        adivinado = True
        break
    elif respuesta == 'menor':
        may = num - 1
    elif respuesta == 'mayor':
        men = num + 1
    else:
        respuesta = input(
            "Respuesta inválida. Ingresa 'mayor', 'menor' o "
            "'correcto': ").lower()
if adivinado:
    print(f"\nAdivine el número {num} en {cont_intentos} intentos")
