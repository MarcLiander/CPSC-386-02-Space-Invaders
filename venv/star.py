import pygame

class Star():

    def __init__(self, ai_settings, screen, x):
        super(Star, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/stardrop.png')
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = 50

    def update_star(self):
        self.rect.y += 2

    def show_star(self):
        self.screen.blit(self.image, self.rect)