import pygame
import random
from Classes.classes import *
from Constant.constants import *


class Needle:

    def __init__(self, obj, level):

        self.obj = pygame.image.load(obj).convert_alpha
        self.level = level
        self.case_x, self.case_y = self.random_position()
        self.x = self.case_x * size_window2
        self.y = self.case_y * size_window2

    def random_position(self):
        count_max = 1
        count = 0
        while count < count_max:

