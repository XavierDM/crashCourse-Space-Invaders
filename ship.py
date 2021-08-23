import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_game):
        # initialize ship & start position
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load ship
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each ship bottom middle
        self.rect.midbottom = self.screen_rect.midbottom

        # store ship x value as float
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # update ship position based on movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object
        self.rect.x = self.x

    def blitme(self):
        # draw ship at current location
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # ship center screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
