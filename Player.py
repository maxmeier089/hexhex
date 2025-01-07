import pygame, pygame.math

class Player(pygame.sprite.Sprite):
    def __init__(self, name, health, speed, pos, standAnimation, standShootAnimation, walkAnimation, walkShootAnimation):
        super().__init__()
        self.name = name
        self.health = health
        self.speed = speed
        self.pos = pos
        self.firePressed = False
        self.firePressedTime = 0
        self.standAnimation = standAnimation
        self.standShootAnimation = standShootAnimation
        self.walkAnimation = walkAnimation
        self.walkShootAnimation = walkShootAnimation
        self.currentAnimation = standAnimation

    def fireDown(self):
        pass

    def fireHold(self, elapsedTime):
        pass

    def fireRelease(self, elapsedTime):
        pass
        

    def update(self, elapsedTime, pressedKeys):

        move = pygame.Vector2(0,0)

        if pressedKeys[pygame.K_UP]:
            move.y -= 1
        if pressedKeys[pygame.K_DOWN]:
            move.y += 1
        if pressedKeys[pygame.K_LEFT]:
            move.x -= 1
        if pressedKeys[pygame.K_RIGHT]:
            move.x += 1

        if pressedKeys[pygame.K_RCTRL]: # FIRE pressed
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


    def loadFrames(self, spritesheet, frameWidth, frameHeight, numFrames):
        frames = []
        for i in range(numFrames):
            # Calculate the x, y, width, and height of each frame
            frameX = i * frameWidth
            frame = spritesheet.subsurface((frameX, 0, frameWidth, frameHeight))
            frames.append(frame)
        return frames
