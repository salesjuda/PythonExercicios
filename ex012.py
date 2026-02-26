#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input("Digite o preço unitário do produto: "))
print(f"O preço do produto com desconto é: {preco-(preco*(5/100)):.2f}")