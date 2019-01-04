import pygame
from pygame.locals import*

from classes import*
from constants import*

#pygame initialisation

pygame.init()

window = pygame.display.set_mode((windows, windows))


pygame.display.set_caption('Mac Gyver')

background = pygame.image.load(img_background).convert()
window.blit(background, (0, 0))


pygame.display.flip()

level = LevelMaze(LevelG)
level.generate()


game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    window.blit(background, (0, 0))
    level.display(window)
    pygame.display.flip()

    
    






















































































'''import pygame
pygame.init()

black = pygame.color(0, 0, 0)
white = pygame.color(255, 255, 255)
corridor_size = 5000

window_size = window_width, window_height = 800, 600
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)

pygame.display.set_caption("generateur de donjons")
clock=pygame.time.clock()
fps = 60


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event == pygame.K_ESACPE):
            pygame.quit()
            quit()
    clock.tick(fps)
    pygame.display.update()'''























'''import turtle

wn = turtle._screen_docrevise()
wn.bgcolor("black")
wn.title("MacGyver")
wn.setup(700, 700)

#create pen

class Pen(turtle.turtle):
    def __init__(self):
        turtle.turtle.__init(self)
        self.shape("square")
        self.penup()
        self.speed(0)


level = [
    "xxxxxxxxxxxxxxx",
    "x xxxx  xxxxxxx",
    "x xxxxx       x",
    "x             x",
    "x xxxxxxx     x",
    "xxxxx         x",
    "x             x",
    "x       xxxxxxx,"
    "x       xxxxxxx",
    "xxxxxxx       x",
    "xxxxxxxx      x",
    "xx            x",
    "xx    xxxxx   x",
    "xxxxx         x",


]
level.append(level)
#create level function
def setupe_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x =-288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "x":
                pen.goto(screen_x, screen_y)
                pen.stamp()'''












































#bmi calculator
'''name = "yk"
heigh_m = 2
weight_kg = 90

bmi = weight_kg / (heigh_m ** 2 )
print("bmi: ")
print(bmi)
if bmi < 25:
    print(name)
    print("is no overweight")
else:
    print(name)
    print("is overweight")

###################################
#calcul de la moyenne
name = "scotty"
note1 = 0
note2 = 0
note3 = 0

moyenne = (note1 + note2 + note3) / 3


print("moyenne:  ")
print(moyenne)

if moyenne < 10:
    print("cet élève est recalé")
elif moyenne == 10:
    print("eleve admis\n mention: passable")
if moyenne > 10:
    print("eleve admis\n mention: bien ")
else:
    pass'''



















