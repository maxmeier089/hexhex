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
        self.spawnPoint = pygame.Vector2(26,3)


    def update(self, elapsedTime, pressedKeys):
        super().update(elapsedTime, pressedKeys)
        for particle in self.particles:
            particle.update(elapsedTime)

    def fireDown(self):
        for _ in range(12):
            self.addSmallParticle()

    def fireHold(self, elapsedTime):
        if elapsedTime > 253:
            self.addSmallParticle()
            self.firePressedTime = 0 # REMOVE HACK

    def addSmallParticle(self):
        s = 0.2
        speed = pygame.Vector2(random.uniform(-s, s), random.uniform(-s, s))
        self.particles.add(PixelParticle(self.pos + self.spawnPoint, speed, 3000, (60,242,255),(255,255,255)))


    def draw(self, displaySurface):
        super().draw(displaySurface)
        for particle in self.particles:
            particle.draw(displaySurface)
