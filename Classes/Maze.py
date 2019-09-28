import pygame
from pygame.locals import *
from Constant.constants import *

# create a class for a level


class Levelmaze:

    # define a constructor
    def __init__(self, file):
        self.file = file
        self.structure = 0

    # Method that generate the level from the levelGame.txt
    def generate(self):

        with open(self.file, "r") as file:
            structure_level = []

            for line in file:
                line_level = []
                # Reading every letters in file
                for sprite in line:
                    # Ignoring the last sprite to continue with the next line
                    if sprite != '\n':
                        # Reading every letters in file
                        line_level.append(sprite)
                # Adding every lines the the array
                structure_level.append(line_level)
                # Then the method save the entire structure of the level
            self.structure = structure_level

    # This method display the level into the window
    def display(self, window):
        # Load the img of the structure of the level
        wall = pygame.image.load(img_wall).convert()
        guard = pygame.image.load(img_guardian).convert()

        for num_line, line in enumerate(self.structure):

            for num_sprite, sprite in enumerate(line):

                x = num_sprite * size_case
                y = num_line * size_case
                if sprite == 'm':
                    window.blit(wall, (x, y))
                elif sprite == 'g':
                    window.blit(guard, (x, y))

    def typecase(self, pixel_x, pixel_y):
        line = self.structure[int(pixel_y/size_case)]
        return line[int(pixel_x/size_case)]                                                     







