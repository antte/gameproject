import ConfigParser
from engine import Engine
import os
import pygame
import sys

from Ball import Ball
from TextPresenter import TextPresenter

config = ConfigParser.ConfigParser()
config.readfp(open('config.cfg'))

engine = Engine(config)
ball = Ball(config)
tp = TextPresenter(config)
engine.entities.append(ball)
engine.entities.append(tp)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    engine.update()
