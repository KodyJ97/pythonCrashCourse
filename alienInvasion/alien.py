import pygame, os
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set it rect attribute
        mydir = os.path.dirname('__file__')
        self.image = pygame.image.load(os.path.join(mydir, 'images/alien.bmp'))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current position"""
        self.screen.blit(self.image, self.rect)