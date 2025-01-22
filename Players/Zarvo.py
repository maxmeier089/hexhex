import math
import pygame, pygame.math
from Particles.PixelEmitter  import *
from Particles.PixelParticle import *
from Player import *
from Animation import *
from Players import *
from Players.MogProjectile import *

class Zarvo(Player):

    LIFTED_STICK_POS = pygame.Vector2(5, 6)

    def __init__(self, pos):

        standAnimation = Animation(self.loadFrames(pygame.image.load("Players\Zarvo\ZarvoStand.png").convert_alpha(), 32, 32, 1), 300)
        standShootAnimation = Animation(self.loadFrames(pygame.image.load("Players\Zarvo\ZarvoStandShoot.png").convert_alpha(), 32, 32, 1), 300)
        walkAnimation = Animation(self.loadFrames(pygame.image.load("Players\Zarvo\ZarvoWalk.png").convert_alpha(), 32, 32, 2), 300)
        walkShootAnimation = Animation(self.loadFrames(pygame.image.load("Players\Zarvo\ZarvoWalkShoot.png").convert_alpha(), 32, 32, 2), 300)    
        winAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogWinner.png").convert_alpha(), 32, 32, 3), 300)  
        deadAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogDead.png").convert_alpha(), 32, 32, 1), 300)    
        #super().__init__("Mog", 100, 0.5, pos, standAnimation, standShootAnimation, walkAnimation, walkShootAnimation, winAnimation, deadAnimation) 
        super().__init__("Mog", 100, 0.5, pos, standAnimation, standShootAnimation, walkAnimation, walkShootAnimation, standAnimation, standAnimation) 
        
        self.projectileOnStick = None
        self.spawnPos = self.pos + Zarvo.LIFTED_STICK_POS
        self.angle = 0  # Start angle in degrees
        self.radius = 0  # Initial radius
        self.spiralSpeed = 0.2  # Angular speed in degrees per second
        self.growthRate = 0.01  # Radius growth rate per second
        
        self.emitterCont = PixelEmitter(pos = self.spawnPos, vel = Vector2(0, 0), delay = 125, ttl = 3000, color=(60,242,255))
        self.emitterCont.velVar = 0.1
        self.emitterCont.endColor = (255,255,255)
        self.children.add(self.emitterCont)

        self.emitterGrow = PixelEmitter(pos = self.spawnPos, vel = Vector2(0, 0), delay = 125, ttl = 500, color=(255,255,255))
        self.emitterGrow.velVar = 0.5
        self.emitterGrow.endColor = (60,242,255)
        self.children.add(self.emitterGrow)

        self.hitboxShape = pygame.Rect(7, 3, 19, 28)

    
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
            self.spawnPos = self.pos + Zarvo.LIFTED_STICK_POS

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
        self.spawnPos = self.pos + Zarvo.LIFTED_STICK_POS
        self.radius = 0  # Initial radius 
        self.projectileOnStick = MogProjectile(self.spawnPos)
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