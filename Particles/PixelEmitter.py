from Particles.PixelParticle import *


class PixelEmitter:
    def __init__(self, pos, vel, velVar, delay, ttl, startColor, endColor):
        #super().__init__(pos, vel, velVar, delay, ttl, startColor, endColor)
        self.pos = pos
        self.vel = vel
        self.velVar = velVar
        self.delay = delay
        self.timeUntilNextParticle = 0
        self.ttl = ttl
        self.startColor = startColor
        self.endColor = endColor
        self.particles = pygame.sprite.Group()
        self.on = False

    def createParticle(self, pos, vel, ttl, startColor, endColor):
        self.particles.add(PixelParticle(pos, vel, ttl, startColor, endColor))
