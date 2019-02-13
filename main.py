import pygame
from pygame.locals import*

# different module importation
from Classes.Maze import*
from Constant.constants import*
#from Classes.classes_object import*

#pygame initialisation
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
level = Levelmaze(LevelG)
level.generate()

mac = pygame.image.load(img_MacGyver).convert()

# creation of the instance of the items
#needle = Needle('aiguille.png', level)
#plastic_tube = PlasticTube('tube_plastique.png', level)
#syringe = Syringe('syringe.png', level)


# main loop of the game
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    window.blit(background, (0, 0))
    #window.blit()
    level.display(window)
    pygame.display.flip()
