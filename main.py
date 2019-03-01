import pygame
from pygame.locals import*

# different module importation
#from Classes.Maze impor*
from Constant.constants import*
from Classes.Mcgyver import *
# from Classes.classes_object import*
import time

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
#  macG = MacGyver("MacGyver.png")
wall = pygame.image.load(img_wall).convert()

MacG = MacGyver()


K = None


# main loop of the game
game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            K = event.key

        elif event.type == KEYUP:
            K = None
    if K == K_RIGHT:
        MacG.moveright()

    if K == K_LEFT:
        MacG.moveleft()
    if K == K_DOWN:
        MacG.movedown()
    if K == K_UP:
        MacG.moveup()

    screen.fill(black)
    screen.blit(img_mac,(MacG.x, MacG.y))

    level.display(screen)
    pygame.display.flip()
    time.sleep(0.05)

    if event.type == pygame.QUIT:
        game_over = True
