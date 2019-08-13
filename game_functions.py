import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    ''' Respond to keypresses '''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True 
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(ai_settings, screen, ship, aliens, bullets):
    ''' Update images on the screen and flip to the new screen '''
    # redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    # bullets.sprites() returns a list of all sprites in the group bullets - loop through each and call draw_bullet() for each
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # after screen.fill() we draw the ship so it appears on top of bg
    ship.blitme() 
    # draws each alien in the group to the screen
    aliens.draw(screen)

    # Make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(bullets):
    ''' Update position of bullets and get rid of old bullets '''
    # Update bullet positions
    # when update() is called on a group, the group automatically calls update() for EACH sprite in the group
    # calls bullet.update() for EACH bullet we place in the group bullets
    bullets.update()

    # get rid of bullets that have disappeared (off top screen + consumes memory)
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    ''' Fire a bullet if limit not reached yet '''
    # Create a new bullet and add it to the bullets group
    # limits the number of bullets that a player can shoot
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        # stores the new bullet in the group bullets
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    ''' Determine the number of aliens that fit in a row '''
    # available space for alien is the screen width minus 2 alien widths
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    # divide the available space by 2 * width of an alien
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    ''' Determine the number of rows of aliens that fit on the screen '''
    # find the available vertical space by subtracting the alien height from the top, the ship height from the bottom and two alien heights from the bottom of the screen
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)

    # find the number of rows by dividing the available space by two times height of an alien
    number_rows = int(available_space_y // (2 * alien_height))
    return number_rows


# row_number parameter added
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    ''' Create an alien and place it in a row '''
    # spacing between each alien is equal to one alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    # alien is pushed to the RIGHT one alien width from the left margin
    # multiply the alien width by 2 to account for the space each alien takes up including the empty space to its right
    # multiply this amount by the alien's position in the row
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    # each row starts 2 alien heights below the last row, so we multiply the alien height by 2 and then by the row number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    ''' Create a full fleet of aliens '''
    # create an alien and find the number of aliens in a row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # the outer loop counts from 0 to the number of rows we want
    for row_number in range(number_rows):
        # inner loop creates the aliens in one row 
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    ''' Respond appropriately if any aliens have reached an edge '''
    # if check_edges() returns True --> call change_fleet_direction()
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    ''' Drop the entire fleet and change the fleet's directions '''
    for alien in aliens.sprites():
        # loop through aliens and drop each one using the setting fleet_drop_speed and then we change the value of fleet_direction by multiplying its current value by -1
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens):
    ''' Update the position of all aliens in the fleet '''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()