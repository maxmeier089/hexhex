import math
import random
import pygame, pygame.math
from ParticleEmitter  import *
from Particles.PixelParticle import *
from Player import *
from Animation import *
from Players import *
from Players.MogProjectile import *

class Mog(Player):
    def __init__(self, pos):
        standAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogStand.png").convert_alpha(), 32, 32, 1), 300)
        standShootAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogStandShoot.png").convert_alpha(), 32, 32, 1), 300)
        walkAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogWalk.png").convert_alpha(), 32, 32, 2), 300)
        super().__init__("Mog", 100, 0.5, pos, standAnimation, standShootAnimation, walkAnimation, standShootAnimation) 
        self.particles = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.projectileOnStick = None
        self.spawnPos = self.pos + pygame.Vector2(26, 3)
        self.angle = 0  # Start angle in degrees
        self.radius = 0  # Initial radius
        self.speed = 0.5  # Angular speed in degrees per second
        self.growth_rate = 0.01  # Radius growth rate per second
        #self.timeUntilNextParticle = 0
        self.emitterA = ParticleEmitter(self.pos + pygame.Vector2(26, 3), Vector2(0,0), 0.1, 125, 3000, (60,242,255),(255,255,255))


    def update(self, elapsedTime, pressedKeys):
        super().update(elapsedTime, pressedKeys)

        if self.firePressed:
            # spiral spawn position
            self.angle += self.speed * elapsedTime
            self.radius += self.growth_rate * elapsedTime
            maxRadius = 7
            if self.radius > maxRadius: self.radius = maxRadius 
            # Convert polar coordinates to Cartesian
            x = self.radius * math.cos(math.radians(self.angle))
            y = self.radius * math.sin(math.radians(self.angle))
            self.spawnPos = self.pos + pygame.Vector2(26, 3) + pygame.math.Vector2(x, y)

            # create particles
            #self.timeUntilNextParticle -= elapsedTime
            #if self.timeUntilNextParticle < 0:
                #self.particles.add(PixelParticle(self.spawnPos.copy(), pygame.Vector2(random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2)), 3000, (60,242,255),(255,255,255)))
                #self.timeUntilNextParticle = 125


        for projectile in self.projectiles:
            projectile.update(elapsedTime)

        for particle in self.particles:
            particle.update(elapsedTime)

        self.emitterA.update(self.pos + pygame.Vector2(26, 3), elapsedTime)


    def fireDown(self):
        self.spawnPos = self.pos + Vector2(26,3)
        self.radius = 0  # Initial radius 
        self.projectileOnStick = MogProjectile(self.spawnPos)
        self.projectiles.add(self.projectileOnStick)
        self.emitterA.on = True
        for _ in range(25):    
            self.particles.add(PixelParticle(self.spawnPos.copy(), pygame.Vector2(random.uniform(-0.3, 0.3), random.uniform(-0.3, -0.1)), 3000, (60,242,255),(255,255,255)))

    def fireHold(self, elapsedTime):
        if self.projectileOnStick is not None:
            self.projectileOnStick.pos = self.spawnPos
            if elapsedTime > 4000:
                self.projectileOnStick.power = 3
            elif elapsedTime > 3000:
                self.projectileOnStick.power = 3
            elif elapsedTime > 2000:
                self.projectileOnStick.power = 2
            elif elapsedTime > 1000:
                self.projectileOnStick.power = 1

    def fireRelease(self, elapsedTime):
        angleRad = math.radians(self.angle)  # Convert angle to radians
        direction = pygame.math.Vector2(math.cos(angleRad), math.sin(angleRad))
        direction.scale_to_length(0.02)
        self.projectileOnStick.vel = direction
        self.projectileOnStick = None
        self.radius = 0
        self.emitterA.on = False
      

    def draw(self, displaySurface):
        super().draw(displaySurface)

        for projectile in self.projectiles:
            projectile.draw(displaySurface)

        for particle in self.particles:
            particle.draw(displaySurface)

        self.emitterA.draw(displaySurface)
