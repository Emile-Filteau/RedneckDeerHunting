import pygame
import time
import sys
from model.Game import *


class RedneckDearHunting:
    def __init__(self, is_fullscreen):
        self.views = {}
        self.current_view = ""

        if is_fullscreen:
            self.screen = pygame.display.set_mode((160, 144), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((160, 144))

        self.game = Game(160, 144)

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
    redneck = RedneckDearHunting(False)
    framerate = 30
    while 1:
        time.sleep(framerate/1000)
        redneck.loop(framerate)
        pygame.display.flip()
