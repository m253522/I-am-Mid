import pygame


class Enemy:
    """Class for enemy objects"""

    def __init__(self):
        self.image = pygame.image.load('images/Dant.png')
        self.rect = self.image.get_rect()
        self.speed = 10


