class Settings():

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color = (0, 0, 0)
        self.item_color = (0, 255, 0)

        self.ship_limit = 3

        self.bullet_width = 8
        self.bullet_height = 24
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10

        self.alien_points = 50
        self.alien_width = 48
        self.alien_height = 64

        self.speedup_scale = 2
        self.score_scale = 50

        self.create_new_aliens = False

        self.ship_speed_factor = 4
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 1
        self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 4
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 1
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor += self.speedup_scale
        self.bullet_speed_factor += self.speedup_scale
        self.alien_speed_factor += self.speedup_scale
        self.alien_points = int(self.alien_points + self.score_scale)