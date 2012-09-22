import pygame
from pygame.locals import *

class Ball:
    IMAGES_PATH = config.get('Assets', 'image_path')

    def __init__(self, config):
        self.speed = [2, 2]
        self.config = config
        self.surface = pygame.image.load(IMAGES_PATH + "ball.gif")
        self.rect = self.surface.get_rect()

        Timer(30.0, explode)

    def tick(self):
        display_width = self.config.getint('Display', 'width')
        display_height = self.config.getint('Display', 'height')

        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > display_width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > display_height:
            self.speed[1] = -self.speed[1]

    def getSurface(self):
        return self.surface

    def getRect(self):
        return self.rect

    def explode(self):
        self.surface = pygame.image.load(IMAGES_PATH + "explosion.png")
        Timer(2.0, destroy)

    def destroy(self):
        self.surface.fill
        self.surface.set_alpha(255)
