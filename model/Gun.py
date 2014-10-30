import pygame
import Item

IMAGE = pygame.image.load('images/gun.png')
IMAGE_POSITION = pygame.Rect(70, 83, 100, 61)


class Gun(Item.Item):
    def __init__(self):
        self.scope = 2
        self.bullet_count = 12

    def draw(self, screen):
        screen.blit(IMAGE, IMAGE_POSITION)

    def use_primary(self, player):
        if self.bullet_count > 0:
            self.bullet_count -= 1
            player.shoot()

    def use_secondary(self, player):
        player.scoping = not player.scoping
        player.scope_angle_width = 0
        player.scope_angle_height = 0