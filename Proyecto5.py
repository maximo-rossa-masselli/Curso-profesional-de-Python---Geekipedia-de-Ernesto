romano = input("Ingresa un número romano para "
               "convertirlo a entero: ").upper() + " "
num = 0
miles = centenas = decenas = False
ant = None

for i in range(len(romano)):
    letra = romano[i]
    if romano[i] == " ":
        sig = " "
    else:
        sig = romano[i+1]
    if letra == "M":
        if ant == "C":
            num += 900
        else:
            num += 1000
    elif letra == "D":
        if ant == "C":
            num += 400
        else:
            num += 500
    elif letra == "C":
        if ant == "X":
            num += 90
        elif sig != "M" and sig != "D":
            num += 100
    elif letra == "L":
        if ant == "X":
            num += 40
        else:
            num += 50
    elif letra == "X":
        if ant == "I":
            num += 9
        elif sig != "C" and sig != "L":
            num += 10
    elif letra == "V":
        if ant == "I":
            num += 4
        else:
            num += 5
    elif letra == "I":
        if sig != "X" and sig != "V":
            num += 1

    ant = letra

print(num)
