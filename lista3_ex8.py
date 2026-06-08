# 8. Dados n e uma sequência de n números inteiros positivos, determinar a soma dos
# números pares, dos ímpares e as respectivas quantidades de cada um dos
# subconjuntos.

n = int(input("Digite o número na sequência: "))
soma_pares = 0
soma_impar = 0
qtd_pares = 0
qtd_impar = 0
for i in range(n):
    numero = int(input(f"Digite o número {i + 1}: "))
    if numero % 2 == 0:
        soma_pares += numero
        qtd_pares += 1
    else:
        soma_impar += numero
        qtd_impar += 1
print(f"Soma dos números pares: {soma_pares}")
print(f"Quantidade de números pares: {qtd_pares}")
print(f"Soma dos números ímpares: {soma_impar}")
print(f"Quantidade de números ímpares: {qtd_impar}")
