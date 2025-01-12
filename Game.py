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

        player1 = Mog(pygame.Vector2(SCREEN_WIDTH-52, SCREEN_HEIGHT-52))
        self.players.add(player1)

        player2 = Mog(pygame.Vector2(20, 20))
        player2.setKeys(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_LCTRL)
        self.players.add(player2)

        self.font = pygame.font.SysFont(None, 82)

        #self.emitter = PixelEmitter(Vector2(100,100), Vector2(0.5,0.5), 200, 1000, (245,45,23))
        #self.emitter.angleSpeed = 0
        #self.emitter.randomizeAngle = True
        #self.emitter.on = True


    def update(self, elapsedTime, pressedKeys):
        for p in self.players:
            p.update(elapsedTime, pressedKeys)
        #self.emitter.update(Vector2(100,100), elapsedTime)


    def draw(self, displaySurface):
        # background
        #displaySurface.fill((34,98,12))
        #displaySurface.fill((125,12,225))
        #displaySurface.fill((125,12,25))
        displaySurface.fill((52,125,25))
        #displaySurface.fill((30,121,127))

        # player
        for p in self.players:
            p.draw(displaySurface)

        #self.emitter.draw(displaySurface)