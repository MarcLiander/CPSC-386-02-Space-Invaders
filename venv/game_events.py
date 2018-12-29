import sys
import pygame
from bullet import Bullet
from star import Star
from random import randint

class EventLoop:
    def __init__(self, settings, screen, ships, fields, stats, scoreboard, stars, finished):
        self.finished = finished
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        for ship in ships:
            self.ship = ship
        for field in fields:
            self.field = field
        self.stats = stats
        self.scoreboard = scoreboard
        self.level_clear = False
        self.level_clear_time = 0

        self.stars = stars
        self.star_timer = 0

    def check_input_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_SPACE:
            if len(self.field.bullets) < 3:
                self.fire_bullet()
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def update_events(self):
        self.scoreboard.update_score(self.field.update_field())
        self.finished = self.ship.update_ship(self.field)

        if len(self.field.aliens) <= 0:
            self.settings.create_new_aliens = True
            self.level_clear_time += 1

        if self.level_clear_time > 120:
            self.level_clear = True
            self.level_clear_time = 0

        self.star_timer += randint(1, 4)
        if self.star_timer > 15:
            self.star_timer = 0
            self.stars.append(Star(self.settings, self.screen, randint(1, self.settings.screen_width - 1)))
        for star in self.stars:
            star.update_star()
            if star.rect.top > self.settings.screen_height:
                self.stars.remove(star)

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for star in self.stars:
            star.show_star()
        self.field.show_field()
        self.ship.show_ship()
        self.scoreboard.show_score()
        pygame.display.flip()

    def fire_bullet(self):
        self.field.bullets.append(Bullet(self.settings, self.screen, self.ship))
