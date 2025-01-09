import pygame
import random

class Emitter:
    def __init__(self, pos, vel, delay, ttl, color):
        self.pos = pos
        self.vel = vel
        self.velVar = 0
        self.delay = delay
        self.timeUntilNextParticle = 0
        self.ttl = ttl
        self.ttlVar = 0
        self.startColor = color
        self.endColor = color
        self.particles = pygame.sprite.Group()
        self.on = False


    def emit(self):
        particleVel = self.vel + pygame.Vector2(random.uniform(-self.velVar, self.velVar), random.uniform(-self.velVar, self.velVar))  
        self.createParticle(self.pos.copy(), particleVel, self.ttl, self.startColor, self.endColor)

    def emitMultiple(self, n):
        for _ in range(n):
            self.emit()

    def createParticle(self, pos, vel, ttl, startColor, endColor):
        pass


    def update(self, pos, elapsedTime):
        self.pos = pos
        for particle in self.particles:
            particle.update(elapsedTime)

        if self.on:
            self.timeUntilNextParticle -= elapsedTime

            if self.timeUntilNextParticle < 0:
                self.emit()
                self.timeUntilNextParticle = self.delay


    def draw(self, displaySurface):
        for particle in self.particles:
            particle.draw(displaySurface)

