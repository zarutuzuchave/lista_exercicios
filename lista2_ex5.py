# Faça um algoritmo que leia 5 números e imprima quantos números maiores que
# 100 foram digitados
contador = 0
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    if num > 100:
        contador += 1
print(f"Quantidade de números maiores que 100: {contador}")
