class Animation:
    
    def __init__(self, frames, timePerFrame):
        self.frames = frames
        self.timePerFrame = timePerFrame
        self.frameIndex = 0
        self.timeSinceLastFrame = 0
        self.startIndex = 0
        self.endIndex = len(self.frames) - 1
        self.pendulum = False
        self.up = True


    def update(self, elapsedTime):
        self.timeSinceLastFrame += elapsedTime

        if self.timeSinceLastFrame > self.timePerFrame:
            
            if self.up: 
                if self.frameIndex < self.endIndex:
                    self.frameIndex += 1
                else:
                    if self.pendulum:
                        self.up = False
                        self.frameIndex -= 1
                        if self.frameIndex < self.startIndex:
                            self.frameIndex = self.startIndex
                    else:
                        self.frameIndex = self.startIndex      
            else:
                if self.frameIndex > self.startIndex:
                    self.frameIndex -= 1
                else:
                    if self.pendulum:
                        self.up = True
                        self.frameIndex += 1
                        if self.frameIndex > self.endIndex:
                            self.frameIndex = self.endIndex
                    else:
                        self.frameIndex = self.startIndex 
        
            self.timeSinceLastFrame = 0
            

    def draw(self, displaysurface, pos):
        displaysurface.blit(self.frames[self.frameIndex], pos)