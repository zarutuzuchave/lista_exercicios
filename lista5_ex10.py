# Suponha que serão digitados 100 números inteiros via teclado, faça
# um algoritmo para:
# a. Somar os números positivos
# b. Contar os números negativos.
# c. A média dos números negativos e a média dos números
# positivos.
# d. A diferença entre o total de números positivos e negativos.

somaPositivos = 0
contPositivos = 0
somaNegativos = 0
contNegativos = 0

for i in range(100):
    numero = int(input("Digite um número: "))
    if numero >= 0:
        somaPositivos += numero
        contPositivos += 1
    else:
        somaNegativos += numero
        contNegativos += 1

mediaPositivos = somaPositivos / contPositivos
mediaNegativos = somaNegativos / contNegativos
diferenca = contPositivos - contNegativos
print("Soma dos positivos:", somaPositivos)
print("Quantidade de negativos:", contNegativos)
print("Média dos positivos:", mediaPositivos)
print("Média dos negativos:", mediaNegativos)
print("Diferença entre positivos e negativos:", diferenca)
