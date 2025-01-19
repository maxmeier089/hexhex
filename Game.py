import pygame
from Config import *
from Player import *
from Animation import *
from Players.Mog import Mog
from Players.Zarvo import Zarvo
from Particles.Emitter import *
from Stages.Volcano import Volcano

class Game:

    def __init__(self):

        self.stage = Volcano()
        
        self.players = pygame.sprite.Group()

        player1 = Mog(pygame.Vector2(40, SCREEN_HEIGHT/2 - 16))
        self.players.add(player1)

        player2 = Zarvo(pygame.Vector2(SCREEN_WIDTH-40-32, SCREEN_HEIGHT/2 - 16))
        player2.makePlayer2()
        self.players.add(player2)

        self.mainFont = pygame.font.Font("Content/m3x6.ttf", 48)
        self.mainText = ""

        self.secondaryFont = pygame.font.Font("Content/m3x6.ttf", 16)
        self.secondaryText = ""

        self.timeFont = pygame.font.Font("Content/m3x6.ttf", 16)
        self.timeText = "0"

        self.isRunning = True
        self.endSequenceOver = False

        self.totalTime = 0.0
        self.totalEndTime = 0.0

        #self.emitter = PixelEmitter(Vector2(100,100), Vector2(0.5,0.5), 200, 1000, (245,45,23))
        #self.emitter.angleSpeed = 0
        #self.emitter.randomizeAngle = True
        #self.emitter.on = True


    def update(self, elapsedTime, pressedKeys):

        if self.isRunning:
            self.totalTime += elapsedTime
        else:
            self.totalEndTime += elapsedTime
            if self.totalEndTime > 5000:
                self.endSequenceOver = True
                self.secondaryText = "- press fire to continue -"

        for p in self.players:
            p.update(elapsedTime, pressedKeys)

            for o in self.stage.obstacles:
                if p.collidesWith(o):
                    # player collides with obstacle
                    p.pos = p.lastPos

                for pr in p.projectiles:
                    if pr.collidesWith(o):
                        # projectile collides with obstacle
                        pr.pos = pr.lastPos
                        pr.hit()

            
        for playerA in self.players:

            allOthersDead = True

            for playerB in self.players:

                if playerA != playerB:

                    if playerB.isAlive:
                        allOthersDead = False

                    if playerA.collidesWith(playerB):
                        # player collides with player
                        playerA.pos = playerA.lastPos
                        playerB.pos = playerB.lastPos

                    for projectileB in playerB.projectiles:

                        if projectileB.hitboxActive and playerA.collidesWith(projectileB):
                            # collision between projectile and player
                            projectileB.explode()
                            playerA.hit(projectileB.getImpact())                       
                            
                        for projectileA in playerA.projectiles:
                            if projectileA.hitboxActive and projectileB.hitboxActive and projectileA.collidesWith(projectileB):
                                # collision between two projectiles
                                projectileA.explode()
                                projectileB.explode()

            if allOthersDead:
                playerA.win()
                self.isRunning = False
                self.mainText = "Player " + str(playerA.playerNumber) + " wins!"

            self.timeText = str((int)(self.totalTime/1000.0))


        #self.emitter.update(Vector2(100,100), elapsedTime)


    def draw(self, displaySurface):
        # background
        #displaySurface.fill((52,125,25))
        #displaySurface.fill((34,98,12))
        #displaySurface.fill((125,12,225))
        #displaySurface.fill((125,12,25))
        #displaySurface.fill((30,121,127))

        self.stage.draw(displaySurface, Vector2(0, 0))

        # players
        for p in self.players:
            p.draw(displaySurface)

        # projectiles
        for p in self.players:
            p.drawProjectiles(displaySurface)

        # healthbars
        for p in self.players:
            p.drawHealthbar(displaySurface)

        if not self.isRunning:
            mainTextPos = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 16)
            mainTextSurface = self.mainFont.render(self.mainText, True, GOLD)
            displaySurface.blit(mainTextSurface, mainTextSurface.get_rect(center=mainTextPos))

            if self.endSequenceOver:
                secondaryTextPos = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 16)
                secondaryTextSurface = self.secondaryFont.render(self.secondaryText, True, GOLD)
                displaySurface.blit(secondaryTextSurface, secondaryTextSurface.get_rect(center=secondaryTextPos))

        timeTextPos = (SCREEN_WIDTH/2, 6)
        timeTextSurface = self.timeFont.render(self.timeText, True, GOLD)
        displaySurface.blit(timeTextSurface, timeTextSurface.get_rect(center=timeTextPos))

        # if random.randint(0,10) == 5:
        #     for p in self.players:
        #         p.health -= 1
        #self.emitter.draw(displaySurface)