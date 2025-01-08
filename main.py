import pygame
from pygame.math import *
from Game import *
from Player import *
from Animation import *
from Players.Mog import *

# Initialize Pygame
pygame.init()

# Original render resolution
RENDER_WIDTH = 256
RENDER_HEIGHT = 240
SCALE_FACTOR = 8  # Scale factor for the window

# Scaled window resolution
WINDOW_WIDTH = RENDER_WIDTH * SCALE_FACTOR
WINDOW_HEIGHT = RENDER_HEIGHT * SCALE_FACTOR

# Create the render surface
displaySurface = pygame.Surface((RENDER_WIDTH, RENDER_HEIGHT), pygame.SRCALPHA)

# Set up the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("<>")


# Create Game
game = Game()
#p1 = Mog(Vector2(20, 20))

# Animation variables
clock = pygame.time.Clock()
lastUpdateTime = pygame.time.get_ticks()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # READ INPUT
    pressedKeys = pygame.key.get_pressed()


    # UPDATE
    currentTime = pygame.time.get_ticks()
    elapsedTime = currentTime - lastUpdateTime
    game.update(elapsedTime, pressedKeys)
    lastUpdateTime = currentTime


    # DRAW
    game.draw(displaySurface)


    # Scale the render surface to the window size
    scaledDisplaySurface = pygame.transform.scale(displaySurface, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Draw the scaled surface to the screen
    screen.blit(scaledDisplaySurface, (0, 0))

    pygame.display.flip()


    clock.tick(60)


pygame.quit()
