# coding: iso-8859-1 -*-
background_image_filename = 'foto_okinawa.jpg'
mouse_image_filename = 'foto_beach_ball.png'

import pygame
from pygame.locals import *
from sys import exit

#inicializando o console
pygame.init()

#definindo a tela
screen = pygame.display.set_mode((720, 640))
#adicionando um nome para a tela
pygame.display.set_caption("Olá, Mundo game!")

#definindo a imgem de background e converte para o mesmo formato do display
background = pygame.image.load(background_image_filename).convert()
#definindo a imagem do cursor(convert_alp´ha permite que as formas sejam desenhadas())
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()


while True:
    for event in pygame.event.get(): #loop infinito que fica esperando  o evento que quit(clicando no X da janela)
        if event.type == QUIT:
            pygame.quit()
            exit()

        screen.blit(background, (0,0))#coloca o background na tela

        x, y = pygame.mouse.get_pos() #coloca o background na tela

        #coloca a imagem como o centro do cursor do mouse
        x-= mouse_cursor.get_width() / 2
        y-= mouse_cursor.get_height() / 2

        #coloca o cursor com a imagem na tela
        screen.blit(mouse_cursor, (x, y))

        #realiza o upgrade da tela
        pygame.display.update()
