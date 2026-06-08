# 1. Faça um programa que carregue uma lista de seis elementos numéricos inteiros e
# mostre:
#   a. A quantidade de números pares;
#   b. Quais são os números pares;
#   c. A quantidade de números ímpares;
#   d. Quais são os números ímpares.

numero = [1,2,4,6,5,7]
pares = 0
numeros_pares = []
impares = 0
numeros_impar = []
for i in range(len(numero)):
    if numero[i] % 2 == 0:
        pares += 1
        numeros_pares.append(numero[i])
    else:
        impares += 1
        numeros_impar.append(numero[i])

print(f"A quantidade de números pares: {pares}")
print(f"Quais são os números pares: {numeros_pares}")
print(f"A quantidade de números ímpares: {impares}")
print(f"Quais são os números ímpares: {numeros_impar}")

   
