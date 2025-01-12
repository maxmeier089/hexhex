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
        projectileFrames = self.loadFrames(pygame.image.load("Players\Mog\MogProjectile.png").convert_alpha(), 8, 8, 7)
        self.animation = Animation(projectileFrames, 200)
        explosionFrames = self.loadFrames(pygame.image.load("Players\Mog\MogExplosion.png").convert_alpha(), 32, 32, 13)
        self.explosionAnimation = Animation(explosionFrames, 100)
        self.explosionAnimation.oneShot = True
        self.animation.startIndex = 0
        self.animation.endIndex = 2
        self.animation.pendulum = True
        self.emitter = PixelEmitter(pos = self.pos.copy(), vel = Vector2(0,0), delay = 500, ttl = 3000, color=(60,242,255))
        self.emitter.velVar = 0.1 
        self.emitter.endColor = (255,255,255)
        self.emitter.on = True
        self.emitterExplode = PixelEmitter(pos = self.pos.copy(), vel = Vector2(0, 0), delay = 1000, ttl = 777, color=(255, 237, 36))
        self.emitterExplode.velVar = 0.2 
        self.emitterExplode.endColor = (60,242,255)
        self.emitterExplode.randomizeAngle = True
        self.emitterExplode.on = False
        self.released = False
        self.exploded = False


    def release(self, vel):
        self.vel = vel
        self.released = True
        self.ttl = MogProjectile.TTL

    def explode(self):
        self.exploded = True
        self.emitterExplode.vel = Vector2(0.1, 0.1) * self.power
        self.emitterExplode.emitMultiple(55 * self.power)
        self.emitter.on = False

        # if self.power == 3 -> startIndex remains 0
        if self.power == 2:
            self.explosionAnimation.setStartIndex(4)
        elif self.power == 1:
            self.explosionAnimation.setStartIndex(6)

        

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
            self.explosionAnimation.update(elapsedTime)
            if len(self.emitter.particles) == 0 and len(self.emitter.particles) == 0:
                self.kill()


    def draw(self, displaySurface):

        if not self.exploded:
            self.animation.draw(displaySurface, self.pos - Vector2(4,4))
        else:
            self.explosionAnimation.draw(displaySurface, self.pos - Vector2(16,16))

        self.emitter.draw(displaySurface)
        self.emitterExplode.draw(displaySurface)

