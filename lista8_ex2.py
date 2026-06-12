# 2 - Um investidor quer registrar suas transações diárias (lucros e prejuízos) e entender o
# comportamento do seu saldo.
# Crie uma função que peça ao usuário para digitar 7 valores (números reais),
# representando o resultado financeiro de cada dia da semana. Valores positivos são
# lucros, valores negativos são prejuízos (ex: 150.50, -50.00, 200.00). Salve-os em uma
# lista.
# Crie uma função chamada analisar_carteira(lista_valores) que:
# Calcule o saldo final acumulado (soma de todos os itens).
# Calcule a porcentagem de dias que foram lucrativos (valores maiores que zero) em
# relação ao total de dias.
# Crie uma função chamada filtrar_e_ordenar(lista_valores) que:
# -Separe apenas os dias de prejuízo (valores menores que zero).
# -Ordene esses prejuízos do pior para o melhor (ou seja, em ordem crescente: o número
# mais negativo primeiro).
# Mostre o saldo final, a taxa de sucesso e a lista de prejuízos ordenados.

transacoes = []

def ler_valores():
    print("Digite o resultado financeiro de cada um dos 7 dias:")
    for i in range(7):
        number = float(input(f"Dia {i+1}: "))
        transacoes.append(number)

def analisar_carteira(lista_valores):
    saldo_final = sum(lista_valores)
    dias_lucrativos = 0
    
    for numero in lista_valores:
        if numero > 0:
            dias_lucrativos += 1
            
    taxa_sucesso = (dias_lucrativos / len(lista_valores)) * 100
    
    return saldo_final, taxa_sucesso

def filtrar_e_ordenar(lista_valores):
    dia_prejuizo = []
    for numero in lista_valores:
        if numero < 0:
            dia_prejuizo.append(numero)
            
    dia_prejuizo.sort() 
    return dia_prejuizo

ler_valores()

saldo, taxa = analisar_carteira(transacoes)
prejuizos_ordenados = filtrar_e_ordenar(transacoes)


print(f"Saldo Final Acumulado: R$ {saldo:.2f}")
print(f"Taxa de Dias Lucrativos: {taxa:.1f}%")
print(f"Prejuízos (do pior para o melhor): {prejuizos_ordenados}")




        
        

