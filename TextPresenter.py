import pygame
from pygame.locals import *
from threading import Timer

class TextPresenter:

    def __init__(self, config):
        self.config = config
        self.x = -100
        self.y = 0

    def tick(self, display):
        font = pygame.font.Font(None, 36)
        string = self.config.get('Display', 'caption')
        white = 255, 255, 255
        text = font.render(string, 20, white)

        text = pygame.transform.rotate(text, self.x % 360)

        textpos = text.get_rect(centerx=self.x)
        display.blit(text, textpos)

        self.x = self.x + 1

        if self.x > 720:
            self.x = -100
