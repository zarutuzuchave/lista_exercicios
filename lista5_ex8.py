# Faça um algoritmo que leia o nome, salário e número de filhos de
# 100 pessoas, e calcule:
# a. O salário médio das pessoas que possuam 2 filhos
# b. O salário médio das que não possuem filhos
# c. Qual a média salarial maior, entre os que têm um e dois filhos
# d. O salário médio geral

soma2 = 0
cont2 = 0
soma0 = 0
cont0 = 0
soma1 = 0
cont1 = 0
somaGeral = 0

for i in range(100):

    nome = input("Nome: ")
    salario = float(input("Salário: "))
    filhos = int(input("Número de filhos: "))

    somaGeral += salario

    if filhos == 2:
        soma2 += salario
        cont2 += 1

    elif filhos == 0:
        soma0 += salario
        cont0 += 1

    elif filhos == 1:
        soma1 += salario
        cont1 += 1


media2 = soma2 / cont2
media0 = soma0 / cont0
media1 = soma1 / cont1
mediaGeral = somaGeral / 100

print("Média de quem tem 2 filhos:", media2)
print("Média de quem não tem filhos:", media0)

if media1 > media2:
    print("A maior média é de quem tem 1 filho")
else:
    print("A maior média é de quem tem 2 filhos")

print("Média geral:", mediaGeral)
