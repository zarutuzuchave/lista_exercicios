#  Faça um algoritmo que leia o ano de nascimento de uma pessoa e imprima a
# idade dela. Assuma que a pessoa já tenha feito aniversário esse ano. 
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f"Sua idade é:{idade} ")
