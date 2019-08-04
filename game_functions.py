import sys
import pygame


def check_events(ship):
    ''' Responds to keypresses and mouse events '''
    # watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Key press is detected by KEYDOWN 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True 
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        # release of key is deteced by KEYUP
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    ''' Update images on the screen and flip to the new screen '''
    # redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    # after screen.fill() we draw the ship so it appears on top of bg
    ship.blitme()
    
    # Make the most recently drawn screen visible
    pygame.display.flip()
