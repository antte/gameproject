import pygame


class Engine:
    def __init__(self, config):

        config.get('Display', 'caption'),
        config.getint('Display', 'width'),
        config.getint('Display', 'height'),
        config.getint('Display', 'framerate')

        pygame.init()
        self.display = pygame.display.set_mode((config.getint('Display', 'width'),
                                                config.getint('Display', 'height')))
        pygame.display.set_caption(config.get('Display', 'caption'))
        pygame.mouse.set_visible(0)

        self.entities = []
        self.framerate = config.getint('Display', 'framerate')
        self.clock = pygame.time.Clock()
        self.show_fps = config.getboolean('Display', 'show_fps')

        self.screen = pygame.display.get_surface()
        self.surface = pygame.display.get_surface()
        self.area = self.screen.get_rect()

    def update(self):
        self.clock.tick(self.framerate)

        black = 0, 0, 0
        white = 255, 255, 255
        self.display.fill(black)

        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))

        if self.show_fps:
            font = pygame.font.Font(None, 36)
            fps_string = str(round(self.clock.get_fps())) + "fps"
            text = font.render(fps_string, 1, white)
            textpos = text.get_rect(centerx=text.get_width() / 2)
            self.display.blit(text, textpos)

        for entity in self.entities:
            entity.tick()
            self.display.blit(entity.surface, entity.rect)

        pygame.display.flip()
