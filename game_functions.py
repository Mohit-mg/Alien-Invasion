import pygame
import sys

from bullet import Bullet



def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """Respond to keypress"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key == pygame.K_LEFT:
        ship.moving_left=True
    elif event.key == pygame.K_SPACE:
        #Creating a new bullet and add it to the bullets group.
        new_bullet= Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key == pygame.K_LEFT:
        ship.moving_left= False

def check_events(ai_settings,screen,ship,bullets):
    """Respond to keypresses and mouse events. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)

            # check_keydown_events(event,ship)
           
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            

       

def update_screen(ai_settings,screen,ship,bullets):
    """update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through th loop.
    screen.fill(ai_settings.bg_color)

    #redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #calling ship image at screen
    ship.blitme()
    #make the most recently drawn screen visible.
    pygame.display.flip()

   