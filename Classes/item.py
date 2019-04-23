import pygame
from pygame.locals import *
from Constant.constants import *


class Item(pygame.sprite.Sprite):

    def __init__(self, image, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
































"""
pygame.init()
screen = pygame.display.set_mode((windows, windows))

player = pygame.sprite.Sprite()
player.image = pygame.image.load(img_MacGyver).convert_alpha()
player.rect = player.image.get_rect()

sprite_needle = pygame.sprite.Sprite()
sprite_needle.image = pygame.image.load("needle.png").convert_alpha()
sprite_needle.rect = player.image.get_rect()
sprite_needle.rect.y = 200
sprite_needle.rect.x = 150

group_object = pygame.sprite.Group()
group_object.add(sprite_needle)


sprite_ether = pygame.sprite.Sprite()
sprite_ether.image = pygame.image.load("ether.png").convert_alpha()
sprite_ether.rect = player.image.get_rect()
sprite_ether.rect.y = 350
sprite_ether.rect.x = 150

group_object = pygame.sprite.Group()
group_object.add(sprite_ether)


sprite_tube = pygame.sprite.Sprite()
sprite_tube.image = pygame.image.load("tube.png").convert_alpha()
sprite_tube.rect = player.image.get_rect()
sprite_tube.rect.y = 0
sprite_tube.rect.x = 200

group_object = pygame.sprite.Group()
group_object.add(sprite_tube)
"""




















