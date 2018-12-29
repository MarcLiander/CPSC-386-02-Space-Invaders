import pygame
from bullet import Bullet, Enemy_Bullet
from alien import Alien
from star import Star
from random import randint

class Field:
    def __init__(self, settings, screen, bullet_sheet, enemy_bullet_sheet, alien_sheet):
        super(Field, self).__init__()

        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.aliens = []
        self.bullets = []
        self.enemy_bullets = []

        self.bullet_sheet = bullet_sheet
        self.enemy_bullet_sheet = enemy_bullet_sheet
        self.alien_sheet = alien_sheet

        self.timer = 0

    def create_level(self):
        number_column = int((self.settings.screen_width - 2 * self.settings.alien_width) / (2 * self.settings.alien_width))
        number_row = int((self.settings.screen_height - 2 * self.settings.alien_height) / (2 * self.settings.alien_height))
        type = 0

        for row_number in range(number_row):
            type = int(row_number / 2) % 3
            for column_number in range(number_column):
                self.aliens.append(Alien(self.settings, self.screen, column_number, row_number, type, self.alien_sheet))

    def update_field(self):
        points_gained = 0
        for bullet in self.bullets:
            bullet.update_bullet()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update_enemy_bullet()
            if enemy_bullet.rect.top > self.screen_rect.height:
                self.enemy_bullets.remove(enemy_bullet)
        for alien in self.aliens:
            if alien.check_edges():
                for alien in self.aliens:
                    alien.rect.y += self.settings.fleet_drop_speed
                    alien.rect.x += 2 * -self.settings.fleet_direction
                self.settings.fleet_direction *= -1
                break
        for alien in self.aliens:
            self.timer += randint(10, 100)
            if self.timer > 2000 * len(self.aliens):
                self.enemy_bullets.append(Enemy_Bullet(self.settings, self.screen, alien))
                self.timer = 0
            alien.update_alien()
            if alien.check_bullet_collision(self.bullets):
                points_gained += self.settings.alien_points * (alien.type + 1)
                self.aliens.remove(alien)
        return points_gained

    def show_field(self):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.show_enemy_bullet()
        for bullet in self.bullets:
            bullet.show_bullet()
        for alien in self.aliens:
            alien.show_alien()