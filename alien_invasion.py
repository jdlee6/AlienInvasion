''' 
NOTE:
pygame.QUIT - x button of game display windows
(0,0) = top-left corner of the screen
    - coordinates increase as you go down and to the right
'''

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    # initialize pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make the Play button
    play_button = Button(ai_settings, screen, "Play")

    # create an instance to store game statistics
    stats = GameStats(ai_settings)

    # make a ship, group of bullets and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop for the game
    while True:
        # this is still in the main loop because we want to know if the player presses Q to quit or clicks a button to close the window
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        # these functions are called only when the game is active
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # update aliens after bullets have been updated b/c we need to check if bullets hit any aliens
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # continue updating the screen so we can make changes to the screen while waiting to see whether the player chooses to start a new game
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()