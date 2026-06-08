# 2. Desenvolva um programa que simule as operações básicas de um
# caixa eletrônico. O cliente começa com um saldo de R$ 0,00. O
# programa deve exibir um menu contínuo com as seguintes regras:
# • O menu deve ter 4 opções: Ver Saldo, Depositar, Sacar e Sair.
# • Crie uma função para o depósito e outra para o saque. Ambas
# devem receber o saldo atual e o valor da operação. Obs:
# devem retornar o saldo atualizado.
# • A função de saque não pode permitir que o usuário saque um
# valor maior do que ele tem na conta (deve exibir uma
# mensagem de erro).
# • Valores de depósito e saque não podem ser negativos



def depositar(saldo, valor):
    if valor > 0:
        saldo += valor
        print(f"Depósito de R$ {valor} realizado com sucesso!")
    else:
        print("Erro: o valor do depósito não pode ser negativo ou zero.")
    
    return saldo


def sacar(saldo, valor):
    if valor <= 0:
        print("Erro: o valor do saque não pode ser negativo ou zero.")
    
    elif valor > saldo:
        print("Erro: saldo insuficiente.")
    
    else:
        saldo -= valor
        print(f"Saque de R$ {valor} realizado com sucesso!")
    
    return saldo
saldo = 0.0

while True:
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Ver Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Saldo atual: R$ {saldo}")

    elif opcao == "2":
        valor = float(input("Digite o valor do depósito: R$ "))
        saldo = depositar(saldo, valor)

    elif opcao == "3":
        valor = float(input("Digite o valor do saque: R$ "))
        saldo = sacar(saldo, valor)

    elif opcao == "4":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
