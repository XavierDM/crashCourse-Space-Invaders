import pygame
from pygame.sprite import Sprite  # used to group related elements at once


class Bullet(Sprite):

    def __init__(self, ai_game):
        # create bullet at current ship position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create bullet rect at 0,0 and set correct position
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store bullet position as float
        self.y = float(self.rect.y)

    def update(self):
        # move bullet up the screen
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
