import pygame
from pygame.locals import*

# different module importation
from Classes.classes import*
from Constant.constants import*

# pygame initialisation
pygame.init()

# creation of the window instance
window = pygame.display.set_mode((windows, windows))

# title of the Game
pygame.display.set_caption('Mac Gyver')

# create a background instance and apply it at the window
background = pygame.image.load(img_background).convert()
window.blit(background, (0, 0))

# refresh de the window
pygame.display.flip()

# create an instance of a level and his generation
level = LevelMaze(LevelG)
level.generate()

# main loop of the game
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    window.blit(background, (0, 0))
    level.display(window)
    pygame.display.flip()
