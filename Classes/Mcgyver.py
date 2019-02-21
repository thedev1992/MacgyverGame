import pygame
from pygame.locals import *
from Constant.constants import *
from Classes.Maze import *



class MacGyver:
    def __init__(self):
        self.image = pygame.image.load(img_MacGyver).convert()
        self.x = 0
        self.y = 0
        self.speed = 10


    def moveright(self):
        self.x =+ self.speed


    def moveleft(self):
        self.x = - 1 #self.speed

    def moveup(self):
        self.y = - 1 #self.speed

    def movedown(self):
        self.y =+ 1 #self.speed


