import pygame, pygame.math
from SpinPlayer import SpinPlayer
from Animation import *
from Players.MogProjectile import *


class Mog(SpinPlayer):

    LIFTED_STICK_POS = pygame.Vector2(26, 3)

    def __init__(self, pos):

        standAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogStand.png").convert_alpha(), 32, 32, 1), 300)
        standShootAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogStandShoot.png").convert_alpha(), 32, 32, 1), 300)
        walkAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogWalk.png").convert_alpha(), 32, 32, 2), 300)
        walkShootAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogWalkShoot.png").convert_alpha(), 32, 32, 2), 300)    
        winAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogWinner.png").convert_alpha(), 32, 32, 3), 300)  
        deadAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogDead.png").convert_alpha(), 32, 32, 1), 300)    
        super().__init__("Mog", 100, 0.5, pos, pygame.Rect(7, 3, 19, 28), standAnimation, standShootAnimation, walkAnimation, walkShootAnimation, winAnimation, deadAnimation, (60, 242, 255), (255,255,255), Mog.LIFTED_STICK_POS) 

    
    def createProjectile(self):
        return MogProjectile(self.spawnPos)