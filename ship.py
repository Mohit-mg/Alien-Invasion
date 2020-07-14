import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        """Initialize the ship and set its starting position."""
        self.screen=screen
        self.ai_settings=ai_settings

        #load the ship image and get its rect.
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #start each new ship at the bottom center of the screen.
        self.rect.centerx=self.screen_rect.centerx      #here we get the center cordinates of the x axis
        self.rect.bottom=self.screen_rect.bottom        #here we get the coordinate bottom of the screen 

        # store a decimal value for the ship's center.
        self.center=float(self.rect.centerx)

        #Movement Flag
        self.moving_right=False
        self.moving_left=False

    def update(self):
        """Update the ships's position based on the movement Flag."""
        #updating the ship's center value, not rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center +=self.ai_settings.ship_speed_factor# self.rect.centerx +=1

            #according to me
            # if self.rect.centerx >=1160:
            #     self.moving_right=False

        if self.moving_left and self.rect.left >0:
            self.center -=self.ai_settings.ship_speed_factor# self.rect.centerx -=1

            #according to me
            # if self.rect.centerx <=40:
            #     self.moving_left=False

        #update rect object from self.center.
        self.rect.centerx=self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)  # here we have to put two arrguments 1st one is image and 2nd one is coordinates of x and y axis of screen

    def center_ship(self):
        """Center the ship on the screen."""
        self.center =self.screen_rect.centerx