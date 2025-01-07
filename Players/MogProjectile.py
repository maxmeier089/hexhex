from Projectile import *


class MogProjectile(Projectile):
    def __init__(self, pos, vel):
        super().__init__(pos)
        self.vel = vel
        self.frames = self.loadFrames(pygame.image.load("Players\Mog\MogProjectile.png").convert_alpha(), 16, 16, 17)
        

    def update(self, elapsedTime):
        self.pos += self.vel

