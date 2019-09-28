#!/usr/bin/env python

import pygame
from pygame.locals import*
from Classes.Maze import *
from Constant.constants import*
from Classes.Mcgyver import *
from Classes.item import *
from Classes.function import *
from random import randint
import time


white = 255, 255, 255


def score(score,smallfont,screen):
    text = smallfont.render("score:" + str(score), True, white)
    screen.blit(text, [0, 0])


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text,screen):
    largeText = pygame.font.Font('freesansbold.ttf', 70)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((windows / 2), (windows / 4))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(0.05)

def main():
    # pygame initialisation
    pygame.init()

    # creation of the window instance
    screen = pygame.display.set_mode((windows, windows))

    smallfont = pygame.font.SysFont(None, 20)

    # title of the Game
    pygame.display.set_caption('Mac Gyver')

    # create a color instance and apply it at the window
    black = 0, 0, 0

    # create an instance of a level and his generation
    level = Levelmaze(LevelG)
    level.generate()

    img_mac = pygame.image.load(img_MacGyver).convert_alpha()
    # macG = MacGyver("MacGyver.png")
    wall = pygame.image.load(img_wall).convert()

    item1 = item_position("Assets/needle.png")
    item2 = item_position("Assets/ether.png")
    item3 = item_position("Assets/tube.png")

    item_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    MacG = MacGyver(0, 0)

    item_list.add(item1, item2, item3)

    all_sprites_list.add(item1, item2, item3, MacG)

    K = None

    Score = 0

    game_over = False

    while not game_over:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                K = event.key

            elif event.type == KEYUP:
                K = None
        if K == K_RIGHT and MacG.rect.x < windows - width_mac:
            if level.postion(MacG.rect.x + size_case, MacG.rect.y) == '0':
                if level.postion(MacG.rect.x + size_case, MacG.rect.y + 29) == '0':
                    MacG.moveright()

        if K == K_LEFT and MacG.rect.x > 0:
            if level.postion(MacG.rect.x - 1, MacG.rect.y) == '0':
                if level.postion(MacG.rect.x - 1, MacG.rect.y + 29) == '0':
                    MacG.moveleft()

        if K == K_DOWN and MacG.rect.y < windows - width_mac:
            if level.postion(MacG.rect.x, MacG.rect.y + size_case) == '0':
                if level.postion(MacG.rect.x + 29, MacG.rect.y + size_case) == '0':
                    MacG.movedown()

        if K == K_UP and MacG.rect.y > 0:
            if level.postion(MacG.rect.x, MacG.rect.y - 1) == '0':
                if level.postion(MacG.rect.x + 29, MacG.rect.y - 1) == '0':
                    MacG.moveup()

        if level.postion(MacG.rect.x + size_case, MacG.rect.y) == 'g' and Score == 3:
            message_display("GAME WON \n CONGRATULATION!", screen)

        if level.postion(MacG.rect.x + size_case, MacG.rect.y) == 'g' and Score < 3:
            message_display('GAME LOST', screen)

        blocks_hit_list = pygame.sprite.spritecollide(MacG, item_list, True)

        for block in blocks_hit_list:
            Score += 1

        screen.fill(black)

        all_sprites_list.draw(screen)

        level.display(screen)

        score(Score, smallfont, screen)

        pygame.display.flip()

        time.sleep(0.05)

        if event.type == pygame.QUIT:
            game_over = True


if __name__ == '__main__':
    main()




