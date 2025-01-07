import pygame, pygame.math
from Player import *
from Animation import *

class Mog(Player):
    def __init__(self, pos):
        idleAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogStand.png").convert_alpha(), 32, 32, 1), 300)
        walkAnimation = Animation(self.loadFrames(pygame.image.load("Players\Mog\MogWalk.png").convert_alpha(), 32, 32, 2), 300)
        super().__init__("Mog", 100, 0.5, pos, idleAnimation, walkAnimation)