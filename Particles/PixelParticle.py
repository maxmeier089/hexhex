from Particle import *

class PixelParticle(Particle):
    def __init__(self, pos, speed, timeToLive, startColor, endColor):
        super().__init__(pos, speed, timeToLive)
        self.startColor = startColor
        self.endColor = endColor
        self.color = startColor

    def interpolate(self, start, end, scale):
        distance = end - start
        progress = distance * scale
        current = start + progress
        return current


    def update(self, elapsedTime):
        super().update(elapsedTime)

        scale = 1 - ((self.timeToLive - self.timeAlreadyLived) / self.timeToLive)

        r = self.interpolate(self.startColor[0], self.endColor[0], scale)
        g = self.interpolate(self.startColor[1], self.endColor[1], scale)
        b = self.interpolate(self.startColor[2], self.endColor[2], scale)

        self.color = (r, g, b)
    
    def draw(self, displaySurface):
        pygame.draw.line(displaySurface, self.color, self.pos, self.pos) 

