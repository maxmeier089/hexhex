from Stage import *

class Volcano(Stage):
    def __init__(self):
        groundTiles = self.loadTiles("Stages\Volcano\VolcanoGround.png")
        super().__init__(groundTiles)