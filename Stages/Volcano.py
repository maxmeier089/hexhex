from Stage import *

class Volcano(Stage):
    def __init__(self):
        groundTiles = self.loadTiles(r"Stages\Volcano\VolcanoGround.png")
        super().__init__(groundTiles)
        self.music = r"Stages\Volcano\vlc4n0.ogg"