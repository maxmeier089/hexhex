import pygame, pygame.math
from pygame import Vector2
from Config import *
from GameObject import *

class Player(GameObject):

    SIZE = 32

    def __init__(self, name, health, speed, pos, standAnimation, standShootAnimation, walkAnimation, walkShootAnimation, winAnimation, deadAnimation):
        super().__init__(pos, Vector2(Player.SIZE, Player.SIZE))
        self.name = name
        self.playerNumber = 1
        self.isAlive = True
        self.isWinner = False
        self.health = health
        self.maxHealth = self.health
        self.speed = speed
        self.firePressed = False
        self.firePressedTime = 0
        self.projectiles = pygame.sprite.Group()
        self.standAnimation = standAnimation
        self.standShootAnimation = standShootAnimation
        self.walkAnimation = walkAnimation
        self.walkShootAnimation = walkShootAnimation
        self.winAnimation = winAnimation
        self.deadAnimation = deadAnimation
        self.currentAnimation = standAnimation
        self.setKeys(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_LCTRL)
        self.healthBarX = HEALTHBAR_MARGIN
        self.healthBarY = HEALTHBAR_MARGIN
        self.healthBarColor = (255,255,255)

    def makePlayer2(self):
        self.playerNumber = 2
        self.setKeys(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RCTRL)
        self.healthBarX = SCREEN_WIDTH - HEALTHBAR_MARGIN - HEALTHBAR_WIDTH
        self.healthBarY = HEALTHBAR_MARGIN

    def fireDown(self):
        pass

    def fireHold(self, elapsedTime):
        pass

    def fireRelease(self, elapsedTime):
        pass


    def setKeys(self, up, down, left, right, fire):
        self.upKey = up
        self.downKey = down
        self.leftKey = left
        self.rightKey = right
        self.fireKey = fire


    def hit(self, impact):
        self.health -= impact
        if self.health <= 0.0:
            self.isAlive = False
            self.currentAnimation = self.deadAnimation
            self.health = 0.0

    def win(self):
        self.isWinner = True
        self.currentAnimation = self.winAnimation
        

    def update(self, elapsedTime, pressedKeys):
        move = Vector2(0,0)

        if self.isAlive and not self.isWinner:
            if pressedKeys[self.upKey]:
                move.y -= 1
            if pressedKeys[self.downKey]:
                move.y += 1
            if pressedKeys[self.leftKey]:
                move.x -= 1
            if pressedKeys[self.rightKey]:
                move.x += 1

            if pressedKeys[self.fireKey]: # FIRE pressed
                if self.firePressed: # was pressed before
                    self.firePressedTime += elapsedTime
                    self.fireHold(self.firePressedTime)
                else: # was not pressed before, new press
                    self.firePressed = True
                    self.fireDown()
            else: # FIRE not pressed
                if self.firePressed: # was pressed before, release
                    self.firePressed = False
                    self.firePressedTime += elapsedTime
                    self.fireRelease(self.firePressedTime)
                    self.firePressedTime = 0
                # else: was not pressed before, nothing changes

            if move.length() > 0:
                # walk
                move.scale_to_length(self.speed)
                if self.firePressed:
                    self.currentAnimation = self.walkShootAnimation
                else:
                    self.currentAnimation = self.walkAnimation
            else:
                # stand
                if self.firePressed:
                    self.currentAnimation = self.standShootAnimation
                else:
                    self.currentAnimation = self.standAnimation

            self.lastPos = self.pos.copy()

            self.pos += move

        for projectile in self.projectiles:
            projectile.update(elapsedTime)

        self.currentAnimation.update(elapsedTime)

        super().update(elapsedTime)


    def draw(self, displaySurface):
        self.currentAnimation.draw(displaySurface, self.pos)
        super().draw(displaySurface)

    def drawProjectiles(self, displaySurface):
        for projectile in self.projectiles:
            projectile.draw(displaySurface)

    def drawHealthbar(self, displaySurface):
        currentBarWidth = (self.health / self.maxHealth) * HEALTHBAR_WIDTH
        pygame.draw.rect(displaySurface, RED, (self.healthBarX, self.healthBarY, HEALTHBAR_WIDTH, HEALTHBAR_HEIGHT), border_radius=3)
        pygame.draw.rect(displaySurface, self.healthBarColor, (self.healthBarX, self.healthBarY, currentBarWidth, HEALTHBAR_HEIGHT), border_radius=3)
        pygame.draw.rect(displaySurface, BLACK, (self.healthBarX, self.healthBarY, HEALTHBAR_WIDTH, HEALTHBAR_HEIGHT), width=1, border_radius=3)

