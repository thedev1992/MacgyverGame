import pygame
from pygame.locals import *
from constants import *


class LevelMaze:

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


        num_line = 0

        for line in self.structure:
            num_box = 0

            for sprite in line:

                x = num_box * size_window2
                y = num_line * size_window2
                if sprite == 'm':
                    window.blit(wall, (x, y))
                elif sprite == 'g':
                    window.blit(guard, (x, y))

                num_box += 1
            num_line += 1

















