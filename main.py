import pygame, sys

pygame.init()

screen_dimensions = {
    'width': 640,
    'height': 480,
}

screen = pygame.display.set_mode(( screen_dimensions['width'] ,
                                  screen_dimensions['height']))
pygame.display.set_caption('glogghack #2')
pygame.mouse.set_visible(0)
images_path = 'images/'

speed = [2, 2]
black = 0, 0, 0

ball = pygame.image.load(images_path + "ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > screen_dimensions['width']:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > screen_dimensions['height']:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
