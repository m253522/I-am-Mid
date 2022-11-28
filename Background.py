import pygame
from Antagonist import Enemy


class BgScreen:
    """Class for background screens"""

    def __init__(self, surface, screenWidth, screenHeight):
        self.surface = surface
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        # Menu title text
        self.menuTitleFont = pygame.font.Font('freesansbold.ttf', 64)
        self.menuTitleText = self.menuTitleFont.render('I am Mid', True, (0, 0, 0))
        self.menuTitleTextRect = self.menuTitleText.get_rect()
        self.menuTitleTextRect.center = (self.screenWidth // 2, self.screenHeight // 4)
        # Start button text
        self.menuButtonFont = pygame.font.Font('freesansbold.ttf', 32)
        self.menuStartButtonText = self.menuButtonFont.render('Start', True, (0, 0, 0))
        self.menuStartButtonTextRect = self.menuStartButtonText.get_rect()
        self.menuStartButtonTextRect.center = (self.screenWidth // 2, self.screenHeight // 2)
        # Instructions
        self.menuTutorialTextFont = pygame.font.Font('freesansbold.ttf', 13)
        self.menuTutorialText = self.menuTutorialTextFont.render('Instructions: You are a Midshipman at the United '
                                                                 'States Naval Academy. You are relieved late from '
                                                                 'watch and and you need to get to class. You can cut '
                                                                 'across the grass on stribling to make it on time. '
                                                                 , True, (0, 0, 0))
        self.menuTutorialText2 = self.menuTutorialTextFont.render('The only obstacles in your path are motivated '
                                                                  'Gunnery Sergeants with very high and tight '
                                                                  'haircuts. Good luck shipmate.', True, (0, 0, 0))
        self.menuTutorialTextRect = self.menuTutorialText.get_rect()
        self.menuTutorialTextRect.center = (self.screenWidth // 2, self.screenHeight // 1.3)
        self.menuTutorialText2Rect = self.menuTutorialText2.get_rect()
        self.menuTutorialText2Rect.center = (self.screenWidth // 2, self.screenHeight // 1.25)

    def drawMainMenu(self):
        pygame.draw.rect(self.surface, (255, 255, 255), (0, 0, self.screenWidth, self.screenHeight))
        pygame.draw.rect(self.surface, (0, 0, 255), self.menuTitleTextRect)
        pygame.draw.rect(self.surface, (0, 255, 0), self.menuStartButtonTextRect)
        self.surface.blit(self.menuTitleText, self.menuTitleTextRect)
        self.surface.blit(self.menuStartButtonText, self.menuStartButtonTextRect)
        self.surface.blit(self.menuTutorialText, self.menuTutorialTextRect)
        self.surface.blit(self.menuTutorialText2, self.menuTutorialText2Rect)

    def drawLevel1(self):
        pygame.draw.rect(self.surface, (135, 62, 35), (0, 0, self.screenWidth, self.screenHeight / 5))
        pygame.draw.rect(self.surface, (135, 62, 35),
                         (0, self.screenHeight - self.screenHeight / 5, self.screenWidth, self.screenHeight / 5))
