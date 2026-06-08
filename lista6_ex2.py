# 2. Faça um programa que carregue uma lista com oito números inteiros e mostre:
#   a. Os números múltiplos de dois;
#   b. Os números múltiplos de três;

numeros = [2,4,6,3,5,8,9,10]

multiplo_de_dois = []
multiplo_de_tres = []

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        multiplo_de_dois.append(numeros[i])

    if numeros[i] % 3 == 0:
        multiplo_de_tres.append(numeros[i])

print(f"Os números múltiplos de dois: {multiplo_de_dois}")
print(f"Os números múltiplos de três: {multiplo_de_tres}")
