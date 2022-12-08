import pygame


class Mid:
    """Make main character object and initialize attributes"""

    def __init__(self, surface, width, height):
        self.image = pygame.image.load('images/Character.png')
        self.rect = self.image.get_rect()
        self.velocityX = 0
        self.velocityY = 0
        self.speed = 2
        self.upPressed = False
        self.downPressed = False
        self.leftPressed = False
        self.rightPressed = False
        self.surface = surface
        self.width = width
        self.height = height

    def updateMovement(self):
        # Smooth movement for the playable character
        # https://github.com/nas-programmer/youtube-tutorials/blob/main/Smooth_movement.py
        self.velocityX = 0
        self.velocityY = 0
        if self.leftPressed:
            self.velocityX = -self.speed
        if self.rightPressed:
            self.velocityX = self.speed
        if self.upPressed:
            self.velocityY = -self.speed
        if self.downPressed:
            self.velocityY = self.speed

        # Convert tuple into list in order to edit it
        self.rect = list(self.rect)

        # Create boundaries for character in level space.
        if self.rect[0] >= (self.width - 50):
            self.rect[0] -= 1
        elif self.rect[0] <= 0:
            self.rect[0] += 1
        elif self.rect[1] >= (self.height - 50):
            self.rect[1] -= 1
        elif self.rect[1] <= 0:
            self.rect[1] += 1

        self.rect[0] += self.velocityX
        self.rect[1] += self.velocityY

        # Convert list back into tuple
        self.rect = tuple(self.rect)
        self.rect = pygame.Rect([(self.rect[0]), (self.rect[1])], (self.image.get_width(), self.image.get_height()))
