# 3. Dadas duas listas já preenchidas no código, uma com os nomes dos funcionários
# (funcionarios = ['Ana', 'Bruno', 'Carlos', 'Diana']) e outra com seus respectivos salários
# (salarios = [1500.0, 3200.0, 1800.0, 4500.0]).
# Cálculos exigidos: A empresa dará um aumento. Quem ganha até R$ 2000,00 receberá
# 15% de aumento. Quem ganha mais de R$ 2000,00 receberá 10%. Modifique os valores
# diretamente na lista salarios aplicando a regra matemática adequada.
# Saída: Percorra as listas atualizadas e imprima um holerite simples no formato: "Nome:
# X - Novo Salário: R$ Y".

funcionarios = ['Ana', 'Bruno', 'Carlos', 'Diana']
salarios = [1500.0, 3200.,0 1800.0, 4500.0]

for i in range(len(salarios)):
    if salarios[i] <= 2000:
        salarios[i] = salarios[i] * 1.15
    else:
        salarios[i] = salarios[i] * 1.10

print("------------- Relatorio -------------")
for i in range(len(funcionarios)):
    print(f"Nome funcionário: {funcionarios[i]} --- Novo Salário: R${salarios[i]:.2f}") 

