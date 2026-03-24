#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo comuptador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
npc = random.randint(0, 5)
njg = int(input("Digite um valor de 0 a 5:"))
print("Você acertou, parabéns! " if npc == njg else "Você errou, tente novamente!")