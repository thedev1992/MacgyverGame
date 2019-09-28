import pygame
from pygame.locals import *
from Constant.constants import *
from random import randint
from Classes.Maze import *

pygame.init()


class Item(pygame.sprite.Sprite):

    def __init__(self, image, pos_x, pos_y):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y





















