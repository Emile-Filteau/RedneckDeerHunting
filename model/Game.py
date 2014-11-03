from World import *
from Player import *


class Game:
    def __init__(self, controller, resolution):
        self.current_frame = 0
        self.resolution = resolution
        self.font = pygame.font.SysFont("consolas", resolution[0]/20)

        self.world = World(resolution)
        self.player = Player(self)

        self.score = 0

    def draw(self, screen):
        self.world.draw(screen, self.resolution, self.player)
        self.player.draw(screen, self.resolution)

        # render text
        score_label = self.font.render("Score: " + str(self.score), 0, (0, 0, 0))
        screen.blit(score_label, (2, 0))

        bullets_label = self.font.render("Bullets: " + str(self.player.bullet_count), 0, (0, 0, 0))
        screen.blit(bullets_label, (0, self.resolution[1]/20))

        bullets_label = self.font.render("X: " + str(self.player.x) + " Y: " + str(self.player.y), 0, (0, 0, 0))
        screen.blit(bullets_label, (0, self.resolution[1]/10))

        bullets_label = self.font.render("Angle: " + str(self.player.angle), 0, (0, 0, 0))
        screen.blit(bullets_label, (0, 1.5*self.resolution[1]/10))

    def update(self, framerate):
        self.current_frame += framerate
        self.player.action()
        self.world.update(framerate, self.player)

    def kill(self, animal):
        self.score += animal.weight * animal.age
        self.world.animals.remove(animal)

    def end(self):
        return

    def key_press(self, key):
        #ARROWS
        if key == 275:
            self.player.add_move_direction('R')
        elif key == 273:
            self.player.add_move_direction('U')
        elif key == 276:
            self.player.add_move_direction('L')
        elif key == 274:
            self.player.add_move_direction('D')
        #Z
        elif key == 122:
            self.player.use('PRIMARY')
        #X
        elif key == 120:
            self.player.use('SECONDARY')
        #ENTER
        elif key == 13:
            return
        #SHIFT
        elif key == 303:
            return

    def key_release(self, key):
        if key == 275:
            self.player.remove_move_direction('R')
        elif key == 273:
            self.player.remove_move_direction('U')
        elif key == 276:
            self.player.remove_move_direction('L')
        elif key == 274:
            self.player.remove_move_direction('D')