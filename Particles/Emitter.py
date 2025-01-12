import math
import random
import pygame
from GameObject import GameObject

class Emitter(GameObject):

    def __init__(self, pos, vel, delay, ttl, color):
        super().__init__(pos, pygame.Vector2(0,0))
        self.pos = pos
        self.vel = vel
        self.velVar = 0
        self.delay = delay
        self.timeUntilNextParticle = 0
        self.ttl = ttl
        self.ttlVar = 0
        self.startColor = color
        self.endColor = color
        self.angle = 0
        self.angleSpeed = 0
        self.randomizeAngle = False
        self.particles = pygame.sprite.Group()
        self.on = False


    def emit(self):
        if self.randomizeAngle:
            self.angle = random.uniform(0, 360)

        direction = pygame.Vector2(math.cos(math.radians(self.angle)), math.sin(math.radians(self.angle)))
        
        particleVel = direction.elementwise() * self.vel + pygame.Vector2(random.uniform(-self.velVar, self.velVar), random.uniform(-self.velVar, self.velVar))  
        
        self.createParticle(self.pos.copy(), particleVel, self.ttl, self.startColor, self.endColor)


    def emitMultiple(self, n):
        for _ in range(n):
            self.emit()
            

    def createParticle(self, pos, vel, ttl, startColor, endColor):
        pass


    def update(self, elapsedTime):
        self.angle += self.angleSpeed * elapsedTime
        if self.angle >= 360:
            self.angle -= 360

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

