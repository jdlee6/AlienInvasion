''' 
NOTE:
pygame.QUIT - x button of game display windows
(0,0) = top-left corner of the screen
    - coordinates increase as you go down and to the right
'''

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # initialize pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    ship = Ship(ai_settings, screen)
    # make a group to store bullets in
    bullets = Group()

    # start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        # when update() is called on a group, the group automatically calls update() for EACH sprite in the group
        # calls bullet.update() for EACH bullet we place in the group bullets
        bullets.update()

        # get rid of bullets that have disappeared (off top screen + consumes memory)
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        gf.update_screen(ai_settings,screen,ship, bullets)


run_game()