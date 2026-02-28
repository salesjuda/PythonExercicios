#Faça um programa que leia um ângulo ualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input("Digite o valor do ângulo: "))
radianos = math.radians(angulo)
print(f"{radianos:.2f}")
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)
print(f"O valor do seno de {angulo:.2f}º é: {seno:.2f}")
print(f"O valor do cosseno de {angulo:.2f}º é: {cosseno:.2f}")
print(f"O valor da tangente de {angulo:.2f}º é: {tangente:.2f}")