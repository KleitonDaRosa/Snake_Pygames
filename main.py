"""
@author:Kleiton Da Rosa
State:Em desenvolvimento
Titulo : Snake_version 0.1
"""
import pygame
from pygame.locals import *

"""
*Anotaçoes pessoais
----> Precisamos Criar a tela e passar os tamanhos
      Para isso criei uma variavel WINDOWS_SIZE = (600,600) 

"""


WINDOWS_SIZE = (600 , 600)
PIXEL_SIZE  = 10

pygame.init()
#Criando a tela do jogo
screen = pygame.display.set_mode(WINDOWS_SIZE)
pygame.display.set_caption('Snake')


#Criando o elemento Cobrinha->Tipo Lista
snake_position = [(250,50),(260,50),(270,50)]
snake_surface = pygame.Surface((PIXEL_SIZE,PIXEL_SIZE))
snake_surface.fill((255,255,255))

#Snake Diretion
snake_diretion = K_LEFT

#Criando a Maçacinha
apple_surface = pygame.Surface((PIXEL_SIZE,PIXEL_SIZE))
apple_surface.fill((255,0,0))




while True:

    pygame.time.Clock().tick(15)#Tempo de movimento
    screen.fill((0,0,0,))
    #Para fechar a tela
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        elif event.type == KEYDOWN:
            if event.key in [K_UP,K_DOWN,K_LEFT,K_RIGHT]:
                snake_diretion = event.key


    #Exibindo a cobrinha na tela
    for pos in snake_position:
        screen.blit(snake_surface,pos)

    #snake_position[0] = snake_position[0][0]+10, snake_position[0][1]

    if snake_diretion == K_UP:
        snake_position[0] = (snake_position[0][0], snake_position[0][1]-10 )
    elif snake_diretion == K_DOWN:
        snake_position[0] = (snake_position[0][0], snake_position[0][1] + PIXEL_SIZE)
    elif snake_diretion == K_LEFT:
        snake_position[0] = (snake_position[0][0]-PIXEL_SIZE,snake_position[0][1])
    elif snake_diretion == K_RIGHT:
        snake_position[0] = (snake_position[0][0]+ PIXEL_SIZE, snake_position[0][1] )
   
      
    pygame.display.update()


