# Faça um programa em python que abra e reproduzao audio de um arquivo MP3.

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

# Manter o programa rodando enquanto a musica toca
input("Pressione Enter para Parar...")