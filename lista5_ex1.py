# 1. Crie um programa que exiba um menu interativo para o usuário com
# opções de conversão de medidas.
# O programa deve rodar continuamente até que o usuário escolha a
# opção de sair.
# O menu deve ter 3 opções: Converter Celsius para Fahrenheit,
# Converter Metros para Centímetros e Sair.
# Crie uma função específica para cada cálculo de conversão.
# Se o usuário digitar uma opção que não existe, o programa deve
# avisar que a opção é inválida e mostrar o menu novamente
# Programa de Conversão de Medidas

def converter_temperatura(celsius):
    return (celsius * 9/5) + 32
def converter_comprimento(metros):
    return metros * 100
while True:
    print("\n=== MENU DE CONVERSÃO ===")
    print("1 - Converter Celsius para Fahrenheit")
    print("2 - Converter Metros para Centímetros")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = converter_temperatura(celsius)
        print(f"{celsius}°C equivalem a {fahrenheit}°F")
    elif opcao == "2":
        metros = float(input("Digite o valor em metros: "))
        centimetros = converter_comprimento(metros)
        print(f"{metros} metros equivalem a {centimetros} centímetros")
    elif opcao == "3":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")
