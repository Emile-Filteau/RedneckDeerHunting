import pygame
import Item

IMAGE = pygame.image.load('images/gun.png')
IMAGE_POSITION = pygame.Rect(70, 83, 100, 61)


class Gun(Item.Item):
    def __init__(self):
        self.scope = 2

    def draw(self, screen, resolution):
        new_width = 100/160.0 * resolution[0]
        new_height = 61/144.0 * resolution[1]

        position = pygame.Rect(70*resolution[0]/160, 83*resolution[1]/144, 100, 61)
        image = pygame.transform.scale(IMAGE, (int(new_width), int(new_height)))
        screen.blit(image, position)

    def use_primary(self, player):
        if player.bullet_count > 0:
            player.bullet_count -= 1
            player.shoot()

    def use_secondary(self, player):
        player.scoping = not player.scoping
        player.scope_angle_width = 0
        player.scope_angle_height = 0