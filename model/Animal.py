import pygame
import math
import random

IDLE_IMAGES = {'L': pygame.image.load('images/Mooses/idle_left.png'),
               'R': pygame.image.load('images/Mooses/idle_right.png')}

MOVE_IMAGES = {'L': [pygame.image.load("images/Mooses/move_left_0.png"),
                     pygame.image.load("images/Mooses/move_left_1.png")],
               'R': [pygame.image.load("images/Mooses/move_right_0.png"),
                     pygame.image.load("images/Mooses/move_right_1.png")]}

EAT_IMAGES = [pygame.image.load("images/Mooses/eating_0.png"),
              pygame.image.load("images/Mooses/eating_1.png"),
              pygame.image.load("images/Mooses/eating_2.png")]
IDLE = 0
MOVE = 1
EAT = 2
RUN = 3


class Animal:
    def __init__(self, x, y, age, sex, weight):
        self.x = x
        self.y = y

        self.age = age
        self.sex = sex
        self.weight = weight

        self.state = 0
        self.moving = False

        self.eating = True
        self.direction = ''
        self.look_direction = 'L'

        self.decision_counter = 0
        self.animation_counter = 0
        self.animation = 0

        self.image_width = 51
        self.image_height = 51

    def move(self, player):
        if 'L' in self.direction:
            self.x -= random.random()
        elif 'R' in self.direction:
            self.x += random.random()
        if 'U' in self.direction:
            self.y += random.random()
        elif 'D' in self.direction:
            self.y -= random.random()

    def update(self, framerate, player):
        if self.x > player.x:
            if 'U' in self.direction:
                self.look_direction = 'L'
            elif 'D' in self.direction:
                self.look_direction = 'R'
        else:
            if 'U' in self.direction:
                self.look_direction = 'R'
            elif 'D' in self.direction:
                self.look_direction = 'L'

        if self.y > player.y:
            if 'L' in self.direction:
                self.look_direction = 'R'
            elif 'R' in self.direction:
                self.look_direction = 'L'
        else:
            if 'L' in self.direction:
                self.look_direction = 'L'
            elif 'R' in self.direction:
                self.look_direction = 'R'

        if self.state == MOVE:
            self.move(player)
            self.animation_counter += framerate
            if self.animationCounter >= 500:
                self.animation += 1
                if self.animation >= len(MOVE_IMAGES[self.look_direction]):
                    self.animation = 0
                self.animation_counter = 0

        elif self.state == EAT:
            self.animation_counter += framerate
            if self.animation_counter >= 250:
                self.animation += 1
                if self.animation >= len(EAT_IMAGES):
                    self.animation = 0
                self.animation_counter = 0

        self.decision_counter += framerate
        if self.decision_counter >= 1000:
            self.take_decision()
            self.decision_counter = 0

    def take_decision(self):
        if self.state == IDLE:
            r = random.random()
            if 0 <= r < 0.25:
                self.state = EAT
                self.reset_counters()
            elif r <= 0.25 and r < 0.50:
                self.state = MOVE
                self.direction = ''
                dir_x = random.random()
                dir_y = random.random()
                if dir_x > 0.5:
                    self.direction += "L"
                else:
                    self.direction += "R"
                if dir_y > 0.5:
                    self.direction += "U"
                else:
                    self.direction += "D"
                self.reset_counters()
        if self.state == EAT:
            r = random.random()
            if 0 <= r <= 0.10:
                self.state = IDLE
                self.reset_counters()
        if self.state == MOVE:
            r = random.random()
            if 0 <= r <= 0.30:
                self.state = IDLE
                self.reset_counters()

    def reset_counters(self):
        self.animation = 0
        self.animation_counter = 0
        self.decision_counter = 0

    def draw(self, screen, player):
        distance = math.sqrt(math.pow(player.x - self.x, 2) + math.pow(player.y - self.y, 2))

        animal_angle = math.atan2(player.y - self.y, player.x - self.x)
        animal_angle += math.pi
        animal_angle *= (180/math.pi)

        size_proportion = distance * 1.5 / player.depth_of_field
        size_proportion = 1.5 - size_proportion

        relative_x = 0
        if player.angle > 270 and animal_angle < 90:
            relative_x = (360 - player.angle + animal_angle) * 160 / player.view_angle
        else:
            relative_x = (animal_angle - player.angle) * 160 / player.view_angle
        relative_y = distance * 144 / 100
        relative_y = 144 - relative_y

        if player.scoping:
            size_proportion = (distance / 2) * 1.5 / player.depth_of_field
            size_proportion = 1.5 - size_proportion

            if player.angle > 270 and animal_angle < 90:
                relative_x = (360 - player.angle - player.scope_angle_width + animal_angle) * 160 / player.view_angle
            else:
                relative_x = (animal_angle - player.scope_angle_width - player.angle) * 160 / player.view_angle

            scope_angle_height = player.scope_angle_height + 45
            delta_h = (scope_angle_height * 100) / 90
            delta_h -= 50
            relative_y += (relative_y * delta_h / 100)

        new_width = self.image_width * size_proportion
        new_height = self.image_height * size_proportion
        if 0 - new_width/2 < relative_x < 160 + new_width/2:
            if 20 - new_height/2 < relative_y < 144 + new_height/2:
                image_rect = pygame.Rect(relative_x-new_width/2, relative_y-new_height/2, new_width, new_height)
                if self.state == MOVE:
                    screen.blit(MOVE_IMAGES[self.look_direction][self.animation], image_rect)
                elif self.state == EAT:
                    screen.blit(EAT_IMAGES[self.animation], image_rect)
                else:
                    screen.blit(IDLE_IMAGES[self.look_direction], image_rect)

    def get_degrees_between_player(self, player):
        angle = 0
        if self.x >= player.x:
            if self.y >= player.y:
                angle = math.atan((player.y - self.y) / (player.x - self.x))
            else:
                angle = math.atan((player.x - self.x) / (player.y - self.y))
        else:
            if self.y >= player.y:
                angle = math.atan((player.x - self.x) / (player.y - self.y))
            else:
                angle = math.atan((player.y - self.y) / (player.x - self.x))
        angle *= 180 / math.pi
        return angle

    def get_cadran_angle(self, player):
        angle = 0
        if self.x >= player.x:
            if self.y >= player.y:
                angle = 0
            else:
                angle = 270
        else:
            if self.y >= player.y:
                angle = 90
            else:
                angle = 180
        return angle