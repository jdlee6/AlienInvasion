import pygame


class Ship():
    
    def __init__(self, ai_settings, screen):
        ''' initialize the ship and set its starting position '''
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and gets its rect.
        self.image = pygame.image.load('images/ship.bmp')
        # rectangular area of the image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # movement flag for continuous movement
        self.moving_right = False
        self.moving_left = False
    

    def update(self):
        ''' update the ship's position based on the movement's flag '''
        # update the ship's center value, not the rect
        # if self.rect.right (x coordinate of right edge of ship) is < value returned by self.screen.right --> ship hasn't reached  the right edge of screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # move the ship to the right by pixels in ai_settings
            self.center += self.ai_settings.ship_speed_factor

        # if self.rect.left (x coordinate of left edge of ship) is > 0, ship hasn't reached the left edge
        # could use self.screen_rect.left
        if self.moving_left and self.rect.left > self.screen_rect.left:
            # move the ship to the left by pixels in ai_settings
            self.center -= self.ai_settings.ship_speed_factor

        # update rect object from self.center
        self.rect.centerx = self.center


    def blitme(self):
        ''' draw the ship at its current location '''
        self.screen.blit(self.image, self.rect)
