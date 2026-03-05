# Faça um programa em python que abra e reproduza o audio de um arquivo MP3.

# Importa a biblioteca do pygame
import pygame

# Iniciar o mixer do pygame
pygame.mixer.init()

# carregar o arquivo de audio
pygame.mixer.music.load('Livres Para Adorar.mp3')

# Definir o volume, pode ser opcional, o voluem vai de 0.0 até 0.1
pygame.mixer.music.set_volume(0.8)

# Reproduz o audio
pygame.mixer.music.play()

# Loop para ficar rodando um menu de opções
print("Digite 1 para pausar, 2 para continuar, 3 para reiniciar e 0 para parar: ")
while True:
    opcao = int(input())
    if opcao == 1:
        pygame.mixer.music.pause()
        print("Você Pausou a musica!")
        
    elif opcao == 2:
        pygame.mixer.music.unpause()
        print("Musica Retomada!")

    elif opcao == 3:
        pygame.mixer.music.play()
        print("Você Reiniciou a musica!")
       
    elif opcao == 0:
       pygame.mixer.music.stop()
       print("Você Encerrou a Musica!")
       break 

    else:
        print("Opção invalida!")

    
          