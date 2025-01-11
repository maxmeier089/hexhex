from pygame import Vector2
from Animation import *
from Particles.PixelEmitter import PixelEmitter
from Particles.PixelParticle import *
from Projectile import *


class MogProjectile(Projectile):

    TTL = 5555

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
        self.released = False


    def release(self, vel):
        self.vel = vel
        self.released = True
        self.ttl = MogProjectile.TTL
        

    def update(self, elapsedTime):

        self.pos += self.vel * elapsedTime

        if self.released:
            self.ttl -= elapsedTime
            if self.ttl <= 0:
                self.kill()

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


    def draw(self, displaySurface):
        self.animation.draw(displaySurface, self.pos - Vector2(4,4))
        self.emitter.draw(displaySurface)

