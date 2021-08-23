import pygame
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load alien image
        self.image = pygame.image.load('Images/alien.bmp')
        self.rect = self.image.get_rect()

        # start alien top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # stpre exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        # returns True if alien at edge
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        # move right
        self.x += (self.settings.alien_speed / self.settings.fleet_direction)
        #self.x += self.settings.alien_speed
        self.rect.x = self.x
