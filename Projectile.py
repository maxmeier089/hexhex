import pygame, pygame.math
from GameObject import *

class Projectile(GameObject):
    def __init__(self, pos):
        super().__init__(pos)