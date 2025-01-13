import pygame

class GameObject(pygame.sprite.Sprite):
    
    def __init__(self, pos, size):
        super().__init__()
        self.pos = pos
        self.size = size
        self.children = pygame.sprite.Group()
        self.hitbox = pygame.Rect(0, 0, self.size.x, self.size.y)
        self.drawHitbox = True

    def loadFrames(self, spritesheet, frameWidth, frameHeight, numFrames):
        frames = []
        for i in range(numFrames):
            # Calculate the x, y, width, and height of each frame
            frameX = i * frameWidth
            frame = spritesheet.subsurface((frameX, 0, frameWidth, frameHeight))
            frames.append(frame)
        return frames
    
    def update(self, elapsedTime):
        for child in self.children:
            child.update(elapsedTime)

    def draw(self, displaySurface):
        if self.drawHitbox:
            pygame.draw.rect(displaySurface, (255,0,255), self.hitbox.move(self.pos), width=1)

        for child in self.children:
            child.draw(displaySurface)