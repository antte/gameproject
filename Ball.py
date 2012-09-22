import pygame


class Ball:
    def __init__(self, config):
        self.speed = [2, 2]
        self.config = config
        images_path = config.get('Assets', 'image_path')
        self.surface = pygame.image.load(images_path + "ball.gif")
        self.rect = self.surface.get_rect()

    def tick(self):
        display_width = self.config.getint('Display', 'width')
        display_height = self.config.getint('Display', 'height')

        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > display_width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > display_height:
            self.speed[1] = -self.speed[1]
