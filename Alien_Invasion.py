import pygame
from pygame.sprite import Group

from setting import settings
from ship import Ship
import game_functions as gf

def run_game():
    #initialize pygame, settings and screen objects.
    pygame.init()
    ai_settings=settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_hight))


    #changing title and logo
    pygame.display.set_caption(ai_settings.title)
    logo=pygame.image.load(ai_settings.logo)
    pygame.display.set_icon(logo)


    #make a ship.
    ship=Ship(ai_settings,screen)
    #make a group to store bullets in.
    bullets=Group()


    # Set the background color.
    bg_color=(190,200,210)



    #start the main loop for the game.
    while True:
        #Function for keyboard and mouse events.
        gf.check_events(ai_settings,screen,ship,bullets)

        #updating surfaces
        ship.update()
        bullets.update()

        #updating game functions
        gf.update_screen(ai_settings,screen,ship,bullets)

       

       

if __name__ == "__main__":
    run_game()