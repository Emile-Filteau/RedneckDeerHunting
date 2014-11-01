import pygame
import time
import sys
from model.Game import *

FRAMERATE = 30


class RedneckDearHunting:
    def __init__(self, resolution=(800, 600), fullscreen=False):
        pygame.init()
        self.resolution = resolution
        self.fullscreen = fullscreen

        if fullscreen:
            self.screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(resolution)

        pygame.display.set_caption('Redneck Dear Hunting')
        pygame.display.set_icon(pygame.image.load('images/Mooses/idle_left.png'))

        self.game = Game(resolution)
        self.views = {}
        self.current_view = ""

    def add_view(self, view_name, view):
        self.views[view_name] = view

    def change_view(self, view_name):
        if self.views[view_name]:
            self.current_view = view_name
            self.views[view_name].init()

    def get_view(self):
        return self.views[self.view_name]

    def loop(self, framerate):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.game.key_press(event.key)
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            """
            if event.type == pygame.KEYUP:
                self.game.key_release(event.key)
            """
        self.game.update(framerate)
        self.game.draw(self.screen)


if __name__ == "__main__":
    redneck = RedneckDearHunting(fullscreen=True)
    while 1:
        time.sleep(FRAMERATE/1000.0)
        redneck.loop(FRAMERATE)
        pygame.display.flip()
