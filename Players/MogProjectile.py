from pygame import Vector2
from Animation import *
from Particles.PixelEmitter import PixelEmitter
from Particles.PixelParticle import *
from Projectile import *


class MogProjectile(Projectile):

    TTL = 4321

    def __init__(self, pos):
        super().__init__(pos)
        self.vel = Vector2(0,0)
        self.power = -1
        frames = self.loadFrames(pygame.image.load("Players\Mog\MogProjectile.png").convert_alpha(), 8, 8, 7)
        self.animation = Animation(frames, 200)
        self.animation.startIndex = 0
        self.animation.endIndex = 2
        self.animation.pendulum = False
        self.emitter = PixelEmitter(pos = self.pos.copy(), vel = Vector2(0,0), delay = 500, ttl = 3000, color=(60,242,255))
        self.emitter.velVar = 0.1 
        self.emitter.endColor = (255,255,255)
        self.emitter.on = True
        self.emitterExplode = PixelEmitter(pos = self.pos.copy(), vel = Vector2(0,0), delay = 1000, ttl = 1000, color=(255,255,255))
        self.emitterExplode.velVar = 0.3 
        self.emitterExplode.endColor = (60,242,255)
        self.emitterExplode.on = False
        self.released = False
        self.exploded = False


    def release(self, vel):
        self.vel = vel
        self.released = True
        self.ttl = MogProjectile.TTL

    def explode(self):
        self.exploded = True
        self.emitterExplode.emitMultiple(123)
        self.emitter.on = False

        

    def update(self, elapsedTime):

        if not self.exploded:
            self.pos += self.vel * elapsedTime

        if self.released:
            self.ttl -= elapsedTime
            if self.ttl <= 0 and not self.exploded:
                self.explode() 

        if self.power == -1:
            self.animation.startIndex = 0
            self.animation.endIndex = 0
            self.emitter.delay = 1500
        elif self.power == 0:
            self.animation.startIndex = 0
            self.animation.endIndex = 1
            self.emitter.delay = 1000
        else:
            self.animation.startIndex = self.power
            self.animation.endIndex = self.power + 2
            self.emitter.delay = 700 - self.power * 200

        self.animation.update(elapsedTime)

        self.emitter.update(self.pos, elapsedTime)
        self.emitterExplode.update(self.pos, elapsedTime)

        if self.exploded:
            if len(self.emitter.particles) == 0 and len(self.emitter.particles) == 0:
                self.kill()


    def draw(self, displaySurface):

        if not self.exploded:
            self.animation.draw(displaySurface, self.pos - Vector2(4,4))

        self.emitter.draw(displaySurface)
        self.emitterExplode.draw(displaySurface)

