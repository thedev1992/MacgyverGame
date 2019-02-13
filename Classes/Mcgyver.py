import pygame
from pygame.locals import *
from Constant.constants import *



class MacGyver:
    def __init__(self, image):
        self.image = pygame.image.load(img_MacGyver).convert()
        self.case_x = 0
        self.case_y = 0
        self.speed = 1


    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed




