import math
import random
import pygame, pygame.math
from Particles.ParticleEmitter  import *
from Particles.PixelParticle import *
from Player import *
from Animation import *
from Players import *
from Players.MogProjectile import *

class Mog(Player):

    LIFTED_STICK_POS = pygame.Vector2(26, 3)

    def __init__(self, pos):
        standAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogStand.png").convert_alpha(), 32, 32, 1), 300)
        standShootAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogStandShoot.png").convert_alpha(), 32, 32, 1), 300)
        walkAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogWalk.png").convert_alpha(), 32, 32, 2), 300)
        super().__init__("Mog", 100, 0.5, pos, standAnimation, standShootAnimation, walkAnimation, standShootAnimation) 
        self.particles = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.projectileOnStick = None
        self.spawnPos = self.pos + Mog.LIFTED_STICK_POS
        self.angle = 0  # Start angle in degrees
        self.radius = 0  # Initial radius
        self.spiralSpeed = 0.2  # Angular speed in degrees per second
        self.growth_rate = 0.01  # Radius growth rate per second
        self.emitterCont = ParticleEmitter(pos = self.spawnPos, vel = Vector2(0,0), delay = 125, ttl = 3000, color=(60,242,255))
        self.emitterCont.velVar = 0.1
        self.emitterCont.endColor = (255,255,255)
        self.emitterGrow = ParticleEmitter(pos = self.spawnPos, vel = Vector2(0,-0.2), delay = 125, ttl = 500, color=(255,255,255))
        self.emitterGrow.velVar = 0.5
        self.emitterGrow.endColor = (60,242,255)
        


    def update(self, elapsedTime, pressedKeys):
        super().update(elapsedTime, pressedKeys)

        if self.firePressed:
            # spiral spawn position
            self.angle += self.spiralSpeed * elapsedTime
            self.radius += self.growth_rate * elapsedTime
            maxRadius = 7
            if self.radius > maxRadius: self.radius = maxRadius 
            # Convert polar coordinates to Cartesian
            x = self.radius * math.cos(math.radians(self.angle))
            y = self.radius * math.sin(math.radians(self.angle))
            self.spawnPos = self.pos + Mog.LIFTED_STICK_POS + pygame.math.Vector2(x, y)

        for projectile in self.projectiles:
            projectile.update(elapsedTime)

        for particle in self.particles:
            particle.update(elapsedTime)

        self.emitterCont.update(self.pos + Mog.LIFTED_STICK_POS, elapsedTime)
        self.emitterGrow.update(self.spawnPos, elapsedTime)


    def fireDown(self):
        self.spawnPos = self.pos + Vector2(26,3)
        self.radius = 0  # Initial radius 
        self.projectileOnStick = MogProjectile(self.spawnPos)
        self.projectiles.add(self.projectileOnStick)
        self.emitterCont.on = True
        for _ in range(7):    
            self.particles.add(PixelParticle(self.spawnPos.copy(), pygame.Vector2(random.uniform(-0.3, 0.3), random.uniform(-0.3, -0.1)), 3000, (60,242,255),(255,255,255)))

    def fireHold(self, elapsedTime):
        if self.projectileOnStick is not None:
            self.projectileOnStick.pos = self.spawnPos
            if elapsedTime > 1500:
                if self.projectileOnStick.power < 3: self.emitterGrow.emitMultiple(25)
                self.projectileOnStick.power = 3
            elif elapsedTime > 1000:
                if self.projectileOnStick.power < 2: self.emitterGrow.emitMultiple(18)
                self.projectileOnStick.power = 2
            elif elapsedTime > 500:
                if self.projectileOnStick.power < 1: self.emitterGrow.emitMultiple(12)
                self.projectileOnStick.power = 1
            elif elapsedTime > 300:
                self.projectileOnStick.power = 0
            elif elapsedTime > 200:
                self.projectileOnStick.power = -1

    def fireRelease(self, elapsedTime):
        if self.projectileOnStick is not None:
            if self.projectileOnStick.power <= 0:
                self.projectileOnStick.kill()
            else:
                angleRad = math.radians(self.angle)  # Convert angle to radians
                direction = pygame.math.Vector2(math.cos(angleRad), math.sin(angleRad))
                direction.scale_to_length(0.02)
                direction = direction.rotate(90)
                self.projectileOnStick.vel = direction
                self.projectileOnStick = None
        self.radius = 0
        self.emitterCont.on = False
      

    def draw(self, displaySurface):
        super().draw(displaySurface)

        for projectile in self.projectiles:
            projectile.draw(displaySurface)

        for particle in self.particles:
            particle.draw(displaySurface)

        self.emitterCont.draw(displaySurface)
        self.emitterGrow.draw(displaySurface)
