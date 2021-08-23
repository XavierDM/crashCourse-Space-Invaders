class Settings:
    # class to store all settings

    def __init__(self):
        # initialize game static settings
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # ship
        self.ship_speed = 1.5
        self.ship_limit = 3

        # bullet
        self.bullet_speed = 1.5
        self.bullet_width = 600
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10

        # how quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initiliaze_dynamic_settings()

    def initiliaze_dynamic_settings(self):
        # initiliaze changing settings
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # 1 = right -1 = left
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        # increase speed settings
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)
