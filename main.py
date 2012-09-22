import ConfigParser
from engine import Engine
import os
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


engine = Engine(display_config)
ball = Ball(config)
engine.entities.append(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            print event

    engine.update()
