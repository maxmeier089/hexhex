import pygame
from Config import *
from Player import *
from Animation import *
from Players.Mog import *
from Particles.Emitter import *

class Game:
    def __init__(self):
        pygame.init()
        self.players = pygame.sprite.Group()

        player1 = Mog(pygame.Vector2(SCREEN_WIDTH-20-32, SCREEN_HEIGHT-20-32))
        self.players.add(player1)

        player2 = Mog(pygame.Vector2(20, 20))
        player2.setKeys(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_LCTRL)
        self.players.add(player2)

        self.font = pygame.font.SysFont(None, 82)


    def update(self, elapsedTime, pressedKeys):
        for p in self.players:
            p.update(elapsedTime, pressedKeys)


    def draw(self, displaySurface):
        # background
        displaySurface.fill((52,125,25))
        #displaySurface.fill((30,121,127))

        # player
        for p in self.players:
            p.draw(displaySurface)