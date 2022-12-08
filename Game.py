import pygame
import sys
from Character import Mid
from Background import BgScreen
from Antagonist import Enemy
import time

# Initialize pygame and general variables
pygame.init()
startGame = False
clock = pygame.time.Clock()
Score = 0

# Play music and initialize sound variables
deathSound = pygame.mixer.Sound('sounds/oof.wav')
deathSound.set_volume(30)
scoreSound = pygame.mixer.Sound('sounds/score.wav')
winSound = pygame.mixer.Sound('sounds/win.wav')
loseSound = pygame.mixer.Sound('sounds/lose.wav')
pygame.mixer.music.set_volume(.25)

# Make screen/display
# https://stackoverflow.com/questions/19954469/how-to-get-the-resolution-of-a-monitor-in-pygame

(width, height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode((width, height))
screen_rect = screen.get_rect()
pygame.display.set_caption("I am Mid")

winScreen = pygame.image.load('images/YouWin.png')
winScreenRect = winScreen.get_rect()
winScreenRect.center = screen_rect.center

# Make levels from background.py class
level = BgScreen(screen, width, height)

# My character
My_character = Mid(screen, width, height)
My_character.rect.midbottom = screen_rect.midbottom

# If the player reaches the other side of stribling, add a point.
if My_character.rect[1] < 100:
    Score += 1

# Common goon marine enemy
Marine1_1 = Enemy('images/marine.png', screen, screen_rect, -200, 170, 5)
Marine1_2 = Enemy('images/marine.png', screen, screen_rect, -120, 350, 5)
Marine1_3 = Enemy('images/marine.png', screen, screen_rect, -420, 420, 5)

# Display Main Menu
level.drawMainMenu()


# Draws the character on the screen
def UpdateScreen():
    if startGame:
        # This makes it possible to use the score variable in the function
        global Score
        global deathSound

        # Creates background color
        screen.fill((50, 100, 50))

        # Load the level picture and load the enemies
        level.drawLevel1()
        Marine1_1.LoadLevel1Entity()
        Marine1_2.LoadLevel1Entity()
        Marine1_3.LoadLevel1Entity()

        # Draw the player and update its movement
        clock.tick(100)
        screen.blit(My_character.image, My_character.rect)
        My_character.updateMovement()

        # Collision detection with enemy
        collide = pygame.Rect.colliderect(Marine1_1.rect, My_character.rect) \
                  or pygame.Rect.colliderect(Marine1_2.rect,
                                             My_character.rect) or pygame.Rect.colliderect(
            Marine1_3.rect, My_character.rect)

        # If you die, reset score and position
        if collide:
            My_character.rect = screen_rect.midbottom
            pygame.mixer.Sound.play(deathSound)
            Score = 0

        # If player makes it across, add score by one and reset position
        if My_character.rect[1] < 100:
            My_character.rect = screen_rect.midbottom
            Score += 1
            pygame.mixer.Sound.play(scoreSound)

        # If score reaches ten, win condition is met and the win screen
        # is displayed along with music and the end of the application.
        if Score == 10:
            screen.fill((0, 0, 0))
            screen.blit(winScreen, winScreenRect)
            pygame.mixer.Sound.play(winSound)
            pygame.display.flip()
            time.sleep(9)
            sys.exit()


# The infinite loop
while True:
    # Get recent events in the loop
    recent_events = pygame.event.get()
    # Call the update screen function
    UpdateScreen()
    # Continually flip the screen
    pygame.display.flip()
    # Xander Spees helped with the mouse variable
    mouse = pygame.mouse.get_pos()
    # Game events
    for event in recent_events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                My_character.upPressed = True
            if event.key == pygame.K_DOWN:
                My_character.downPressed = True
            if event.key == pygame.K_RIGHT:
                My_character.rightPressed = True
            if event.key == pygame.K_LEFT:
                My_character.leftPressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                My_character.upPressed = False
            if event.key == pygame.K_DOWN:
                My_character.downPressed = False
            if event.key == pygame.K_RIGHT:
                My_character.rightPressed = False
            if event.key == pygame.K_LEFT:
                My_character.leftPressed = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the mouse is clicked in the position of the start button then the game starts
            if (mouse[0] > 603) & (mouse[0] < 678) & (mouse[1] > 344) & (mouse[1] < 376):
                startGame = True
                # Play music if game is started
                pygame.mixer.music.load('sounds/Theme.wav')
                pygame.mixer.music.play(-1)
