import pygame


class Engine:
    def __init__(self, display_config):
        pygame.init()
        self.display = pygame.display.set_mode((display_config['width'],
                                                display_config['height']))
        pygame.display.set_caption(display_config['caption'])
        pygame.mouse.set_visible(0)

    def update(self):
        black = 0, 0, 0
        self.display.fill(black)

        for entity in self.entities:
            entity.tick()
            self.display.blit(entity.surface, entity.rect)

        pygame.display.flip()
