import ConfigParser
import pygame
import sys

from Ball import Ball

config = ConfigParser.ConfigParser()
config.readfp(open('config.cfg'))

display_config = {
    'caption': config.get('Display', 'caption'),
    'width': config.getint('Display', 'width'),
    'height': config.getint('Display', 'height')
}

pygame.init()

display = pygame.display.set_mode((display_config['width'],
                                  display_config['height']))
pygame.display.set_caption(display_config['caption'])
pygame.mouse.set_visible(0)
black = 0, 0, 0
ball = Ball(config)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            print event

    ball.tick()

    display.fill(black)
    display.blit(ball.getSurface(), ball.getRect())
    pygame.display.flip()
