import random
import pygame, pygame.math
from pygame import Vector2
from Config import *

class Stage:
    def __init__(self, groundTiles):
        self.groundTiles = groundTiles

        self.rows = int(SCREEN_HEIGHT / 8)
        self.cols = int(SCREEN_WIDTH / 8)

        lst = []
        self.groundMatrix = []
        for _ in range(self.cols):
            for _ in range(self.rows):
                lst.append(random.randint(0, len(groundTiles)-1))
            self.groundMatrix.append(lst)
            lst = []

        self.name = "x"

        


    def draw(self, displaysurface, pos):
        for x in range(self.cols):
            for y in range(self.rows):
                tileNumber = self.groundMatrix[x][y]
                displaysurface.blit(self.groundTiles[tileNumber], Vector2(x * 8, y * 8))

    def loadTiles(self, path):
        spritesheet = pygame.image.load(path).convert_alpha()
        size = spritesheet.get_height()
        numTiles = int(spritesheet.get_width() / size)
        tiles = []
        for i in range(numTiles):
            tilesX = i * size
            tile = spritesheet.subsurface((tilesX, 0, size, size))
            tiles.append(tile)
        return tiles