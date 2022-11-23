import pygame


class Mid:
    """Make main character object and initialize attributes"""

    def __init__(self):
        self.image = pygame.image.load('images/Character.png')
        self.rect = self.image.get_rect()
        self.velocityX = 0
        self.velocityY = 0
        self.speed = 1
        self.upPressed = False
        self.downPressed = False
        self.leftPressed = False
        self.rightPressed = False

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

        self.rect.x += self.velocityX
        self.rect.y += self.velocityY
