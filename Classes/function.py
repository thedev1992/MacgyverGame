from Constant.constants import *
from random import randint
from Classes.Maze import *
from Classes.item import *

level = Levelmaze(LevelG)
level.generate()


def item_position(item_object):
    position_found = False
    while position_found == False:

        pos_x = (randint(0, 14) * size_case)
        pos_y = (randint(0, 14) * size_case)
        if level.typecase(pos_x, pos_y) == '0':
            items = Item(item_object, pos_x, pos_y)
            return items






