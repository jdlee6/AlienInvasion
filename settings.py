class Settings():
    ''' a class to store all settings for alien invasion '''
    
    def __init__(self):
        ''' initialize the game's settings '''
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship Settings (1.5 px instead of 1 px)
        self.ship_speed_factor = 1.5

        # Bullet Settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3