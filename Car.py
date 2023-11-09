import pygame
class Car(pygame.sprite.Sprite):
    def __init__(self,screen,carnum):
        super().__init__()

        scale = (40,70)

        # Initialize car based on color
        if carnum ==1:
            self.image_o = pygame.transform.scale(pygame.image.load('PNG/Cars/car_red_5.png'),scale)
        if carnum ==2:
            self.image_o = pygame.image.load('PNG/Cars/car_blue_5.png')
        self.image_o = pygame.transform.rotate(self.image_o,-90)
        self.image = self.image_o
        # create rect obj for car
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 20
        self.screen = screen

        #initial speed
        self.speed = 0
        #initial direction
        self.bearing = 0
        #acceleration when on gas pedal
        self.accel_g = 10
        #acceleration when coasting
        self.accel_c = -5



    def update(self):
        self.image = pygame.transform.rotate(self.image_o, self.bearing)

    def turn_left(self):
        """Turn car left 10 degrees"""
        self.bearing += 2

    def turn_right(self):
        """Turn car right 10 degrees"""
        self.bearing -= 2

    def speed_set(self,change):
        """Slow down or speed up"""
        pass







