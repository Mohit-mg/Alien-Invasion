import pygame

class settings():
    """ A class to store all the settings of the game."""
    def __init__(self):
        """ Initialize the game's  static settings."""
        #Title and logo settings
        self.title="Alien Invasion"
        self.logo="images/logo.png"
        #background
        self.background=pygame.image.load("images/background.png")

        #screen settings 
        self.screen_width=1200
        self.screen_height=600
        self.bg_color=(230,230,230)

        #ship settings
        # self.ship_speed_factor=3
        self.ship_limit=3

        #bullet settings
        # self.bullet_speed_factor=4
        self.bullet_width=5
        self.bullet_height=15
        self.bullet_color=250,250,250
        self.bullet_allowed=3

        #Alien Settings
        # self.alien_speed_factor=3
        self.fleet_drop_speed=20
      

        #How quickly the game speeds up
        self.speedup_scale=1.1
        #how quickly the alien point values increase
        self.score_scale=1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1

        #fleet_direction of 1 represents right ; -1 represents left.
        self.fleet_direction=1

        #Scoring
        self.alien_points=50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale

        self.alien_points=int(self.alien_points*self.score_scale)
        # print(self.alien_points)