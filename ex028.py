#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo comuptador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import time
import random
npc = random.randint(0, 5)
print("-=-" * 20)
print("Vou pensar em um numero, tente advinhar!")
print("-=-" * 20)
njg = int(input("Digite um valor de 0 a 5: "))
print("Processando...")
time.sleep(2)
print("Você acertou, parabéns! " if npc == njg else f"Você errou, eu pensei no numero {npc} tente novamente!")