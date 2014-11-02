import pygame
import Animal
import math, random


class World:
    def __init__(self, resolution):
        self.resolution = resolution

        self.animals = []
        self.animals.append(Animal.Animal(80, 0, 10, 'M', 180))

    def update(self, framerate, player):
        for animal in self.animals:
            animal.update(framerate, player)

            distance = math.sqrt(math.pow(player.x - animal.x, 2) + math.pow(player.y - animal.y, 2))
            if distance > 200:
                self.animals.remove(animal)

        if len(self.animals) < 5:
            if random.random() <= 0.2:
                x = random.random()*50 + 50
                if random.random() > 0.5:
                    x *= -1
                y = random.random()*50 + 50
                if random.random() > 0.5:
                    y *= -1
                a = random.random()*10 + 5
                w = random.random()*100 + 100
                self.animals.append(Animal.Animal(player.x + x, player.y + y, a, 'M', w))

    def spawn_animal(self):
        return

    def draw(self, screen, resolution, player):
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

        pygame.draw.rect(screen, (0, 100, 255), pygame.Rect(0, 0, resolution[0], resolution[1]/5))

        land_lines_color = (255, 255, 0)
        for i in range(0, 7*resolution[0]/16, 2):
            j = float(i / float(7*resolution[0]/16))
            j = resolution[1] - (j*resolution[1]) + (resolution[1]/5)
            pygame.draw.rect(screen, land_lines_color, pygame.Rect(i, j, 1, 1), 1)

        for i in range(9*resolution[0]/16, resolution[0], 2):
            j = float((i-9*resolution[0]/16) / float(7*resolution[0]/16))
            j = (resolution[1]/5) + (j*resolution[1])
            pygame.draw.rect(screen, land_lines_color, pygame.Rect(i, j, 1, 1), 1)

        for x in range(0, resolution[1]/5):
            j = resolution[1]/5 + x*x
            for i in range(0, resolution[0], 4):
                pygame.draw.rect(screen, land_lines_color, pygame.Rect(i, j, 1, 1), 1)

        #TODO : Draw them with depth
        for animal in self.animals:
            animal.draw(screen, resolution, player)

        if player.scoping:
            pygame.draw.rect(screen, (0, 100, 255), pygame.Rect(0, 0, resolution[0], resolution[1]/5))

    def check_collision(self, player, position):
        for animal in self.animals:
            # size = animal.get_size_proportion(player, self.resolution)
            # print (animal.x, animal.y), animal.image_width/2, position
            width = (animal.image_width/2)/5
            if position[0] > animal.x - width and position[0] < animal.x + width:
                if position[1] > animal.y - width and position[1] <= animal.y + width:
                    return animal
        return None