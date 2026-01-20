tupla1 = (1, 2, 3, 4, 5)
tupla2 = (8, 6, 4, 2, 0)
suma = [0, 0, 0, 0, 0]

for i in range(5):
    suma[i] = tupla1[i] + tupla2[i]

suma = tuple(suma)

print(f"""
      Tupla 1:  {tupla1}
                +
      Tupla 2:  {tupla2}
                ================
      Suma:     {suma}
""")
