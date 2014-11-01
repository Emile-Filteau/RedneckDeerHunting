import pygame
import Gun
import math


class Player:
    def __init__(self, world):
        self.x = 0
        self.y = 0
        self.angle = 0

        self.depth_of_field = 100
        self.view_angle = 45
        self.move_distance = 5

        self.selected_item = 0

        self.items = []
        self.items.append(Gun.Gun())
        self.bullet_count = 12

        self.scope_angle_width = 0
        self.scope_angle_height = 0
        self.scoping = False
        self.scope = pygame.image.load("images/scope.png")

        self.world = world

    def draw(self, screen, resolution):
        if not self.scoping:
            self.items[self.selected_item].draw(screen, resolution)
        else:
            image = pygame.transform.scale(self.scope, (resolution[0], int(4*resolution[1]/5.0)))
            screen.blit(image, pygame.Rect(0, resolution[1]/5, resolution[0], resolution[1]-resolution[1]/5))

    def shoot(self):
        print 'SHOOT'
        self.world.check_collision(self)
        #self.make_noise(alot, false)

    def action(self, key_action):
        if not self.scoping:
            if key_action == 'R' or key_action == 'L':
                self.rotate(key_action)
            elif key_action == 'U' or key_action == 'D':
                self.move(key_action)
        else:
            if key_action == 'R' or key_action == 'L' or key_action == 'U' or key_action == 'D':
                self.move_scope_perspective(key_action)

        if key_action == 'PRIMARY' or key_action == 'SECONDARY':
            self.use(key_action)

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
        if direction == 'U':
            foward = 1
        elif direction == 'D':
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

    def degree_to_radian(self, degree):
        return degree * (math.pi / 180)

    def get_look_cadran(self):
        return math.floor(self.angle/90)

    def rotate(self, direction):
        if direction == 'R':
            self.angle += 2
            if self.angle >= 360:
                self.angle %= 360
        elif direction == 'L':
            self.angle -= 2
            if self.angle < 0:
                self.angle += 360

    def move_scope_perspective(self, direction):
        if direction == 'L':
            self.scope_angle_width -= 1
            if self.scope_angle_width < self.view_angle/2 * -1:
                self.scope_angle_width = self.view_angle/2 * -1
        elif direction == 'R':
            self.scope_angle_width += 1
            if self.scope_angle_width > self.view_angle/2:
                self.scope_angle_width = self.view_angle/2
        elif direction == 'U':
            self.scope_angle_height += 5
            if self.scope_angle_height > 180:
                self.scope_angle_height = 180
        elif direction == 'D':
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