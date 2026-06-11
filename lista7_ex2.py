#2.Um pequeno comércio quer analisar as movimentações do dia. Crie um programa
# que receba várias entradas financeiras e armazene-as em uma única lista chamada
# movimentações.
# Valores positivos representam vendas (receitas) e valores negativos representam
# pagamentos (despesas). Pare de registrar quando o usuário digitar 0.
# Cálculos exigidos: Percorra a lista para calcular o total arrecadado (soma dos
# positivos), o total gasto (soma dos negativos) e o saldo final do dia (receitas +
# despesas).
# Saída: Imprima um relatório financeiro simples mostrando esses três valores. Mostre
# também uma mensagem de "Lucro" se o saldo for positivo, ou "Prejuízo" se for
# negativo.
movimentacoes = []

while True:
    valores = int(input("Digite os valores ou 0 para sair: "))
    if valores == 0:
        break
    else:
        movimentacoes.append(valores)
    
total_arrecadado = 0
total_gasto = 0

for i in range(len(movimentacoes)):
    valor = movimentacoes[i]

    if valor > 0:
        total_arrecadado += valor
    elif valor < 0:
        total_gasto += valor

saldo = total_arrecadado + total_gasto

print("--------------- Relatorio ---------------")
print(f"Saldo total: ${saldo:.2f}")
print(f"Total Arrecadado ${total_arrecadado:.2f}")
print(f"Total Gasto: ${total_gasto:.2f}")
if saldo > 0:
    print("Lucro $>$")
else:
    print("Prejuízo @-@")
