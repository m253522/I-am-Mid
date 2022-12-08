import pygame


class Enemy:
    """Class for enemy objects"""

    def __init__(self, imageSelection, surface, surface_rect, spawnX, spawnY, speed):
        self.image = pygame.image.load(imageSelection)
        self.rect = self.image.get_rect()
        self.surface = surface
        self.surface_rect = surface_rect
        self.spawnX = spawnX
        self.spawnY = spawnY
        self.speed = speed
        self.velocityX = 0
        self.velocityY = 0
        self.rect.x = self.spawnX
        self.rect.y = self.spawnY

    def moveRight(self):
        self.velocityX = 0
        if self.rect.x <= self.surface_rect[2]:
            self.velocityX += self.speed
            self.rect.x += self.velocityX
        else:
            self.rect.x = self.spawnX

    def LoadLevel1Entity(self):
        from Game import Score
        if Score >= 8:
            self.speed = 9
        elif Score >= 5:
            self.speed = 7
        else:
            self.speed = 5
        self.moveRight()
        self.surface.blit(self.image, self.rect)
