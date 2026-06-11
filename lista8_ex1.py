# 1 – Crie um programa que ajude um professor a analisar o desempenho de uma turma.
# O programa deve pedir ao usuário o nome e a nota de vários alunos. O programa para de
# pedir dados quando o usuário digitar "sair" no nome. Essas notas devem ser salvas em
# uma lista.
# Em seguida crie uma função chamada calcular_estatisticas(lista_notas) que recebe a
# lista de notas e retorne:
# A média aritmética da turma.
# A maior e a menor nota (sem usar as funções prontas max() e min()).
# Crie uma função chamada exibir_ranking(lista_notas) que ordene as notas de forma
# decrescente (do maior para o menor) e exiba o resultado na tela.
lista_notas = []
while True:
    nomes = str(input("Digite o nome do aluno ou sair: "))
    if nomes == "sair":
        break
    else:
        notas = float(input("Digite a nota do aluno: "))
        lista_notas.append(notas)

def calcular_estatisticas(lista_notas):
    soma = 0
    maior = lista_notas[0]
    menor = lista_notas[0]
    for nota in lista_notas:
        soma += nota
        if nota > maior:
            maior = nota
        if nota < menor:  
            menor = nota
    media = soma / len(lista_notas)
    return media, maior, menor


def exibir_ranking(lista_notas):
    notas = sorted(lista_notas, reverse=True)
    print("---------- Ranking ----------")
    posicao = 1
    for nota in notas:
        print(posicao, "º Lugar:", nota)
        posicao += 1
    
media, maior, menor = calcular_estatisticas(lista_notas)    
print("\n---------- Estatísticas ----------")
print(f"Média da turma: {media:.2f}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
exibir_ranking(lista_notas)