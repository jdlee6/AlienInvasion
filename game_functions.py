import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    ''' Respond to keypresses '''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True 
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # create a new bullet and add it to the bullets group
        # limits the number of bullets that a player can shoot
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            # stores the new bullet in the group bullets
            bullets.add(new_bullet)


def check_keyup_events(event, ship):
    ''' Respond to key releases '''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    ''' Responds to keypresses and mouse events '''
    # watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Key press is detected by KEYDOWN 
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # release of key is deteced by KEYUP
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    ''' Update images on the screen and flip to the new screen '''
    # redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    # bullets.sprites() returns a list of all sprites in the group bullets - loop through each and call draw_bullet() for each
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # after screen.fill() we draw the ship so it appears on top of bg
    ship.blitme()
    
    # Make the most recently drawn screen visible
    pygame.display.flip()
