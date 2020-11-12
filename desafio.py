# coding: iso-8859-1 -*-

import pygame
from pygame.locals import *
from sys import exit

#inicializando o console
pygame.init()

#definindo a tela
screen = pygame.display.set_mode((720, 640))
#adicionando um nome para a tela
pygame.display.set_caption("desafio-modulo 4")

pygame.draw.rect(screen, (255,0,0), [360,320,10,10])

while True:
    for event in pygame.event.get(): #loop infinito que fica esperando  o evento que quit(clicando no X da janela)
        if event.type == QUIT:
            pygame.quit()
            exit()

        # screen.fill((120,0,255))#coloca o background na tela

        x, y = pygame.mouse.get_pos() #coloca o background na tela

        print(x, y)

    pygame.display.update()
