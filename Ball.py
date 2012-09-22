import pygame
from pygame.locals import *
from threading import Timer

class Ball:

    isExploding = False

    def __init__(self, config):
        self.speed = [1, 1]
        self.config = config
        image_path = self.config.get('Assets', 'image_path')
        self.surface = pygame.image.load(image_path + "ball.gif")
        self.rect = self.surface.get_rect()

        Timer(5, self.explode).start()

    def tick(self):
        display_width = self.config.getint('Display', 'width')
        display_height = self.config.getint('Display', 'height')

        if not self.isExploding:
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
        self.isExploding = True
        image_path = self.config.get('Assets', 'image_path')
        self.surface = pygame.image.load(image_path + "explosion.png")
        Timer( 1, self.destroy).start()

    def destroy(self):
        self.surface.fill((0,0,0))
        self.isExploding = False
