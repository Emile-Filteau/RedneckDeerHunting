import pygame
import Animal
import math


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.animals = []
        self.animals.append(Animal.Animal(40, 30, 10, 'M', 180))
        self.animals.append(Animal.Animal(10, 5, 10, 'M', 180))

    def update(self, framerate, player):
        for animal in self.animals:
            animal.update(framerate, player)

            distance = math.sqrt(math.pow(player.x - animal.x, 2) + math.pow(player.y - animal.y, 2))
            if distance > 200:
                self.animals.remove(self.animals.index(animal))
            if len(self.animals) < 5:
                #TODO : roll dice, spawn animal
                print len(self.animals)

    def spawn_animal(self):
        return
        return

    def draw(self, screen, player):
        """
        //MAP
        /*
        context.fillStyle="#006600";
        context.fillRect(160,0,160,144);

        context.strokeStyle = "000000";
        context.strokeRect(160,0,160,144);

        context.fillStyle = "FFFF00";
        context.fillRect(160+ player.x+80-2.5,player.y+80-2.5,5,5);

        context.fillStyle = "996633";
        for(i in this.animals) {
            animal = this.animals[i]
            context.fillRect(160+ animal.x+80-2.5,animal.y+80-2.5,5,5);
        }
        */
        """
        background_color = (0, 102, 0)
        screen.fill(background_color)

        land_lines_color = (255, 255, 0)
        for i in range(1, 70, 2):
            j = i * 100 / 70
            j = 100 - j + 20
            pygame.draw.rect(screen, land_lines_color, pygame.Rect(i, j, 1, 1))

        for i in range(91, 160, 2):
            j = (i-90) * 100 / 70 + 20
            pygame.draw.rect(screen, land_lines_color, pygame.Rect(i, j, 1, 1))

        x = 2
        for j in range(20, 144, x):
            x += 2
            for i in range(0, 160, 4):
                pygame.draw.rect(screen, land_lines_color, pygame.Rect(i, j, 1, 1))

        #TODO : Draw them with depth
        for animal in self.animals:
            animal.draw(screen, player)

    def check_collision(self, player):
        """
        "draw" a line where the gun is pointing (height?) of length = viewDepth (*2?)
        for each points on this line, check if there is a Moose (animal width / height offsets)
        when an animal is found, kill it and return it
        """
        return