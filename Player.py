import pygame, pygame.math
from GameObject import *

class Player(GameObject):

    SIZE = 32

    def __init__(self, name, health, speed, pos, standAnimation, standShootAnimation, walkAnimation, walkShootAnimation):
        super().__init__(pos, pygame.Vector2(Player.SIZE, Player.SIZE))
        self.name = name
        self.health = health
        self.speed = speed
        self.firePressed = False
        self.firePressedTime = 0
        self.standAnimation = standAnimation
        self.standShootAnimation = standShootAnimation
        self.walkAnimation = walkAnimation
        self.walkShootAnimation = walkShootAnimation
        self.currentAnimation = standAnimation
        self.setKeys(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RCTRL)

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
        

    def update(self, elapsedTime, pressedKeys):

        move = pygame.Vector2(0,0)

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

        self.pos += move

        self.currentAnimation.update(elapsedTime)


    def draw(self, displaySurface):
        self.currentAnimation.draw(displaySurface, self.pos)
