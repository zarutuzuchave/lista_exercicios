# Fazer um algoritmo para ajudar a bilheteria do metrô. O operador deve informar
# o tipo do bilhete (unitário, duplo ou 10 viagens) e o valor pago pelo passageiro.
# O sistema deve mostrar, então, a quantidade de bilhetes possíveis e o troco que o
# passageiro deve receber.
# Considere a seguinte tabela de preço:
# Bilhete unitário ..................................... 1,30
# Bilhete duplo ........................................ 2,60
# Bilhete de 10 viagens ......................... 12,00

tabela_precos = print("""Bilhete unitário .............. 1,30
Bilhete duplo ................. 2,60
Bilhete de 10 viagens ........ 12,00
""")

tipo = input("Tipo (unico, duplo ou 10 viagens): ")
valor_pago = float(input("Valor pago: "))

if tipo == "unico":
    preco = 1.30
elif tipo == "duplo":
    preco = 2.60
elif tipo == "10 viagens":
    preco = 12.00
else:
    print("Tipo inválido")
    exit()

quantidade = int(valor_pago // preco)
troco = valor_pago - (quantidade * preco)

print(f"Quantidade de bilhetes: {quantidade}")
print(f"Troco: R$ {troco:.2f}")





