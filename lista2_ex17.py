# 17. Fazer um algoritmo, que considerando três valores informados pelo usuário,
# mostrar se eles correspondem ou não aos comprimentos dos lados de um triângulo.
# Em caso positivo, mostrar se é um triângulo eqüilátero, isósceles ou escaleno.
# Obs:
# - O comprimento de cada lado de um triângulo é menor do que a soma dos
# comprimentos dos outros dois lados.
# - Triângulo Eqüilátero: tem os comprimentos dos três lados iguais.
# - Triângulo Isósceles – tem os comprimentos de dois lados iguais.
# - Triângulo Escaleno – tem os comprimentos de seus três lados diferentes.

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))
if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado2 + lado1):
    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Os valores informados não correspondem aos comprimentos dos lados de um triângulo.")

