import pygame, pygame.math
from GameObject import *

class Projectile(GameObject):

    SIZE = 8

    def __init__(self, pos):
        super().__init__(pos, pygame.Vector2(Projectile.SIZE, Projectile.SIZE))

    def hit(self):
        pass