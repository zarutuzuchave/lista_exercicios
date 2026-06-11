# 4. Crie um programa onde o usuário vai digitando os preços dos produtos que está
# colocando no carrinho de supermercado. Armazene todos os preços em uma lista. O
# cadastro termina quando o usuário digitar um valor negativo.
# Cálculos exigidos: Calcule o valor total da compra. Se o cliente comprou mais de 10
# itens no total, ele ganha um desconto fixo de 5% sobre o valor bruto.
# Saída: Exiba a quantidade total de produtos comprados, o valor bruto, o valor do
# desconto calculado e o valor final a ser pago.


precos = []
qtd_produtos = 0
while True:
    user = float(input("Digite o PREÇO do Produto: "))
    if user <= 0:
        break
    else:
        qtd_produtos += 1
        precos.append(user)

total_preco = sum(precos)
if qtd_produtos > 10:
    desconto = total_preco * 0.05
    final = total_preco - desconto
else:
    print("Compre Mais (|)>_>(|)")


print(f"O preço otal da sua compra foi de:R${total_preco:.2f}")
print(f"O seu desconto foi de:R${desconto:.2f}")
print(f"Valor a ser pago:R${final:.2f}")
    
