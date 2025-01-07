class Animation:
    def __init__(self, frames, timePerFrame):
        self.frames = frames
        self.timePerFrame = timePerFrame
        self.frameIndex = 0
        self.timeSinceLastFrame = 0


    def update(self, elapsedTime):
        self.timeSinceLastFrame += elapsedTime
        if self.timeSinceLastFrame > self.timePerFrame:
            self.frameIndex = (self.frameIndex + 1) % len(self.frames)
            self.timeSinceLastFrame = 0
            

    def draw(self, displaysurface, pos):
        displaysurface.blit(self.frames[self.frameIndex], pos)