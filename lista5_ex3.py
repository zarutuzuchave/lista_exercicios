# Faça uma função que recebe um valor inteiro e verifica se o valor é
# positivo ou negativo. A função deve retornar um valor inteiro. 

def verificar_numero(valor):
    if valor >= 0:
        return 1
    else:
        return -1

numero = int(input("Digite um número inteiro: "))

if verificar_numero(numero) == 1:
    print("O número é positivo.")
else:
    print("O número é negativo.")
