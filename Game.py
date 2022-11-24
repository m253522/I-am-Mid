import pygame
import sys
from Character import Mid
from Background import BgScreen
from Antagonist import Enemy

# Initialize pygame and general variables
pygame.init()

clock = pygame.time.Clock()

# Make screen/display
# https://stackoverflow.com/questions/19954469/how-to-get-the-resolution-of-a-monitor-in-pygame

(width, height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode((width, height))
screen_rect = screen.get_rect()
pygame.display.set_caption("I am Mid")

# Make levels from background.py class
level = BgScreen(screen, width, height)

# My character
My_character = Mid()
My_character.rect.midbottom = screen_rect.midbottom

# Final Boss
# Dant = Enemy('images/Dant.png')

# Common goon marine enemy
Marine1_1 = Enemy('images/marine.png', screen, screen_rect, 200, 120, 5)
Marine1_2 = Enemy('images/marine.png', screen, screen_rect, 500, 200, 5)
Marine1_3 = Enemy('images/marine.png', screen, screen_rect, 250, 380, 5)


# def LoadBoss():
# screen.blit(Dant, Dant.rect)
# if Dant.rect.right != screen_rect.right:
# Dant.moveRight()


# Function that updates the screen when needed
def UpdateScreen():
    screen.fill((50, 100, 50))
    screen.blit(My_character.image, My_character.rect)
    level.drawMainMenu()

    # level.drawLevel1()
    # Marine1_1.LoadLevel1Entity()
    # Marine1_2.LoadLevel1Entity()
    # Marine1_3.LoadLevel1Entity()


# The infinite loop
while True:
    recent_events = pygame.event.get()
    pygame.display.flip()
    clock.tick(100)
    UpdateScreen()
    # My_character.updateMovement()
    for event in recent_events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                My_character.upPressed = True
                UpdateScreen()
            if event.key == pygame.K_DOWN:
                My_character.downPressed = True
                UpdateScreen()
            if event.key == pygame.K_RIGHT:
                My_character.rightPressed = True
                UpdateScreen()
            if event.key == pygame.K_LEFT:
                My_character.leftPressed = True
                UpdateScreen()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                My_character.upPressed = False
                UpdateScreen()
            if event.key == pygame.K_DOWN:
                My_character.downPressed = False
                UpdateScreen()
            if event.key == pygame.K_RIGHT:
                My_character.rightPressed = False
                UpdateScreen()
            if event.key == pygame.K_LEFT:
                My_character.leftPressed = False
                UpdateScreen()
