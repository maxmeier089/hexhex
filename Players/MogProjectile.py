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
        self.animation.startIndex = 0
        self.animation.endIndex = 2
        self.animation.pendulum = True
        
        explosionFrames = self.loadFrames(pygame.image.load("Players\Mog\MogExplosion.png").convert_alpha(), 32, 32, 13)
        self.explosionAnimation = Animation(explosionFrames, 100)
        self.explosionAnimation.oneShot = True
        
        self.emitter = PixelEmitter(pos = self.pos.copy(), vel = Vector2(0,0), delay = 500, ttl = 3000, color=(60,242,255))
        self.emitter.velVar = 0.1 
        self.emitter.endColor = (255,255,255)
        self.emitter.on = True
        self.children.add(self.emitter)
        
        self.emitterCountdown = PixelEmitter(pos = self.pos.copy(), vel = Vector2(0,0), delay = 750, ttl = 3000, color=(255,237,36))
        self.emitterCountdown.endColor = (255,255,255)
        self.children.add(self.emitterCountdown)
        
        self.released = False
        self.exploded = False

        self.hitbox = pygame.Rect(-4, -4, Projectile.SIZE, Projectile.SIZE)


    def release(self, vel):
        self.vel = vel
        self.released = True
        self.ttl = MogProjectile.TTL


    def explode(self):
        if self.exploded: # already exploded
            # ignore method call
            return
        
        self.exploded = True

        self.emitter.on = False
        self.emitterCountdown.on = False

        self.emitterExplode = PixelEmitter(pos = self.pos.copy(), vel = Vector2(0.1, 0.1) * self.power, delay = 1000, ttl = 777, color=(255, 237, 36))
        self.emitterExplode.velVar = 0.2 
        self.emitterExplode.endColor = (60,242,255)
        self.emitterExplode.randomizeAngle = True
        self.children.add(self.emitterExplode)
        self.emitterExplode.emitMultiple(55 * self.power)
        
        # if self.power == 3 -> startIndex remains 0
        if self.power == 2:
            self.explosionAnimation.setStartIndex(4)
        elif self.power == 1:
            self.explosionAnimation.setStartIndex(6)
      

    def update(self, elapsedTime):
        if not self.exploded:
            self.pos += self.vel * elapsedTime

        self.emitter.pos = self.pos.copy()
        self.emitterCountdown.pos = self.pos.copy()

        if self.released:
            self.ttl -= elapsedTime
            if self.ttl <= 2250:
                self.emitterCountdown.on = True
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

        if self.exploded:
            self.explosionAnimation.update(elapsedTime)
            if not self.explosionAnimation.isRunning and len(self.emitter.particles) == 0 and len(self.emitter.particles) == 0:
                self.kill()

        super().update(elapsedTime)


    def draw(self, displaySurface):

        if not self.exploded:
            self.animation.draw(displaySurface, self.pos - Vector2(4,4))
        else:
            self.explosionAnimation.draw(displaySurface, self.pos - Vector2(16,16))

        super().draw(displaySurface)

