import pygame
import math

import background


class Car(pygame.sprite.Sprite):
    def __init__(self,screen,carnum,position):
        super().__init__()

        #scale car
        scale = (40,70)

        # Initialize car based off of player/color (carnum)
        if carnum ==1:
            self.image_o = pygame.transform.scale(pygame.image.load('PNG/Cars/car_black_5.png'),scale)
        if carnum ==2:
            self.image_o = pygame.transform.scale(pygame.image.load('PNG/Cars/car_blue_5.png'),scale)
        self.image_o = pygame.transform.rotate(self.image_o,-90)
        #^original image: never altered
        self.image = self.image_o
        # create rect obj for car
        self.rect = self.image.get_rect()

        #init starting spot based off of given position (player 1 and 2)
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
        """update the car each time the loop runs"""
        self.image = pygame.transform.rotate(self.image_o, self.bearing)
        # Assign new rect with current center.
        # Keep the image in center as the rect changes size.
        self.rect = self.image.get_rect(center=self.rect.center)
        #set velocity based on speed and given bearing
        self.velox = self.speed*math.cos((self.bearing*math.pi)/180)
        self.veloy = -self.speed*math.sin((self.bearing*math.pi)/180)
        #create velo vector2 (used for car on car collision pysics)
        self.velo = pygame.Vector2(self.velox,self.veloy)
        self.rect.x +=self.velo.x
        self.rect.y += self.velo.y

        #car does not go past border of screen
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
        """Turn car left 3 degrees"""
        self.bearing += 3

    def turn_right(self):
        """Turn car right 3 degrees"""
        self.bearing -= 3

    def speed_upf(self,max):
        """Slow down or speed up"""
        #speed up at a rate of .2 per loop until max speed is reached
        if self.speed < max:
            self.speed += .2
        if self.speed > max:
            self.speed = max
    def coast(self):
        """Slow down or speed up"""
        #if speed is positive, slow down at a rate of .1 per loop until speed is 0
        if self.speed > 0:
            self.speed -= .1
        #if speed is negative, slow down at a rate of .2 per loop until speed is 0
        if self.speed < 0:
            self.speed += .2
        if self.speed == 0:
            self.speed =0

    def speed_upr(self,max):
        """Slow down or speed up"""
        #speed up in the reverse direction at a rate of .2 per loop until max reverse speed is reached
        if self.speed > max:
            self.speed -=.2
        if self.speed < max:
            self.speed = max
    def track1_grass_slow(self, screen, max):
        """slows the car's max speed down by half when on the grass in middle of the track"""
        tile_size = 80
        WIDTH = screen.get_width()
        HEIGHT = screen.get_height()
        if self.rect.centerx > 2*tile_size and self.rect.centerx < (WIDTH-2*tile_size) and self.rect.centery > 2*tile_size and self.rect.centery < (HEIGHT-2*tile_size):
            return max/2
        else:
            return max

    def bounce(self, xcenter2, ycenter2,bearingcar2, speedcar2): #bounce function
        """Contains bounce physics for car on car collisions"""
        elasticity = 5 #elasticity constant
        speedcar1 = self.speed

        #distance between the cars
        dx = self.rect.centerx - xcenter2
        dy = self.rect.centery - ycenter2

        #tangent of the two cars collision
        tangent = math.atan2(dy, dx)

        #if sin/cos tanent is within ____ then change to ___ to create wanted outcome
        if  math.sin(tangent) >.9 and math.cos(tangent)>0:
            tangent = 30
        if  math.sin(tangent) >.9 and math.cos(tangent)<0:
            tangent = -30

        #physics
        self.bearing = 2 * tangent - self.bearing
        p2angle = 2 * tangent - bearingcar2
        (speedcar1, speedcar2) = (speedcar2,speedcar1)
        speedcar1 *= elasticity
        speedcar2 *= elasticity
        angle = 0.5 * math.pi + tangent

        #set new angles and speeds
        self.rect.centerx += math.sin(angle)
        self.rect.centery -= math.cos(angle)
        p2x = -math.sin(angle)
        p2y = math.cos(angle)
        return p2x, p2y, p2angle


