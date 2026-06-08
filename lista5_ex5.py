# Faça uma função que receba 3 valores inteiros por parâmetro e
# imprima-os ordenados em ordem crescente. 

def ordenar(a, b, c):
    if a > b:
        a, b = b, a

    if a > c:
        a, c = c, a

    if b > c:
        b, c = c, b

    print(a, b, c)

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))

ordenar(n1, n2, n3)
