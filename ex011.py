#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
altura = float(input("Digite a Altura da parede: "))
largura = float(input("Digite a Largura da parede: "))
area = altura * largura
print(f"Área: {area:.2f}m²")
print(f"Vc vai precisar de {area / 2:.2f} Litros de tinta")