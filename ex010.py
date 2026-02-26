#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comrar.
#Considere US$1,00 = R$3,27

valor = float(input("Digite o valor que vc tem na carteira: R$"))
print("Você consegue comprar US${:.2f} Dólares com a cotação atual!".format(valor/5.19))