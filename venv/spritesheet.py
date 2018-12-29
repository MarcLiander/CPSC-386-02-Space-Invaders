import pygame

class SpriteSheet:

    def __init__(self, filename, type):
        self.sheet = pygame.image.load(filename).convert()
        self.type = type

    def image_get(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size)
        image.blit(self.sheet, (0, 0), rect)
        if self.type == 2:
            transparent_color = None
        elif self.type == 1:
            transparent_color = image.get_at((59, 47))
        else:
            transparent_color = image.get_at((47, 63))
        image.set_colorkey(transparent_color)
        return image