"""Suponha que você foi ao supermercado e comprou 2   s. Faça um algoritmo que leia o nome e o preço dos produtos comprados e calcule o preço total da compra. Ao final, se sua compra totalizar mais de R$100,00, você terá um desconto de 20%. Deverão ser impressos os nomes dos 2 produtos comprados, seus preços e o valor total da compra com e sem o desconto obtido."""

print("---------------------------")
produto1 = input("Digite o nome do pruduto 1: ")
precoProduto1 = float(input("Digite o preço do produto 1: "))
produto2 = input("Digite o nome do pruduto 2: ")
precoProduto2 = float(input("Digite o preço do produto 2: "))
print("---------------------------")

precoTotal = precoProduto1+precoProduto2
precoDesconto = precoTotal*0.20


def mostrarPrecos():
    print(produto1, "- R$", precoProduto1)
    print(produto2, "- R$", precoProduto2)
    print("Total: R$", precoTotal)
    print("Total da compra com desconto: R$ ", precoTotal-precoDesconto)


if (precoTotal > 100):
    mostrarPrecos()
    print("Sua compra ultrapassou o valor de R$100,00, você tem direito ao desconto de 20%")
    print("---------------------------")
else:
    mostrarPrecos()
    print("---------------------------")
