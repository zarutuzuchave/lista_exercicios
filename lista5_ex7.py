# Faça um algoritmo para ler um número até que o usuário opte por
# terminar a entrada dos dados e, mostre na tela as seguintes
# informações: a média dos números, o maior e o menor número.
soma = 0
quantidade = 0
numero = float(input("Digite um número (-1 para sair): "))
maior = numero
menor = numero

while numero != -1:

    soma += numero
    quantidade += 1

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

    numero = float(input("Digite um número (-1 para sair): "))

media = soma / quantidade

print("Média:", media)
print("Maior número:", maior)
print("Menor número:", menor)
