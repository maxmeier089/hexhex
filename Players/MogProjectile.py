from SpinProjectile import *


class MogProjectile(SpinProjectile):
    
    def __init__(self, pos):
        super().__init__(pos, "Players\Mog\MogProjectile.png", "Players\Mog\MogExplosion.png", (60, 242, 255), (255, 255, 255))
        