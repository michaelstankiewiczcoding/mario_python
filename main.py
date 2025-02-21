import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    # Update game state (to be added)
    # Render (to be added)
    screen.fill((0, 0, 0))  # Clear screen with black
    pygame.display.flip()   # Update display
    clock.tick(60)          # 60 FPS

pygame.quit()
