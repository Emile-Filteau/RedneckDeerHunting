import pygame
import sys


class MainMenu:
    def __init__(self, controller, resolution):
        self.controller = controller
        self.resolution = resolution
        self.title = pygame.image.load("images/title.png")
        self.title_position = self.title.get_rect()
        self.title_position.x = 0
        self.title_position.y = 20

        self.font = pygame.font.SysFont("consolas", 60)

        self.options = [
            {'text': 'Start Game'},
            {'text': 'High Scores'},
            {'text': 'Exit'}
        ]
        self.background = pygame.transform.scale(pygame.image.load('images/background.jpg'), (resolution[0], resolution[1]))
        pygame.mixer.music.load('sounds/menu_music.mp3')
        pygame.mixer.music.play(-1)
        self.selected_item = 0
        self.target = pygame.transform.scale(pygame.image.load('images/target.png'), (50, 50))

    def draw(self, screen):
        screen.blit(self.background, self.background.get_rect())

        screen.blit(self.title, self.title_position)

        pos_y = 1.5*self.resolution[1]/5
        i = 0
        for option in self.options:
            label = self.font.render(option['text'], 0, (0, 0, 0))
            pos_x = self.resolution[0]/2 - label.get_width()/2
            screen.blit(label, (pos_x, pos_y))
            if self.selected_item == i:
                screen.blit(self.target, pygame.Rect(pos_x - 60, pos_y, 50, 50))
                screen.blit(self.target, pygame.Rect(pos_x + label.get_width() + 10, pos_y, 50, 50))
            pos_y += self.resolution[1]/5
            i += 1

    def key_press(self, key):
        if key == 273:
            self.selected_item -= 1
            if self.selected_item < 0:
                self.selected_item = len(self.options)-1
        elif key == 274:
            self.selected_item += 1
            if self.selected_item > len(self.options)-1:
                self.selected_item = 0
        elif key == 13:
            self.execute()

    def execute(self):
        if self.selected_item == 0:
            self.controller.change_view('game')
            return
        elif self.selected_item == 1:
            print 'Show the high scores'
            return
        elif self.selected_item == 2:
            sys.exit()