import pygame
import math
import random

TREE_IMAGES = [pygame.image.load('images/Trees/tree0.png'),
               pygame.image.load('images/Trees/tree1.png'),
               pygame.image.load('images/Trees/tree2.png')]
TREE_SIZE = (500, 500)


class Tree():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.type = random.randint(0, 2)

    def draw(self, screen, resolution, player):
        distance = math.sqrt(math.pow(player.x - self.x, 2) + math.pow(player.y - self.y, 2))

        angle = math.atan2(player.y - self.y, player.x - self.x)
        angle += math.pi
        angle *= (180/math.pi)

        size_proportion = distance * 1.5 / player.depth_of_field
        size_proportion = 1.5 - size_proportion

        relative_x = 0
        if player.angle > 270 and angle < 90:
            relative_x = (360 - player.angle + angle) * resolution[0] / player.view_angle
        else:
            relative_x = (angle - player.angle) * resolution[0] / player.view_angle
        relative_y = distance * resolution[1] / 100
        relative_y = resolution[1] - relative_y

        if player.scoping:
            size_proportion *= 2
            if player.angle > 270 and angle < 90:
                relative_x = (360 - player.angle - player.scope_angle_width + angle) * resolution[0] / player.view_angle
            else:
                relative_x = (angle - player.scope_angle_width - player.angle) * resolution[0] / player.view_angle

            scope_angle_height = player.scope_angle_height + 45
            delta_h = (scope_angle_height * 100) / 90
            delta_h -= 50
            relative_y += (relative_y * delta_h / 100)

        new_width = resolution[0] * size_proportion
        new_height = resolution[1] * size_proportion
        if 0 - new_width/2 < relative_x < resolution[0] + new_width/2:
            if relative_y + new_height/2 >= resolution[1]/5 and relative_y < resolution[1]:
                image_rect = pygame.Rect(relative_x-new_width/2, relative_y-new_height/2, new_width, new_height)
                image = pygame.transform.scale(TREE_IMAGES[self.type], (int(new_width), int(new_height)))
                screen.blit(image, image_rect)

    def check_bullet_collision(self, player, resolution):
        distance = math.sqrt(math.pow(player.x - self.x, 2) + math.pow(player.y - self.y, 2))

        angle = math.atan2(player.y - self.y, player.x - self.x)
        angle += math.pi
        angle *= (180/math.pi)

        size_proportion = distance * 1.5 / player.depth_of_field
        size_proportion = 1.5 - size_proportion

        relative_x = 0
        if player.angle > 270 and angle < 90:
            relative_x = (360 - player.angle + angle) * resolution[0] / player.view_angle
        else:
            relative_x = (angle - player.angle) * resolution[0] / player.view_angle
        relative_y = distance * resolution[1] / 100
        relative_y = resolution[1] - relative_y

        if player.scoping:
            size_proportion = (distance / 2) * 1.5 / player.depth_of_field
            size_proportion = 1.5 - size_proportion

            if player.angle > 270 and angle < 90:
                relative_x = (360 - player.angle - player.scope_angle_width + angle) * resolution[0] / player.view_angle
            else:
                relative_x = (angle - player.scope_angle_width - player.angle) * resolution[0] / player.view_angle

            scope_angle_height = player.scope_angle_height + 45
            delta_h = (scope_angle_height * 100) / 90
            delta_h -= 50
            relative_y += (relative_y * delta_h / 100)

        new_width = resolution[0] * size_proportion
        new_height = resolution[1] * size_proportion
        if relative_x - new_width/2 < resolution[0]/2 < relative_x + new_width/2:
            if relative_y - new_height/2 < resolution[1]/2 < relative_y + new_height/2:
                return True
        return False

    def distance(self, player):
        return math.sqrt(math.pow(player.x - self.x, 2) + math.pow(player.y - self.y, 2))