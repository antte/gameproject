import ConfigParser
from engine import Engine
import os
import pygame
import sys

from Ball import Ball

config = ConfigParser.ConfigParser()
config.readfp(open('config.cfg'))

engine = Engine(config)
ball = Ball(config)
engine.entities.append(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    engine.update()
