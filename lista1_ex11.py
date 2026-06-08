# Elabore um algoritmo para fazer a conversão de graus fahrenheit (º F) para
# graus celsius (º C). A fórmula para conversão é: c= 5/9 * (f-32)
fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = 5 / 9 * (fahrenheit - 32)
print(f"A temperatura em Celsius é:{celsius}")
