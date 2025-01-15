import pygame

class GameObject(pygame.sprite.Sprite):
    
    def __init__(self, pos, size):
        super().__init__()
        self.pos = pos
        self.lastPos = pos
        self.size = size
        self.children = pygame.sprite.Group()
        self.hitboxShape = pygame.Rect(0, 0, self.size.x, self.size.y)
        self.hitbox = self.hitboxShape.move(self.pos)
        self.hitboxActive = True
        self.drawHitbox = False     

    def loadFrames(self, spritesheet, frameWidth, frameHeight, numFrames):
        frames = []
        for i in range(numFrames):
            # Calculate the x, y, width, and height of each frame
            frameX = i * frameWidth
            frame = spritesheet.subsurface((frameX, 0, frameWidth, frameHeight))
            frames.append(frame)
        return frames
    
    def collidesWith(self, other):
        return self.hitbox.colliderect(other.hitbox)
    
    def update(self, elapsedTime):
        self.hitbox = self.hitboxShape.move(self.pos)
        for child in self.children:
            child.update(elapsedTime)

    def draw(self, displaySurface):
        if self.drawHitbox and self.hitboxActive:
            pygame.draw.rect(displaySurface, (255,0,255), self.hitbox, width=1)

        for child in self.children:
            child.draw(displaySurface)