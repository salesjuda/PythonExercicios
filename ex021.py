# Faça um programa em python que abra e reproduza o audio de um arquivo MP3.

# Importa a biblioteca do pygame
import pygame
opcao = 0
cont = 0
# Iniciar o mixer do pygame
pygame.mixer.init()

# carregar o arquivo de audio
pygame.mixer.music.load('Livres Para Adorar.mp3')

# Definir o volume, pode ser opcional, o voluem vai de 0.0 até 0.1
pygame.mixer.music.set_volume(0.8)

# Reproduz o audio
pygame.mixer.music.play()

# Loop para ficar rodando um menu de opções
while cont == 0:
    opcao = int(input("Digite 1 para pausar, 2 para continuar e 0 para parar: "))
    if opcao == 1:
        pygame.mixer.music.pause()
        cont = 0
    elif opcao == 2:
        pygame.mixer.music.unpause()
        cont = 0
    elif opcao == 0:
        cont = 1
else:
    print("Você encerrou a musica: ")
          