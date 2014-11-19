import pygame
import time
import sys
from model.Game import *
from model.MainMenu import *
from model.ScoreScreen import *

FRAMERATE = 30


class RedneckDearHunting:
    def __init__(self, resolution=(800, 600), fullscreen=False):
        pygame.init()
        pygame.mixer.init(frequency=22050)
        self.resolution = resolution
        self.fullscreen = fullscreen

        if fullscreen:
            self.screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(resolution)

        pygame.display.set_caption('Redneck Dear Hunting')
        pygame.display.set_icon(pygame.image.load('images/Mooses/idle_left.png'))

        self.main_menu = MainMenu(self, resolution)
        self.game = Game(self, resolution)
        #self.score_screen = ScoreScreen(self, resolution, self.game)

        self.views = {
            'main_menu': self.main_menu,
            'game': self.game,
            #'score_screen': self.score_screen
        }
        self.current_view = 'main_menu'

    def change_view(self, view_name):
        if self.views[view_name]:
            self.current_view = view_name

    def loop(self, framerate):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.views[self.current_view].key_press(event.key)
            if event.type == pygame.KEYUP:
                self.views[self.current_view].key_release(event.key)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        if self.current_view == 'game':
            self.game.update(framerate)
        self.views[self.current_view].draw(self.screen)


if __name__ == "__main__":
    redneck = RedneckDearHunting(fullscreen=False)
    while 1:
        time.sleep(FRAMERATE/1000.0)
        redneck.loop(FRAMERATE)
        pygame.display.flip()
