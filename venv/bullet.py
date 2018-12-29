import pygame
from pygame.sprite import Sprite
from spritesheet import SpriteSheet

class Bullet(Sprite):
    def __init__(self, settings, screen, ship):
        super(Bullet, self).__init__()
        self.settings = settings
        self.screen = screen
        self.sprite = SpriteSheet('images/laser.png', 2)

        self.index = 0
        self.type = 0
        self.timer = 0
        self.image = self.sprite.image_get((8 * self.index, 24 * self.type, 8, 24))
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

    def update_bullet(self):
        self.rect.y -= self.settings.bullet_speed_factor

        if self.timer < 10:
            self.timer += 1
        else:
            self.index += 1
            if self.index >= 4:
                self.index = 0
            self.image = self.sprite.image_get((8 * self.index, 24 * self.type, 8, 24))
            self.timer = 0

    def show_bullet(self):
        self.screen.blit(self.image, self.rect)


class Enemy_Bullet(Sprite):
    def __init__(self, ai_settings, screen, alien):
        super(Enemy_Bullet, self).__init__()
        self.screen = screen
        self.sprite = SpriteSheet('images/enemy_laser.png', 2)

        self.index = 0
        self.type = 0
        self.timer = 0
        self.image = self.sprite.image_get((8 * self.index, 24 * self.type, 8, 24))
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update_enemy_bullet(self):
        self.y += self.speed_factor
        self.rect.y = self.y

        if self.timer < 10:
            self.timer += 1
        else:
            self.index += 1
            if self.index >= 4:
                self.index = 0
            self.image = self.sprite.image_get((8 * self.index, 24 * self.type, 8, 24))
            self.timer = 0

    def show_enemy_bullet(self):
        self.screen.blit(self.image, self.rect)