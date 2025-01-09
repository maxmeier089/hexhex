import pygame
from pygame.math import *
from Config import *
from Game import *
from Player import *
from Animation import *
from Players.Mog import *


# Initialize Pygame
pygame.init()

# Scaled window resolution
WINDOW_WIDTH = SCREEN_WIDTH * SCALE_FACTOR
WINDOW_HEIGHT = SCREEN_HEIGHT * SCALE_FACTOR

# Create the render surface
displaySurface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

# Set up the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("<>")

# Animation variables
clock = pygame.time.Clock()
lastUpdateTime = pygame.time.get_ticks()
running = True


# Create Game
game = Game()

# Run!
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


    clock.tick(FPS)


pygame.quit()
