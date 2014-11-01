from World import *
from Player import *


class Game:
    def __init__(self, resolution):
        self.current_frame = 0
        self.resolution = resolution
        self.font = pygame.font.SysFont("consolas", resolution[0]/20)

        self.world = World()
        self.player = Player(self.world)

        self.score = 0

    def draw(self, screen):
        self.world.draw(screen, self.resolution, self.player)
        self.player.draw(screen, self.resolution)

        # render text
        score_label = self.font.render("Score: " + str(self.score), 0, (0, 0, 0))
        screen.blit(score_label, (2, 0))

        bullets_label = self.font.render("Bullets: " + str(self.player.bullet_count), 0, (0, 0, 0))
        screen.blit(bullets_label, (0, self.resolution[0]/20))


    def update(self, framerate):
        self.current_frame += framerate
        self.world.update(framerate, self.player)

    def key_press(self, key):
        #ARROWS
        if key == 275:
            self.player.action('R')
        elif key == 273:
            self.player.action('U')
        elif key == 276:
            self.player.action('L')
        elif key == 274:
            self.player.action('D')
        #Z
        elif key == 122:
            self.player.action('PRIMARY')
        #X
        elif key == 120:
            self.player.action('SECONDARY')
        #ENTER
        elif key == 13:
            return
        #SHIFT
        elif key == 303:
            return
"""
ADD KEY RELEASE YOU WANT TO CREATE FLUID MOVEMENT
    keyrelease : function(key) {
        this.base(key);
        //droite
        if(key == 39) {
        }
        //haut
        else if(key == 38) {
        }
        //gauche
        else if(key == 37) {
        }
        //bas
        else if(key == 40) {
        }
        //Z
        else if(key == 90) {

        }
        //X
        else if(key == 88) {

        }
        //ENTER
        else if(key == 13) {

        }
        //SHIFT
        else if(key == 16) {

        }
    }
"""