# 4. Faça um procedimento que recebe por parâmetro os valores necessários para o
# cálculo da fórmula de báskara e imprima as suas raízes, caso seja possível calcular.
def calcular_baskara(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        print("Não é possível calcular as raízes reais.")
    elif d == 0:
        raiz = -b / (2*a)
        print(f"A raiz única é: {raiz}")
    else:
        raiz1 = (-b + d **0.5) / (2*a)
        raiz2 = (-b - d **0.5) / (2*a)
        print(f"As raízes são: {raiz1} e {raiz2}")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
calcular_baskara(a, b, c)
