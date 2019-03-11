import pygame
from pygame.locals import *
from Constant.constants import *

# create a class for a level

class Levelmaze:
    # define a constructor
    def __init__(self, file):
        self.file = file
        self.structure = 0

    def generate(self):

        with open(self.file, "r") as file:
            structure_level = []

            for line in file:
                line_level = []

                for sprite in line:

                    if sprite != '\n':

                        line_level.append(sprite)

                structure_level.append(line_level)
            self.structure = structure_level

    def display(self, window):

        wall = pygame.image.load(img_wall).convert()
        guard = pygame.image.load(img_guardian).convert()

        for num_line, line in enumerate(self.structure):

            for num_sprite, sprite in enumerate(line):

                x = num_sprite * size_window2
                y = num_line * size_window2
                if sprite == 'm':
                    window.blit(wall, (x, y))
                elif sprite == 'g':
                    window.blit(guard, (x, y))

    def postion(self,case_x, case_y):
        line = self.structure[int(case_y/size_window2)]
        return line[int(case_x/size_window2)]



