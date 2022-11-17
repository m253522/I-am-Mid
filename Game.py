import pygame
import sys

# Initialize pygame
pygame.init()

# Make screen/display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill((0, 0, 0))

# The True loop
while True:
    pygame.display.flip()
    recent_events = pygame.event.get()
    for event in recent_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
