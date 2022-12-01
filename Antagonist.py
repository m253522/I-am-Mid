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

    def moveRight(self):
        self.rect.x += self.speed

    def moveLeft(self):
        self.rect.x -= self.speed

    def LoadLevel1Entity(self):
        if self.rect.x - self.spawnX != self.surface_rect.right:
            self.surface.blit(self.image, (self.rect.x - self.spawnX, self.rect.y + self.spawnY))
            self.moveRight()
        elif self.rect.x - self.spawnX == self.surface_rect.right:
            self.rect.x = 0
            self.surface.blit(self.image, (self.rect.x - self.spawnX, self.rect.y + self.spawnY))
            self.moveRight()



