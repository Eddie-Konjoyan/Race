import pygame
import math
class Car(pygame.sprite.Sprite):
    def __init__(self,screen,carnum):
        super().__init__()

        scale = (40,70)

        # Initialize car based on color
        if carnum ==1:
            self.image_o = pygame.transform.scale(pygame.image.load('PNG/Cars/car_red_5.png'),scale)
        if carnum ==2:
            self.image_o = pygame.transform.scale(pygame.image.load('PNG/Cars/car_blue_5.png'),scale)
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
        # Assign new rect with current center.
        # Keep the image in center as the rect changes size.
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.x += self.speed*math.cos((self.bearing*math.pi)/180)
        self.rect.y += -self.speed*math.sin((self.bearing*math.pi)/180)

    def turn_left(self):
        """Turn car left 10 degrees"""
        self.bearing += 3.5

    def turn_right(self):
        """Turn car right 10 degrees"""
        self.bearing -= 3.5

    def speed_upf(self):
        """Slow down or speed up"""
        if self.speed < 8:
            self.speed += .2
    def coast(self):
        """Slow down or speed up"""
        if self.speed > 0:
            self.speed -= .1
        if self.speed < 0:
            self.speed += .2
        if self.speed == 0:
            self.speed =0

    def speed_upr(self):
        """Slow down or speed up"""
        if self.speed >-4:
            self.speed -=.2






