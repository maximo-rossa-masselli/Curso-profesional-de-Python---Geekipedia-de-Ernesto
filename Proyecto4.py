try:
    num = int(input("Ingresa un numero entero para convertirlo a romano: "))
    if num <= 0 or num > 3999:
        print("El número debe ser un entero entre 1 y 3999.\n")
    else:
        # Calculo cada dígito por separado
        miles = num // 1000
        centenas = (num - miles*1000) // 100
        decenas = (num - miles*1000 - centenas*100) // 10
        unidad = num - miles*1000 - centenas*100 - decenas*10

        # Unidad de mil en romano
        miles_romano = "M" * miles

        # Centenas en romano
        if centenas <= 3:
            centenas_romano = "C" * centenas
        elif centenas == 4:
            centenas_romano = "CD"
        elif 5 <= centenas <= 8:
            centenas_romano = "D" + "C" * (centenas - 5)
        elif centenas == 9:
            centenas_romano = "CM"

        # Decenas en romano
        if decenas <= 3:
            decenas_romano = "X" * decenas
        elif decenas == 4:
            decenas_romano = "XL"
        elif 5 <= decenas <= 8:
            decenas_romano = "L" + "X" * (decenas - 5)
        elif decenas == 9:
            decenas_romano = "XC"

        # Unidad en romano
        if unidad <= 3:
            unidad_romano = "I" * unidad
        elif unidad == 4:
            unidad_romano = "IV"
        elif 5 <= unidad <= 8:
            unidad_romano = "V" + "I" * (unidad - 5)
        elif unidad == 9:
            unidad_romano = "IX"

        print(miles_romano + centenas_romano + decenas_romano +
              unidad_romano + "\n")
except ValueError:
    print("Debes ingresar un número entero.\n")
except Exception as e:
    print("Ocurrió un error: ", e)
