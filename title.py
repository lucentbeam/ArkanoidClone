__author__ = 'sean'

#external modules
import sys
import pygame

(width, height) = (800,600)

black = (0,0,0)
white = (0,0,0)
game_name = "Crackanoid"

font_test = pygame.font.SysFont("vera",72)

def Title(self):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Crackanoid')
    screen.fill(black)
    font_test.render(game_name, True, (255,255,255))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
