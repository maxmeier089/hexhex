import pygame
import random

class Particle(pygame.sprite.Sprite):
    
    def __init__(self, pos, speed, timeToLive):
        super().__init__()
        self.pos = pos
        self.speed = speed
        self.timeToLive = timeToLive
        self.timeAlreadyLived = 0
        

    def update(self, elapsedTime):
        self.pos += self.speed
        self.timeAlreadyLived += elapsedTime

        if self.timeAlreadyLived >= self.timeToLive:
            self.kill()


    def draw(self, displaySurface):
        pass
        #pygame.draw.line(displaySurface, self.color, self.pos, self.pos) 
        #pygame.draw.circle(displaySurface, self.color, self.pos, self.size)
        #pygame.draw.rect(displaySurface, self.color, pygame.Rect(self.pos.x, self.pos.y, 1, 1))


    