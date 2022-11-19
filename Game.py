import pygame
import sys
from Character import Mid
from Background import BgScreen

# Initialize pygame
pygame.init()

# Make screen/display
# https://stackoverflow.com/questions/19954469/how-to-get-the-resolution-of-a-monitor-in-pygame

(width, height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode((width, height))
screen_rect = screen.get_rect()
pygame.display.set_caption("My game")

# Make levels from background.py class
level = BgScreen(screen, width, height)

# Function that updates the screen when needed
def UpdateScreen():
    screen.fill((50, 100, 50))
    level.drawLevel1()

UpdateScreen()

# My character
My_character = Mid()
My_character.rect.midbottom = screen_rect.midbottom
screen.blit(My_character.image, My_character.rect)

# The infinite loop
while True:
    recent_events = pygame.event.get()
    screen.blit(My_character.image, My_character.rect)
    pygame.display.flip()
    for event in recent_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                My_character.moveUp()
                UpdateScreen()
            if event.key == pygame.K_DOWN:
                My_character.moveDown()
                UpdateScreen()
            if event.key == pygame.K_RIGHT:
                My_character.moveRight()
                UpdateScreen()
            if event.key == pygame.K_LEFT:
                My_character.moveLeft()
                UpdateScreen()
