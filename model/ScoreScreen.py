import pygame
import sys


class ScoreScreen:
    def __init__(self, controller, resolution, game):
        self.controller = controller
        self.resolution = resolution
        self.game = game

        self.font = pygame.font.SysFont("consolas", 60)

        self.title = self.font.render('Final Score : ', (20 , 20))
        self.background = pygame.transform.scale(pygame.image.load('images/background.jpg'), (resolution[0], resolution[1]))
        self.target = pygame.transform.scale(pygame.image.load('images/target.png'), (50, 50))

    def draw(self, screen):
        screen.blit(self.background, self.background.get_rect())
        self.title = self.font.render('Final Score : ' + str(self.game.score))
        screen.blit(self.title, (self.resolution/2 - self.title.get_rect()/2, 20))

    def key_press(self, key):
        # if key == 273:
        #     self.selected_item -= 1
        #     if self.selected_item < 0:
        #         self.selected_item = len(self.options)-1
        # elif key == 274:
        #     self.selected_item += 1
        #     if self.selected_item > len(self.options)-1:
        #         self.selected_item = 0
        # elif key == 13:
        #     self.execute()
        return

    def execute(self):
        # if self.selected_item == 0:
        #     self.controller.change_view('game')
        #     return
        # elif self.selected_item == 1:
        #     print 'Show the high scores'
        #     return
        # elif self.selected_item == 2:
        #     sys.exit()
        return