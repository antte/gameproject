import pygame
from pygame.locals import *
from threading import Timer

class Ball:

    is_exploding = False

    def __init__(self, config):
        self.speed = [3, 3]
        self.config = config
        image_path = self.config.get('Assets', 'image_path')
        self.surface = pygame.image.load(image_path + "ball.gif")
        self.rect = self.surface.get_rect()

    def tick(self, display):
        display_width = self.config.getint('Display', 'width')
        display_height = self.config.getint('Display', 'height')

        if pygame.key.get_pressed()[K_SPACE]:
            self.explode()

        if not self.is_exploding:
            self.rect = self.rect.move(self.speed)

        if self.rect.left < 0 or self.rect.right > display_width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > display_height:
            self.speed[1] = -self.speed[1]

        display.blit(self.surface, self.rect)

    def getSurface(self):
        return self.surface

    def getRect(self):
        return self.rect

    def explode(self):
        self.is_exploding = True
        image_path = self.config.get('Assets', 'image_path')
        self.surface = pygame.image.load(image_path + "explosion.png")
        old = self.surface
        self.surface = pygame.Surface((280, 238))
        pygame.transform.scale2x(old, self.surface)
        self.__explode_sound()

        Timer(1, self.destroy).start()

    def destroy(self):
        self.surface.fill((0,0,0))
        self.is_exploding = False

    def __explode_sound(self):
        pygame.mixer.init()
        sound_path = self.config.get('Assets', 'sound_path')
        pygame.mixer.Sound(sound_path + 'explosion.wav').play()
