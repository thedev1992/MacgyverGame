import pygame
from pygame.locals import*
from Classes.Maze import *
from Constant.constants import*
from Classes.Mcgyver import *
from Classes.item import *
from random import randint
import time

# pygame initialisation
pygame.init()

# creation of the window instance
screen = pygame.display.set_mode((windows, windows))

smallfont = pygame.font.SysFont(None, 20)
white = 255, 255, 255

# title of the Game
pygame.display.set_caption('Mac Gyver')

# create a background instance and apply it at the window
black = 0,0,0

# refresh de the windowpygame.display.flip()

# create an instance of a level and his generation
level = Levelmaze(LevelG)
level.generate()

img_mac = pygame.image.load(img_MacGyver).convert_alpha()
# macG = MacGyver("MacGyver.png")
wall = pygame.image.load(img_wall).convert()

needle = pygame.image.load("needle.png").convert_alpha()
ether = pygame.image.load("ether.png").convert_alpha()
tube = pygame.image.load("tube.png").convert_alpha()

position_found = False
while position_found == False:

    pos_x = (randint(0, 14) * size_case)
    pos_y = (randint(0, 14) * size_case)
    if level.postion(pos_x, pos_y) == '0':
        item1 = Item(tube, pos_x, pos_y)

        position_found = True

position_found = False
while position_found == False:

    pos_x = (randint(0, 14) * size_case)
    pos_y = (randint(0, 14) * size_case)
    if level.postion(pos_x, pos_y) == '0':
        item2 = Item(needle, pos_x, pos_y)

        position_found = True

position_found = False
while position_found == False:

    pos_x = (randint(0, 14) * size_case)
    pos_y = (randint(0, 14) * size_case)
    if level.postion(pos_x, pos_y) == '0':
        item3 = Item(ether, pos_x, pos_y)

        position_found = True

item_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
MacG = MacGyver(0, 0)

item_list.add(item1, item2, item3)

all_sprites_list.add(item1, item2, item3, MacG)


K = None

def score(score):
    text = smallfont.render("score:" + str(score), True, white)
    screen.blit(text, [0, 0])

Score = 0
# main loop of the game
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
        print('game won')

    if level.postion(MacG.rect.x + size_case, MacG.rect.y) == 'g' and Score < 3:
        print('GAME lost')


    blocks_hit_list = pygame.sprite.spritecollide(MacG, item_list, True)

    for block in blocks_hit_list:
        Score += 1

    screen.fill(black)

    all_sprites_list.draw(screen)

    level.display(screen)

    score(Score)

    pygame.display.flip()

    time.sleep(0.05)

    if event.type == pygame.QUIT:
        game_over = True
