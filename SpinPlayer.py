import math
import pygame, pygame.math
from Particles.PixelEmitter  import *
from Particles.PixelParticle import *
from Player import *
from Animation import *
from Players import *
from Players.MogProjectile import *

class SpinPlayer(Player):

    def __init__(self, name, health, speed,  pos, hitboxShape, standAnimation, standShootAnimation, walkAnimation, walkShootAnimation, winAnimation, deadAnimation, colorA, colorB, liftedStickPos):

        super().__init__(name, health, speed, pos, hitboxShape, standAnimation, standShootAnimation, walkAnimation, walkShootAnimation, winAnimation, deadAnimation) 
        
        self.colorA = colorA
        self.colorB = colorB

        self.liftedStickPos = liftedStickPos

        self.projectileOnStick = None

        self.spawnPos = self.pos + self.liftedStickPos
        self.angle = 0  # Start angle in degrees
        self.radius = 0  # Initial radius
        self.spiralSpeed = 0.2  # Angular speed in degrees per second
        self.growthRate = 0.01  # Radius growth rate per second
        
        self.emitterCont = PixelEmitter(pos = self.spawnPos, vel = Vector2(0, 0), delay = 125, ttl = 3000, color=colorA)
        self.emitterCont.velVar = 0.1
        self.emitterCont.endColor = colorB
        self.children.add(self.emitterCont)

        self.emitterGrow = PixelEmitter(pos = self.spawnPos, vel = Vector2(0, 0), delay = 125, ttl = 500, color=colorB)
        self.emitterGrow.velVar = 0.5
        self.emitterGrow.endColor = colorA
        self.children.add(self.emitterGrow)


    def createProjectile(self):
        pass

    
    def hit(self, impact):
        super().hit(impact)
        if not self.isAlive:
            self.emitterCont.on = False
            self.removeProjectileOnStick()


    def win(self):
        super().win()
        self.emitterCont.on = True
        self.removeProjectileOnStick()
        

    def removeProjectileOnStick(self):
        if self.projectileOnStick is not None:
            self.projectileOnStick.kill()
            self.projectileOnStick = None
        

    def update(self, elapsedTime, pressedKeys):

        if (self.isWinner):
            self.spawnPos = self.pos + Vector2(5,5)
        else:
            self.spawnPos = self.pos + self.liftedStickPos

            if self.firePressed:
                # spiral spawn position
                self.angle += self.spiralSpeed * elapsedTime
                self.radius += self.growthRate * elapsedTime
                maxRadius = 7
                if self.radius > maxRadius: self.radius = maxRadius 
                # Convert polar coordinates to Cartesian
                x = self.radius * math.cos(math.radians(self.angle))
                y = self.radius * math.sin(math.radians(self.angle))
                self.spawnPos += pygame.math.Vector2(x, y)     

        self.emitterCont.pos = self.spawnPos.copy()
        self.emitterGrow.pos = self.spawnPos.copy()

        super().update(elapsedTime, pressedKeys)


    def fireDown(self):
        self.spawnPos = self.pos + self.liftedStickPos
        self.radius = 0  # Initial radius 
        self.projectileOnStick = self.createProjectile()
        self.projectiles.add(self.projectileOnStick)
        self.emitterCont.on = True

    def fireHold(self, elapsedTime):
        if self.projectileOnStick is not None:
            self.projectileOnStick.pos = self.spawnPos
            if elapsedTime > 2250:
                if self.projectileOnStick.power < 3:
                    self.emitterGrow.emitMultiple(25)
                    self.projectileOnStick.power = 3
            elif elapsedTime > 1500:
                if self.projectileOnStick.power < 2: self.emitterGrow.emitMultiple(18)
                self.projectileOnStick.power = 2
            elif elapsedTime > 750:
                if self.projectileOnStick.power < 1: self.emitterGrow.emitMultiple(12)
                self.projectileOnStick.power = 1
            elif elapsedTime > 500:
                self.projectileOnStick.power = 0
            elif elapsedTime > 250:
                self.projectileOnStick.power = -1

    def fireRelease(self, elapsedTime):
        if self.projectileOnStick is not None:
            if self.projectileOnStick.power <= 0:
                self.projectileOnStick.kill()
            else:
                angleRad = math.radians(self.angle)  # Convert angle to radians
                direction = pygame.math.Vector2(math.cos(angleRad), math.sin(angleRad))
                direction.scale_to_length(0.035)
                direction = direction.rotate(90)
                self.projectileOnStick.release(direction)
                self.projectileOnStick = None
        self.radius = 0
        self.emitterCont.on = False  