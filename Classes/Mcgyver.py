import pygame
from pygame.locals import *
from Constant.constants import *
from Classes.Maze import *


class MacGyver(pygame.sprite.Sprite):

    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_MacGyver).convert()
        self.rect = self.image.get_rect()
        self.speed = 10
        self.rect.x = x
        self.rect.y = y

    def moveright(self):
        self.rect.x += self.speed

    def moveleft(self):
        self.rect.x -= self.speed

    def moveup(self):
        self.rect.y -= self.speed

    def movedown(self):
        self.rect.y += self.speed





