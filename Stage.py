import random
import pygame, pygame.math
from pygame import Vector2
from Config import *
from Obstacle import Obstacle

class Stage:

    TILE_SIZE = 8

    def __init__(self, groundTiles):

        self.groundTiles = groundTiles

        self.obstacles = []
        topBorder = Obstacle(Vector2(0, 0), Vector2(SCREEN_WIDTH, 2))
        self.obstacles.append(topBorder)
        downBorder = Obstacle(Vector2(0, SCREEN_HEIGHT - 2), Vector2(SCREEN_WIDTH, 2))
        self.obstacles.append(downBorder)
        leftBorder = Obstacle(Vector2(0, 0), Vector2(2, SCREEN_HEIGHT))
        self.obstacles.append(leftBorder)
        rightBorder = Obstacle(Vector2(SCREEN_WIDTH - 2, 0), Vector2(2, SCREEN_HEIGHT))
        self.obstacles.append(rightBorder)
        
        

        self.rows = int(SCREEN_HEIGHT / Stage.TILE_SIZE)
        self.cols = int(SCREEN_WIDTH / Stage.TILE_SIZE)

        self.groundMatrix = []
        for _ in range(self.cols):
            currentColumn = []
            for _ in range(self.rows):
                currentColumn.append(random.randint(0, len(groundTiles) - 1))
            self.groundMatrix.append(currentColumn)    


    def draw(self, displaysurface, pos):
        for x in range(self.cols):
            for y in range(self.rows):
                tileNumber = self.groundMatrix[x][y]
                displaysurface.blit(self.groundTiles[tileNumber], Vector2(x * Stage.TILE_SIZE, y * Stage.TILE_SIZE))
        pygame.draw.rect(displaysurface, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), width=2)

                

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