# 5. Uma empresa fez uma pesquisa de satisfação onde as notas possíveis eram apenas 1
# (Ruim), 2 (Bom) e 3 (Excelente). Crie uma lista longa simulando as respostas de 20
# clientes (ex: votos = [1, 2, 3, 2, 2, 1, 3, ...]).
# Cálculos exigidos: Crie uma lógica para contar quantas vezes cada nota aparece na
# lista. Em seguida, calcule o percentual que cada categoria representa em relação ao total
# de 20 votos.
# Saída: Imprima um relatório gerencial informando a quantidade absoluta de votos e a
# porcentagem para "Ruim", "Bom" e "Excelente". Indique também qual foi a avaliação
# vencedora (a que teve mais votos).
votos = [1, 2, 3, 2, 2, 2, 3, 3, 2, 1, 2, 3, 3, 2, 3, 1, 1, 1, 3, 4,]
ruim = 0
bom = 0
excelente = 0 
for i in range(len(votos)):
    if votos[i] == 1:
        ruim += 1
    elif votos[i] == 2:
        bom += 1
    else:
        excelente += 1
ruim *= 5
bom *= 5
excelente *= 5

print("--------------- Relatório ---------------")
print(f"Porcentagem de votos Ruim:{ruim}%")
print(f"Porcentagem de votos Bom:{bom}%")
print(f"Porcentagem de votos Excelente:{excelente}%")
if ruim > bom and excelente:
    print("As avaliações ruins ganharam.")
elif bom > ruim and excelente:
    print("As avaliações boas ganharam.")
elif excelente > ruim and bom:
    print("As avaliações Excelentes ganharam.")
else:
    print("Todos perderam")
