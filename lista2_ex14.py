# Faça um algoritmo que receba três notas, calcule e mostre a média e o conceito
# que segue a tabela abaixo:
# Média Ponderada Conceito
# 8,0 |⎯| 10,0 A
# 7,0 |⎯ 8,0 B
# 6,0 |⎯ 7,0 C
# 5,0 |⎯ 6,0 D
# 0,0 |⎯ 5,0 E

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
match media:
    case m if m >= 8 and m <= 10:
        print("Conceito A")
    case m if m >= 7 and m < 8:
        print("Conceito B")
    case m if m >= 6 and m < 7:
        print("Conceito C")
    case m if m >= 5 and m < 6:
        print("Conceito D")
    case m if m >= 0 and m < 5:
        print("Conceito E")

