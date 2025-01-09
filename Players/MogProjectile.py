import random
from pygame import Vector2
from Animation import *
from Particles.PixelParticle import *
from Projectile import *


class MogProjectile(Projectile):
    def __init__(self, pos):
        super().__init__(pos)
        self.vel = Vector2(0,0)
        self.power = -1
        frames = self.loadFrames(pygame.image.load("Players\Mog\MogProjectile.png").convert_alpha(), 8, 8, 7)
        self.animation = Animation(frames, 200)
        self.animation.startIndex = 0
        self.animation.endIndex = 2
        self.animation.pendulum = False
        self.particles = pygame.sprite.Group()
        self.timeUntilNextParticle = 0
        

    def update(self, elapsedTime):
        self.pos += self.vel * elapsedTime

        if self.power == -1:
            self.animation.startIndex = 0
            self.animation.endIndex = 0
        elif self.power == 0:
            self.animation.startIndex = 0
            self.animation.endIndex = 1
        else:
            self.animation.startIndex = self.power
            self.animation.endIndex = self.power + 2

        self.animation.update(elapsedTime)

        self.timeUntilNextParticle -= elapsedTime

        if self.timeUntilNextParticle < 0:
            self.particles.add(PixelParticle(self.pos.copy(), pygame.Vector2(random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1)), 3000, (60,242,255),(255,255,255)))
            self.timeUntilNextParticle = 700 - self.power * 200




        for particle in self.particles:
            particle.update(elapsedTime)


    def draw(self, displaySurface):
        self.animation.draw(displaySurface, self.pos - Vector2(4,4))
        for particle in self.particles:
            particle.draw(displaySurface)

