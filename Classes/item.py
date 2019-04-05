import pygame
import random
from Classes.Maze import *
from Constant.constants import *


class Needle:
    def __init__(self):

        self.needle = pygame.image.load("needle.png").convert_alpha()


class Ether:
    def __init__(self):
        self.ether = pygame.image.load("ether.png").convert_alpha()


class Tube:
    def __init__(self):
        self.tube = pygame.image.load("tube.png").convert_alpha()


