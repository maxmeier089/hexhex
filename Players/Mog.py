import random
import pygame, pygame.math
from Particles.PixelParticle import *
from Player import *
from Animation import *

class Mog(Player):
    def __init__(self, pos):
        standAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogStand.png").convert_alpha(), 32, 32, 1), 300)
        standShootAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogStandShoot.png").convert_alpha(), 32, 32, 1), 300)
        walkAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogWalk.png").convert_alpha(), 32, 32, 2), 300)
        super().__init__("Mog", 100, 0.5, pos, standAnimation, standShootAnimation, walkAnimation, standShootAnimation) 
        self.particles = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.spawnPoint = pygame.Vector2(26,3)
        self.timeUntilNextParticle = 0


    def update(self, elapsedTime, pressedKeys):
        super().update(elapsedTime, pressedKeys)
        for particle in self.particles:
            particle.update(elapsedTime)

        if self.firePressed:
            self.timeUntilNextParticle -= elapsedTime 
            if self.timeUntilNextParticle < 0:
                self.particles.add(PixelParticle(self.pos + self.spawnPoint, pygame.Vector2(random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2)), 3000, (60,242,255),(255,255,255)))
                self.timeUntilNextParticle = 234


    def fireDown(self):
        for _ in range(5):
            self.particles.add(PixelParticle(self.pos + self.spawnPoint, pygame.Vector2(random.uniform(-0.3, 0.3), random.uniform(-0.3, -0.1)), 2000, (60,242,255),(255,255,255)))

    #def fireHold(self, elapsedTime):
        


    def draw(self, displaySurface):
        super().draw(displaySurface)
        for particle in self.particles:
            particle.draw(displaySurface)
