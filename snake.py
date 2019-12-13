import math
import random
import pygame
import tkinter as tk

class snake():
    global space, width, grid_space, space
    def __init__(self):
        self.pos=(10,10)
        self.dirx=0
        self.diry=0
        self.color=(255,0,0)

    def draw(self,surface):
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.color, (i*space,j*space,space+1,space+1))

    def move():
            passSs


def drawGrid(surface):
    global width, grid_space, space, s
    space=width//grid_space
    startPoint=0
    for l in range(grid_space):
        startPoint= startPoint+space
        pygame.draw.line(surface, (225, 225, 225), (startPoint, 0), (startPoint, width))
        pygame.draw.line(surface, (225, 225, 225), (0, startPoint), (width, startPoint))

def redrawWindow(surface):
    surface.fill((0,0,0))
    drawGrid(surface)
    s.draw(surface)
    pygame.display.update()

def main():
    global width, grid_space, s
    size = width, height = 500, 500
    grid_space = 20
    screen = pygame.display.set_mode(size)
    s = snake()
    while 1:
        redrawWindow(screen)

    pass
main()
