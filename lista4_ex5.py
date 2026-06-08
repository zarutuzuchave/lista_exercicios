# 5. Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito
# quando ele é igual a soma dos seus divisores excetuando ele próprio. (Ex: 6 é perfeito,6 = 1 + 2 + 3, que são seus divisores).
# A função deve retornar o valor inteiro 1 para verdadeiro e 0 caso contrário.

n = int(input("Digite um número: "))
soma = 0

for i in range(1, n):
    if n % i == 0:
        soma += i

if soma == n:
    print("Número perfeito")
else:
    print("Não é um número perfeito")
