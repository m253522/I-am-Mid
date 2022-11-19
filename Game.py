import pygame
import sys
from Character import Mid

# Initialize pygame
pygame.init()


# Make screen/display
def UpdateScreen():
    screen.fill((50, 100, 50))


(width, height) = (600, 600)
screen = pygame.display.set_mode((width, height))

UpdateScreen()
screen_rect = screen.get_rect()
pygame.display.set_caption("My game")

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
                My_character.rect.y = My_character.rect.y - 10
                UpdateScreen()
            if event.key == pygame.K_DOWN:
                My_character.rect.y = My_character.rect.y + 10
                UpdateScreen()
            if event.key == pygame.K_RIGHT:
                My_character.rect.x = My_character.rect.x + 10
                UpdateScreen()
            if event.key == pygame.K_LEFT:
                My_character.rect.x = My_character.rect.x - 10
                UpdateScreen()

