import pygame
from pygame.locals import *
from Constant.constants import *
from random import randint
from Classes.Maze import *

needle = pygame.image.load("Assets/needle.png").convert_alpha()
ether = pygame.image.load("Assets/ether.png").convert_alpha()
tube = pygame.image.load("Assets/tube.png").convert_alpha()


class Item(pygame.sprite.Sprite):

    def __init__(self, image, pos_x, pos_y):

        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y





















