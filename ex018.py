#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, cos, sin, tan
angulo = float(input("Digite o valor do ângulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f"O valor do seno de {angulo:.2f}º é: {seno:.2f}")
print(f"O valor do cosseno de {angulo:.2f}º é: {cosseno:.2f}")
print(f"O valor da tangente de {angulo:.2f}º é: {tangente:.2f}")