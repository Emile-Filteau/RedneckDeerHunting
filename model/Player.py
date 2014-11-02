import pygame
import Gun
import math


class Player:
    def __init__(self, game):
        self.x = 0
        self.y = 0
        self.angle = 0

        self.depth_of_field = 100
        self.view_angle = 45
        self.move_distance = 2
        self.move_direction = ""

        self.selected_item = 0

        self.items = []
        self.items.append(Gun.Gun())
        self.bullet_count = 12

        self.scope_angle_width = 0
        self.scope_angle_height = 0
        self.scoping = False
        self.scope = pygame.image.load("images/scope.png")

        self.foot_step = pygame.mixer.Sound('sounds/footstep.wav')

        self.game = game

    def draw(self, screen, resolution):
        if not self.scoping:
            self.items[self.selected_item].draw(screen, resolution)
        else:
            image = pygame.transform.scale(self.scope, (resolution[0], int(4*resolution[1]/5.0)))
            screen.blit(image, pygame.Rect(0, resolution[1]/5, resolution[0], resolution[1]-resolution[1]/5))

    def shoot(self):
        #self.make_noise(alot, false)
        cadran = self.get_look_cadran()
        angle_theta = math.radians((self.angle % 90) + (self.view_angle/2 + self.scope_angle_width))
        for p in range(0, self.depth_of_field*2):
            check_collision = (0, 0)
            if cadran == 0 or cadran == 2:
                p_x = math.sin(angle_theta) * p
                p_y = math.cos(angle_theta) * p
            elif cadran == 1 or cadran == 3:
                p_x = math.sin(angle_theta) * p
                p_y = math.cos(angle_theta) * p
            if cadran == 0:
                check_collision = (self.x + p_x, self.y + p_y)
            elif cadran == 1:
                check_collision = (self.x - p_x, self.y + p_y)
            elif cadran == 2:
                check_collision = (self.x - p_x, self.y - p_y)
            if cadran == 3:
                check_collision = (self.x + p_x, self.y - p_y)

            target = self.game.world.check_collision(self, check_collision)
            if target:
                self.game.kill(target)
                return

    def add_move_direction(self, key_action):
        self.move_direction += key_action

    def remove_move_direction(self, key_action):
        if key_action in self.move_direction:
            self.move_direction = self.move_direction.replace(key_action, "")

    def action(self):
        if not self.scoping:
            if 'R' in self.move_direction or 'L' in self.move_direction:
                self.rotate(self.move_direction)
            if 'U' in self.move_direction or 'D' in self.move_direction:
                self.move(self.move_direction)
        else:
            if 'R' in self.move_direction or 'L' in self.move_direction or \
                    'U' in self.move_direction or 'D' in self.move_direction:
                self.move_scope_perspective(self.move_direction)

    def move(self, direction):
        cadran = self.get_look_cadran()
        angle_theta = (self.angle % 90) + (self.view_angle/2)
        angle_beta = 90 - angle_theta
        if cadran == 0 or cadran == 2:
            delta_x = (self.move_distance * math.sin(self.degree_to_radian(angle_beta)) / math.sin(self.degree_to_radian(90)))
            delta_y = (self.move_distance * math.sin(self.degree_to_radian(angle_theta)) / math.sin(self.degree_to_radian(90)))
        if cadran == 1 or cadran == 3:
            delta_x = (self.move_distance * math.sin(self.degree_to_radian(angle_theta)) / math.sin(self.degree_to_radian(90)))
            delta_y = (self.move_distance * math.sin(self.degree_to_radian(angle_beta)) / math.sin(self.degree_to_radian(90)))
        foward = 0
        if 'U' in self.move_direction:
            foward = 1
        elif 'D' in self.move_direction:
            foward = -1

        if cadran == 0:
            self.x += delta_x * foward
            self.y += delta_y * foward
        elif cadran == 1:
            self.x -= delta_x * foward
            self.y += delta_y * foward
        elif cadran == 2:
            self.x -= delta_x * foward
            self.y -= delta_y * foward
        elif cadran == 3:
            self.x += delta_x * foward
            self.y -= delta_y * foward
        #self.foot_step.play()

    def degree_to_radian(self, degree):
        return degree * (math.pi / 180)

    def get_look_cadran(self):
        return math.floor(self.angle/90)

    def rotate(self, direction):
        if 'R' in self.move_direction:
            self.angle += 10
            if self.angle >= 360:
                self.angle %= 360
        elif 'L' in self.move_direction:
            self.angle -= 10
            if self.angle < 0:
                self.angle += 360

    def move_scope_perspective(self, direction):
        if 'L' in self.move_direction:
            self.scope_angle_width -= 1
            if self.scope_angle_width < self.view_angle/2 * -1:
                self.scope_angle_width = self.view_angle/2 * -1
        elif 'R' in self.move_direction:
            self.scope_angle_width += 1
            if self.scope_angle_width > self.view_angle/2:
                self.scope_angle_width = self.view_angle/2
        elif 'U' in self.move_direction:
            self.scope_angle_height += 5
            if self.scope_angle_height > 180:
                self.scope_angle_height = 180
        elif 'D' in self.move_direction:
            self.scope_angle_height -= 5
            if self.scope_angle_height < -180:
                self.scope_angle_height = -180

    def use(self, which):
        if which == 'PRIMARY':
            self.items[self.selected_item].use_primary(self)
        else:
            self.items[self.selected_item].use_secondary(self)

    def make_noise(self, amount, is_animal_friendly):
        #TODO Need to pass this to world (world.emitNoise(this, amount, isAnimalFriendly))
        return