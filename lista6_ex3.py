# 3. Uma escola deseja saber se existem alunos cursando, simultaneamente, as disciplinas
# Lógica e Linguagem de Programação. Coloque os números das matrículas dos alunos
# que cursam Lógica em uma lista, no máximo 10 alunos. Coloque os números das
# matrículas dos alunos que cursam Linguagem de Programação em outra lista, no
# máximo 8 alunos. Mostre o número de matrícula que aparece nas duas listas.

log = [1,2,3,4,5,6,7,8,9,10]
prog = [1,2,3,15,13,12,11,8]
ambas = []
for alunos in log:
    if alunos in prog:
        ambas.append(alunos)
print(ambas)
