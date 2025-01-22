import pygame, pygame.math
from Particles.PixelEmitter  import *
from Particles.PixelParticle import *
from Player import *
from Animation import *
from Players import *
from Players.ZarvoProjectile import *
from SpinPlayer import SpinPlayer

class Zarvo(SpinPlayer):

    LIFTED_STICK_POS = pygame.Vector2(5, 6)

    def __init__(self, pos):

        standAnimation = Animation(self.loadFrames(pygame.image.load("Players\Zarvo\ZarvoStand.png").convert_alpha(), 32, 32, 1), 300)
        standShootAnimation = Animation(self.loadFrames(pygame.image.load("Players\Zarvo\ZarvoStandShoot.png").convert_alpha(), 32, 32, 1), 300)
        walkAnimation = Animation(self.loadFrames(pygame.image.load("Players\Zarvo\ZarvoWalk.png").convert_alpha(), 32, 32, 2), 300)
        walkShootAnimation = Animation(self.loadFrames(pygame.image.load("Players\Zarvo\ZarvoWalkShoot.png").convert_alpha(), 32, 32, 2), 300)    
        winAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogWinner.png").convert_alpha(), 32, 32, 3), 300)  
        deadAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogDead.png").convert_alpha(), 32, 32, 1), 300)    
        super().__init__("Zarvo", 100, 0.5, pos, pygame.Rect(5, 3, 20, 28), standAnimation, standShootAnimation, walkAnimation, walkShootAnimation, standAnimation, standAnimation, (194, 92, 60), (255,255,255), Zarvo.LIFTED_STICK_POS) 
    

    def createProjectile(self):
        return ZarvoProjectile(self.spawnPos)
