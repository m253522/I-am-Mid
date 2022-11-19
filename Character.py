import pygame


class Mid:
    """Make main character object"""

    def __init__(self):
        self.image = pygame.image.load('images/Character.png')
        self.rect = self.image.get_rect()
        self.speed = 50

    def moveDown(self):
        self.rect.y += self.speed

    def moveUp(self):
        self.rect.y -= self.speed

    def moveRight(self):
        self.rect.x += self.speed

    def moveLeft(self):
        self.rect.x -= self.speed
