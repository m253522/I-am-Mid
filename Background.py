import pygame
from Antagonist import Enemy

class BgScreen:
    """Class for background screens"""

    def __init__(self, surface, screenWidth, screenHeight):
        self.surface = surface
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

    #def drawTitleScreen(self):
        #pygame.draw.rect(self.surface, ())

    def drawLevel1(self):
        pygame.draw.rect(self.surface, (135, 62, 35), (0, 0, self.screenWidth, self.screenHeight / 5))
        pygame.draw.rect(self.surface, (135, 62, 35), (0, self.screenHeight - self.screenHeight / 5, self.screenWidth, self.screenHeight / 5))
