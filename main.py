import pygame
from pygame.locals import*

# different module importation
#from Classes.Maze impor*
from Constant.constants import*
from Classes.Mcgyver import *
from Classes.item import *
import time

# pygame initialisation
pygame.init()

# creation of the window instance
screen = pygame.display.set_mode((windows, windows))

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


block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
MacG = MacGyver(0,0)
item1 = Item(tube, 100, 100)
item2 = Item(needle,200,150)
item3 = Item(ether,350, 150)

block_list.add(item1, item2, item3, MacG)
all_sprites_list.add(item1, item2, item3, MacG)


K = None


# main loop of the game
game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            K = event.key

        elif event.type == KEYUP:
            K = None
    if K == K_RIGHT and MacG.rect.x < windows - width_mac:
        #if level.postion(MacG.rect.x + size_case, MacG.rect.y) == '0':
            #if level.postion(MacG.rect.x + size_case, MacG.rect.y + 29) == '0':
                MacG.moveright()

    if K == K_LEFT and MacG.rect.x > 0:
        #if level.postion(MacG.rect.x - 1, MacG.rect.y) == '0':
            #if level.postion(MacG.rect.x - 1, MacG.rect.y + 29) == '0':
                MacG.moveleft()

    if K == K_DOWN and MacG.rect.y < windows - width_mac:
        #if level.postion(MacG.rect.x, MacG.rect.y + size_case) == '0':
            #if level.postion(MacG.rect.x + 29, MacG.rect.y + size_case) == '0':
                MacG.movedown()

    if K == K_UP and MacG.rect.y > 0:
        #if level.postion(MacG.rect.x, MacG.rect.y - 1) == '0':
            #if level.postion(MacG.rect.x + 29, MacG.rect.y - 1) == '0':
                MacG.moveup()








    screen.fill(black)
    #screen.blit(img_mac, (MacG.x, MacG.y))
    all_sprites_list.draw(screen)



    #screen.blit(needle, (200, 150))

    #screen.blit(ether, (350, 150))

    #level.display(screen)
    pygame.display.flip()
    time.sleep(0.05)

    if event.type == pygame.QUIT:
        game_over = True
