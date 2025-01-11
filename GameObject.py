import pygame

class GameObject(pygame.sprite.Sprite):
    
    def __init__(self, pos, size):
        super().__init__()
        self.pos = pos
        self.size = size

    def loadFrames(self, spritesheet, frameWidth, frameHeight, numFrames):
        frames = []
        for i in range(numFrames):
            # Calculate the x, y, width, and height of each frame
            frameX = i * frameWidth
            frame = spritesheet.subsurface((frameX, 0, frameWidth, frameHeight))
            frames.append(frame)
        return frames