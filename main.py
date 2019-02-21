import pygame
from pygame.locals import*

# different module importation
#from Classes.Maze impor*
from Constant.constants import*
from Classes.Mcgyver import *
# from Classes.classes_object import*

# pygame initialisation
pygame.init()

# creation of the window instance
screen = pygame.display.set_mode((windows, windows))

# title of the Game
pygame.display.set_caption('Mac Gyver')

# create a background instance and apply it at the window
black = 0,0,0

# refresh de the windowpygame.display.flip()

# create an instance of a level and his generation
level = Levelmaze(LevelG)
level.generate()

img_mac = pygame.image.load(img_MacGyver).convert_alpha()
# macG = MacGyver("MacGyver.png")
wall = pygame.image.load(img_wall).convert()


x = 0
y = 0

blue = 0,0,255

# main loop of the game
game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                x = + 5

            if event.key == K_LEFT:
                x = - 5
            if event.key == K_DOWN:
                x = + 5
            if event.key == K_UP:
                x = - 5

    screen.fill(black)
    screen.blit(img_mac,(x,y))
    # pygame.draw.rect(screen,blue,(x,y,100,100))

    level.display(screen)
    pygame.display.flip()


    if event.type == pygame.QUIT:
        game_over = True
