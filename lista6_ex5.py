# 5. Dado as listas A e B de tamanho 6 e do tipo float faça um programa que,
#   utilizando um laço de repetição,e utilizando outro laço, inicialize os valores de ambas
#   as listas, some os valores posição por posição e guarde o novo valor na lista A.

a = []
b = []

for i in range(6):
    a.append(float(input("Digite um valor para A: ")))
for i in range(6):
    b.append(float(input("Digite um valor para B: ")))
for i in range(6):
    a[i] += b[i]
