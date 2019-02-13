import pygame
import random
from Classes.Maze import *
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
            self.case_x = random.randint(0, 14)
            self.case_y = random.randint(0, 14)

            # If the sprite is a free_space
            if self.level.structure[self.case_y][self.case_x] == '0':

                # then change it to a mark where the program gonna pop the item.
                self.level.structure[self.case_y][self.case_x] = "o1"

                # And quit the loop
                count += 1
                break
        return self.case_x, self.case_y

    # Method that display the item on the map
    def display(self, window):

        # Load the sprite
        img_needle = pygame.image.load("images/ether.png").convert_alpha()

        # Display the item on screen
        window.blit(img_needle, (self.x, self.y))


