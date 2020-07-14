import pygame

class settings():
    """ A class to store all the settings of the game."""
    def __init__(self):
        """ Initialize the game's settings."""
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
        self.ship_speed_factor=3

        #bullet settings
        self.bullet_speed_factor=2
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=250,250,250
        self.bullet_allowed=3

        #Alien Settings
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        #fleet_direction of 1 represents right; -1represents left.
        self.fleet_direction=1