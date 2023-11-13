import pygame
import math

import background


class Car(pygame.sprite.Sprite):
    def __init__(self,screen,carnum,position):
        super().__init__()

        scale = (40,70)

        # Initialize car based on color
        if carnum ==1:
            self.image_o = pygame.transform.scale(pygame.image.load('PNG/Cars/car_black_5.png'),scale)
        if carnum ==2:
            self.image_o = pygame.transform.scale(pygame.image.load('PNG/Cars/car_blue_5.png'),scale)
        self.image_o = pygame.transform.rotate(self.image_o,-90)
        self.image = self.image_o
        # create rect obj for car
        self.rect = self.image.get_rect()
        if position == 1:
            self.rect.x = 550
            self.rect.y = 30
        elif position == 2:
            self.rect.x = 550
            self.rect.y = 90
        self.screen = screen

        #initial speed
        self.speed = 0
        #initial direction
        self.bearing = 0
        #acceleration when on gas pedal
        self.accel_g = 10
        #acceleration when coasting
        self.accel_c = -5


    def update(self,screen):
        self.image = pygame.transform.rotate(self.image_o, self.bearing)
        # Assign new rect with current center.
        # Keep the image in center as the rect changes size.
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.x += self.speed*math.cos((self.bearing*math.pi)/180)
        self.rect.y += -self.speed*math.sin((self.bearing*math.pi)/180)

        if self.rect.x > screen.get_width()-self.image.get_width()+10:
            self.rect.x = screen.get_width()-self.image.get_width()+10
            self.speed = 0
        if self.rect.x < -10:
            self.rect.x = -10
            self.speed = 0
        if self.rect.y > screen.get_height()-self.image.get_height()+10:
            self.rect.y = screen.get_height()-self.image.get_height()+10
            self.speed = 0
        if self.rect.y < -10:
            self.rect.y = -10
            self.speed = 0
    def turn_left(self):
        """Turn car left 10 degrees"""
        self.bearing += 3

    def turn_right(self):
        """Turn car right 10 degrees"""
        self.bearing -= 3

    def speed_upf(self,max):
        """Slow down or speed up"""
        if self.speed < max:
            self.speed += .2
        if self.speed > max:
            self.speed = max
    def coast(self):
        """Slow down or speed up"""
        if self.speed > 0:
            self.speed -= .1
        if self.speed < 0:
            self.speed += .2
        if self.speed == 0:
            self.speed =0

    def speed_upr(self,max):
        """Slow down or speed up"""
        if self.speed > max:
            self.speed -=.2
        if self.speed < max:
            self.speed = max
    def track1_grass_slow(self, screen, max):
        tile_size = 80
        WIDTH = screen.get_width()
        HEIGHT = screen.get_height()
        if self.rect.centerx > 2*tile_size and self.rect.centerx < (WIDTH-2*tile_size) and self.rect.centery > 2*tile_size and self.rect.centery < (HEIGHT-2*tile_size):
            return max/2
        else:
            return max

    def bounce(self, bearingcar2, speedcar2):
        vx1_initial = self.speed * math.cos(math.radians(self.bearing))
        vy1_initial = self.speed * math.sin(math.radians(self.bearing))
        vx2_initial = speedcar2 * math.cos(math.radians(bearingcar2))
        vy2_initial = speedcar2 * math.sin(math.radians(bearingcar2))

        # Calculate the final velocities after an elastic collision
        vx1_final = ( 2  * vx2_initial) / (2)
        vy1_final = ( 2  * vy2_initial) / (2)

        # Calculate the final angles after the collision
        theta1_final = math.degrees(math.atan2(vy1_final, vx1_final))


        # Calculate the resultant velocity magnitudes
        v1_final = math.sqrt(vx1_final ** 2 + vy1_initial ** 2)


        self.speed = v1_final
        self.bearing = theta1_final





