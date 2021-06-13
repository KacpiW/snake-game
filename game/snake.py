# %%
import os
import pygame

# Initialize all of the imported Pygame modules
pygame.init()

# Create a display surface and customize it
display = pygame.display.set_mode((400, 400))

pygame.display.update()
pygame.display.set_caption("Very Basic Snake Game")

game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event)

# Uninitialize all the imported modules and exit
pygame.quit()
quit()

# %%
