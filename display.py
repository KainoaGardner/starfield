from settings import *
from star import *

def display():
    screen.fill("black")
    for star in stars:
        star.update()
        star.draw()
    pygame.display.update()
    clock.tick(FPS)