import sys
import pygame
from settings import Settings
from game_stats import GameStats
from game_events import EventLoop
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from field import Field

class Game():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("CPSC 386-02 Project - Modified Space Invaders")
        self.clock = pygame.time.Clock()

        self.ships = []
        self.fields = []
        self.stats = GameStats(self.settings)
        self.scoreboard = Scoreboard(self.settings, self.screen, self.stats)

        self.play_button = Button(self.settings, self.screen, "Play")
        self.reset_level = True

        self.stars = []

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_clicked = self.play_button.rect.collidepoint(mouse_x, mouse_y)
                    if button_clicked:
                        self.reset_level = False
            while not self.reset_level:
                self.scoreboard.ships.clear()
                self.scoreboard.prep_ships()
                self.ships.append(Ship(self.settings, self.screen, ship_sheet = 'Images/ship_spritesheet.png'))
                self.fields.append(Field(self.settings, self.screen, bullet_sheet = 'Images/laser.png', enemy_bullet_sheet = 'Images/enemy_laser.png', alien_sheet = 'Images/alien_spritesheet.png'))
                eloop = EventLoop(self.settings, self.screen, self.ships, self.fields, self.stats, self.scoreboard, self.stars, finished = False)
                for field in self.fields:
                    field.create_level()
                while not eloop.finished:
                    eloop.update_events()
                    eloop.check_input_events()
                    eloop.update_screen()
                    if eloop.level_clear:
                        self.fields.clear()
                        self.fields.append(Field(self.settings, self.screen, bullet_sheet='Images/laser.png', enemy_bullet_sheet='Images/enemy_laser.png', alien_sheet='Images/alien_spritesheet.png'))
                        for field in self.fields:
                            eloop.field = field
                        eloop.field.create_level()
                        self.settings.create_new_aliens = False
                        self.settings.increase_speed()
                        eloop.level_clear = False
                    if self.stats.ships_left <= 0:
                        self.reset_level = True
                    self.clock.tick(60)
                self.stats.ships_left -= 1
                self.ships.clear()
                self.fields.clear()
            self.play_button.draw_button()
            pygame.display.flip()
            self.settings.initialize_dynamic_settings()
            self.stats.score = 0
            self.stats.ships_left = self.settings.ship_limit


game = Game()
game.play()