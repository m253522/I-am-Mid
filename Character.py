import pygame


class Mid:
    """Make main character object"""
    def __init__(self):
        self.image = pygame.image.load('images/Character.png')
        self.rect = self.image.get_rect()

    def moveUp(self):
        self.rect.y = self.rect.y + 1
