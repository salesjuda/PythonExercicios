#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimentoda hipotenusa
import math
cco = float(input("Digite o comprimento do cateto oposto: "))
cca = float(input("Digite o comprimento do cateto adjacente: "))

ch = math.hypot(cco, cca)

print(f"O comprimento da hipotenusa é: {ch:.2f}")
