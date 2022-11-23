import pygame


class Enemy:
    """Class for enemy objects"""

    def __init__(self, imageSelection):
        self.image = pygame.image.load(imageSelection)
        self.rect = self.image.get_rect()
        self.speed = 1

    def moveRight(self):
        self.rect.x += self.speed

    def moveLeft(self):
        self.rect.x -= self.speed
