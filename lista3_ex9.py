# 9. Dado um inteiro positivo n, determinar o fatorial de n, que denotamos por n!.
n = int(input("Digite um número inteiro positivo: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
print(f"O fatorial de {n} é: {fatorial}")
    
