# 1 - Crie duas listas vazias: nomes e medias. Escreva um programa que peça ao usuário
# para digitar o nome de 5 alunos e a média final de cada um. Guarde os nomes na
# primeira lista e as médias na segunda lista.
# Cálculos exigidos: Após o cadastro, o programa deve percorrer as listas e calcular a
# média geral da turma.
# Saída: Imprima o nome de cada aluno ao lado de sua nota e, ao final, informe quantos
# alunos ficaram acima da média geral da turma

nomes = []
medias = []

for i in range(5):
    name = input(f"Digite o nome do {i+1}° aluno:  ")
    media = float(input(f"Digite a media do {i+1}° aluno: "))
    medias.append(media)
    nomes.append(name)

soma = 0 
for i in range(len(medias)):
    soma += medias[i]

media_geral = soma / len(medias)

for i in range(len(nomes)):
    print(f"Aluno:{nomes[i]}    Media: {medias[i]:.1f}")

acima_media = 0
for i in range(len(medias)):
    if medias[i] > media_geral:
        acima_media += 1

print(f"Media Geral: {media_geral} ")
print(f"Alunos Acima da Média: {acima_media}")
