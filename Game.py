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

        player1 = Mog(pygame.Vector2(40, SCREEN_HEIGHT/2))
        self.players.add(player1)

        player2 = Mog(pygame.Vector2(SCREEN_WIDTH-40-32, SCREEN_HEIGHT/2))
        player2.makePlayer2()
        self.players.add(player2)

        self.font = pygame.font.SysFont(None, 82)

        #self.emitter = PixelEmitter(Vector2(100,100), Vector2(0.5,0.5), 200, 1000, (245,45,23))
        #self.emitter.angleSpeed = 0
        #self.emitter.randomizeAngle = True
        #self.emitter.on = True


    def update(self, elapsedTime, pressedKeys):
        for p in self.players:
            p.update(elapsedTime, pressedKeys)

        for p in self.players:
            for p2 in self.players:
                if p != p2:
                    for pr in p2.projectiles:
                        if pr.hitboxActive and p.collidesWith(pr):
                            p.health -= 0.1 + pr.power * 0.1
                            pr.explode()


        #self.emitter.update(Vector2(100,100), elapsedTime)


    def draw(self, displaySurface):
        # background
        #displaySurface.fill((34,98,12))
        #displaySurface.fill((125,12,225))
        #displaySurface.fill((125,12,25))
        displaySurface.fill((52,125,25))
        #displaySurface.fill((30,121,127))

        # players
        for p in self.players:
            p.draw(displaySurface)

        # projectiles
        for p in self.players:
            p.drawProjectiles(displaySurface)

        # healthbars
        for p in self.players:
            p.drawHealthbar(displaySurface)

        # if random.randint(0,10) == 5:
        #     for p in self.players:
        #         p.health -= 1
        #self.emitter.draw(displaySurface)