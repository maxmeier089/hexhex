from pygame import Vector2
from Animation import *
from Projectile import *


class MogProjectile(Projectile):
    def __init__(self, pos):
        super().__init__(pos)
        self.vel = Vector2(0,0)
        self.frames = self.loadFrames(pygame.image.load("Players\Mog\MogProjectile.png").convert_alpha(), 16, 16, 7)
        self.animation = Animation(self.frames, 200)
        

    def update(self, elapsedTime):
        self.pos += self.vel * elapsedTime

    def draw(self, displaySurface):
        self.animation.draw(displaySurface, self.pos)

