
## FAÇA UM PROGRAMA EM PY QUE ABRA E REPRODUZA O AUDIO DE UM ARQUIVO MP3

import pygame
pygame.init()
pygame.mixer.music.load('SE_FOR_AMOR.mp3')
pygame.mixer.music.play()
pygame.event.wait()