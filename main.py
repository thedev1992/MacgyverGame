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
# macG = MacGyver("MacGyver.png")
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
    if K == K_RIGHT and MacG.x < windows - width_mac:
        # si y a un obstacle mac ne passe pas
        # size window2 = blockzise

            if level.postion(MacG.x + size_case, MacG.y) == '0':
                if level.postion(MacG.x + size_case, MacG.y + 29) == '0':
                    MacG.moveright()

    if K == K_LEFT and MacG.x > 0:
        if level.postion(MacG.x - size_case, MacG.y - 29) == '0':
            MacG.moveleft()
    if K == K_DOWN and MacG.y < windows - width_mac:
        if level.postion(MacG.x, MacG.y + size_case) == '0':
            MacG.movedown()
    if K == K_UP and MacG.y > 0:
            if level.postion(MacG.x, MacG.y - size_case + 29) == '0':
                MacG.moveup()

    screen.fill(black)
    screen.blit(img_mac, (MacG.x, MacG.y))

    level.display(screen)
    pygame.display.flip()
    time.sleep(0.05)

    if event.type == pygame.QUIT:
        game_over = True
