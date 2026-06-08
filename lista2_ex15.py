#  Faça um algoritmo que receba três notas de um aluno, calcule e mostre a média
# aritmética e a mensagem que segue a tabela abaixo. Para alunos de exame,
# calcule e mostre a nota mínima a ser tirada no exame para que o aluno obtenha
# aprovação, considerando que a média no exame é 6,0.
# Média Ponderada Conceito
# 0,0 |⎯ 3,0 Reprovado
# 3,0 |⎯ 7,0 Exame
# 7,0 |⎯| 10,0 Aprovado
media = 0
media_minima = 0
for i in range(3):
    nota = int(input("digite a nota do aluno:"))
    media += nota

media /= 3
if media < 3:
    print("Reprovado")
    print(media)   
elif media < 7:
    media_minima = 12 - media
    print("Exame")
    print(media)   
    print(f"Minima  no exame: {media_minima} ")
else:
    print("Aprovado")
    print(media)   




