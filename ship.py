import pygame


class Ship():
    
    def __init__(self, screen):
        ''' initialize the ship and set its starting position '''
        self.screen = screen

        # Load the ship image and gets its rect.
        self.image = pygame.image.load('images/ship.bmp')
        # rectangular area of the image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # movement flag for continuous movement
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        ''' update the ship's position based on the movement's flag '''
        if self.moving_right:
            # move the ship to the right
            self.rect.centerx += 1

        if self.moving_left:
            # move the ship to the left
            self.rect.centerx -= 1


    def blitme(self):
        ''' draw the ship at its current location '''
        self.screen.blit(self.image, self.rect)
