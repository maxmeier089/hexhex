import pygame, pygame.math

class Player(pygame.sprite.Sprite):
    def __init__(self, name, health, speed, pos, idleAnimation, walkAnimation):
        super().__init__()
        self.name = name
        self.health = health
        self.speed = speed
        self.pos = pos
        self.idleAnimation = idleAnimation
        self.walkAnimation = walkAnimation
        self.currentAnimation = idleAnimation
        

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

        if move.length() > 0:
            # walking
            move.scale_to_length(self.speed)
            self.currentAnimation = self.walkAnimation
        else:
            # idle
            self.currentAnimation = self.idleAnimation

        self.pos += move

        self.currentAnimation.update(elapsedTime)


    def draw(self, displaysurface):
        self.currentAnimation.draw(displaysurface, self.pos)


    def loadFrames(self, spritesheet, frameWidth, frameHeight, numFrames):
        frames = []
        for i in range(numFrames):
            # Calculate the x, y, width, and height of each frame
            frameX = i * frameWidth
            frame = spritesheet.subsurface((frameX, 0, frameWidth, frameHeight))
            frames.append(frame)
        return frames
