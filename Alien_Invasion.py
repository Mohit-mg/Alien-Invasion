import pygame
from pygame.sprite import Group

from setting import settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf


def run_game():
    #initialize pygame, settings and screen objects.
    pygame.init()
    ai_settings=settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))


    #changing title and logo
    pygame.display.set_caption(ai_settings.title)
    logo=pygame.image.load(ai_settings.logo)
    pygame.display.set_icon(logo)

    #Make the Play button.
    play_button=Button(ai_settings,screen,"Play")

    #Create an instance to Store game statistics and create a scoreboard.
    stats=GameStats(ai_settings)
    sb= Scoreboard(ai_settings,screen,stats)


    #make a ship, a group of bullets, and a group of aliens.
    ship=Ship(ai_settings,screen)
    bullets=Group()
    aliens=Group()

    # Create the fleet of the aliens.
    gf.Create_fleet(ai_settings,screen,ship,aliens)

    


    #make an alien.
    # alien=Alien(ai_settings,screen)



    #start the main loop for the game.
    while True:
        #Function for keyboard and mouse events.
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

        
        if stats.game_active:
        #updating surfaces
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)

        # #get rid of the bullets that have disappeared.
        # for bullet in bullets.copy():
        #     if bullet.rect.bottom <=0:
        #         bullets.remove(bullet)
        #     print(len(bullets))

        #updating game functions
        # gf.update_screen(ai_settings,screen,ship,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

       

       

if __name__ == "__main__":
    run_game()