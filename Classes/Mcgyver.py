import pygame
from pygame.locals import *
from Constant.constants import *
from Classes.Maze import *


class MacGyver(pygame.sprite.Sprite):
    """
        This class represents the PLayer.
        It derives from the "Sprite" class in Pygame.
        """

    def __init__(self, x, y):
        # subclassing sprite before to add it to a group
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_MacGyver).convert()
        # get the rectangular area of the Surface
        self.rect = self.image.get_rect()
        self.speed = 10
        self.rect.x = x
        self.rect.y = y
    """   
         We define different fonction of the Player which 
         hold his position on the screen
         and the speed by which it moves.          
        """
    def moveright(self):
        self.rect.x += self.speed

    def moveleft(self):
        self.rect.x -= self.speed

    def moveup(self):
        self.rect.y -= self.speed

    def movedown(self):
        self.rect.y += self.speed





