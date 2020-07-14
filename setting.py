class settings():
    """ A class to store all the settings of the game."""
    def __init__(self):
        """ Initialize the game's settings."""
        #Title and logo settings
        self.title="Alien Invasion"
        self.logo="images/logo.png"

        #screen settings 
        self.screen_width=1200
        self.screen_hight=600
        self.bg_color=(230,230,230)

        #ship settings
        self.ship_speed_factor=1.5

        #bullet settings
        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullet_allowed=3