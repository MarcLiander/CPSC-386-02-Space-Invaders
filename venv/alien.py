from pygame.sprite import Sprite
from spritesheet import SpriteSheet

class Alien(Sprite):
    def __init__(self, settings, screen, column_number, row_number, type, alien_sheet):
        super(Alien, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.sprites = SpriteSheet(alien_sheet, 0)

        self.index = 0
        self.type = type
        self.timer = 0
        self.image = self.sprites.image_get((self.settings.alien_width * self.index, self.settings.alien_height * self.type, self.settings.alien_width, self.settings.alien_height))
        self.rect = self.image.get_rect()

        self.rect.x = self.settings.alien_width + 2 * self.settings.alien_width * column_number
        self.rect.y = self.screen_rect.height - (6 * self.rect.height) - 1.2 * self.rect.height * row_number

    def check_edges(self):
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update_alien(self):
        self.rect.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)

        if self.timer < 25:
            self.timer += 1
        else:
            self.index += 1
            if self.index >= 4:
                self.index = 0
            self.image = self.sprites.image_get((self.settings.alien_width * self.index, self.settings.alien_height * self.type, self.settings.alien_width, self.settings.alien_height))
            self.timer = 0

    def check_bullet_collision(self, bullets):
        for bullet in bullets:
            if self.rect.colliderect(bullet.rect):
                bullets.remove(bullet)
                return True
        return False

    def show_alien(self):
        self.screen.blit(self.image, self.rect)