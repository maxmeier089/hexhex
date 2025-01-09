import pygame
from Player import *
from Animation import *
from Players.Mog import *
from Particles.ParticleEmitter import *

class Game:
    def __init__(self):
        pygame.init()
        self.player = Mog(pygame.Vector2(20, 20))
        self.font = pygame.font.SysFont(None, 82)


    def update(self, elapsedTime, pressedKeys):
        self.player.update(elapsedTime, pressedKeys)


    def draw(self, displaySurface):
        # background
        displaySurface.fill((52,125,25))

        # player
        self.player.draw(displaySurface)