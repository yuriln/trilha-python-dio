numeros = [1, 2, 3, 4, 11, 14]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

        # print(pares)

pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)

quadrado = [numero ** 2 for numero in numeros]
# print(quadrado)