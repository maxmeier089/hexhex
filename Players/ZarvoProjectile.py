from SpinProjectile import *


class ZarvoProjectile(SpinProjectile):

    def __init__(self, pos):
        super().__init__(pos, "Players\Zarvo\ZarvoProjectile.png", "Players\Zarvo\ZarvoExplosion.png", (194, 92, 60), (0, 0, 0))
        