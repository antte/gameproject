import ConfigParser
import os
import pygame
import sys

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

speed = [2, 2]
black = 0, 0, 0

images_path = config.get('Assets', 'image_path')
ball = pygame.image.load(images_path + "ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > display_config['width']:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > display_config['height']:
        speed[1] = -speed[1]

    display.fill(black)
    display.blit(ball, ballrect)
    pygame.display.flip()
