from Particles.PixelParticle import *


class ParticleEmitter:
    def __init__(self, pos, vel, velVar, delay, ttl, startColor, endColor):
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


    def emit(self):
        particleVel = self.vel + pygame.Vector2(random.uniform(-self.velVar, self.velVar), random.uniform(-self.velVar, self.velVar))  
        self.createParticle(self.pos.copy(), particleVel, self.ttl, self.startColor, self.endColor)

    def createParticle(self, pos, vel, ttl, startColor, endColor):
        self.particles.add(PixelParticle(pos, vel, ttl, startColor, endColor))


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

