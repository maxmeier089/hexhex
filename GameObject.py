import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos

    def loadFrames(self, spritesheet, frameWidth, frameHeight, numFrames):
        frames = []
        for i in range(numFrames):
            # Calculate the x, y, width, and height of each frame
            frameX = i * frameWidth
            frame = spritesheet.subsurface((frameX, 0, frameWidth, frameHeight))
            frames.append(frame)
        return frames