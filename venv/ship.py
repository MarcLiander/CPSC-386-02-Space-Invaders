from spritesheet import SpriteSheet


class Ship():

    def __init__(self, settings, screen, ship_sheet):
        super(Ship, self).__init__()

        self.screen = screen
        self.settings = settings

        self.index = 0
        self.type = 0
        self.timer = 0
        self.sprite = SpriteSheet(ship_sheet, 1)
        self.image = self.sprite.image_get((60 * self.index, 48 * self.type, 60, 48))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update_ship(self, field):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0 and not self.settings.create_new_aliens:
            self.rect.centery -= self.settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.settings.ship_speed_factor

        if self.rect.bottom < self.screen_rect.bottom and self.settings.create_new_aliens:
            self.rect.centery += self.settings.screen_height / 120

        if self.timer < 25:
            self.timer += 1
        else:
            self.index += 1
            if self.index >= 8:
                self.index = 0
            self.image = self.sprite.image_get((60 * self.index, 48 * self.type, 60, 48))
            self.timer = 0

        return self.hit_by_enemy(field)

    def show_ship(self):
        self.screen.blit(self.image, self.rect)

    def hit_by_enemy(self, field):
        for alien in field.aliens:
            if self.rect.colliderect(alien.rect):
                return True
        for enemy_bullet in field.enemy_bullets:
            if self.rect.colliderect(enemy_bullet.rect):
                return True
        return False