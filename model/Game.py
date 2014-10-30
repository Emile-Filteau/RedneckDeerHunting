from World import *
from Player import *


class Game:
    def __init__(self, camera_width, camera_height):
        self.current_frame = 0
        self.camera_width = camera_width
        self.camera_height = camera_height

        self.world = World(500, 500)
        self.player = Player(self.world)

    def draw(self, screen):
        self.world.draw(screen, self.player)
        self.player.draw(screen)

    def update(self, framerate):
        self.current_frame += framerate
        self.world.update(framerate, self.player)

    def key_press(self, key):
        #ARROWS
        if key == 39:
            self.player.action('R')
        elif key == 38:
            self.player.action('U')
        elif key == 37:
            self.player.action('L')
        elif key == 40:
            self.player.action('D')
        #Z
        elif key == 90:
            self.player.action('PRIMARY')
        #X
        elif key == 88:
            self.player.action('SECONDARY')
        #ENTER
        elif key == 13:
            return
        #SHIFT
        elif key == 16:
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