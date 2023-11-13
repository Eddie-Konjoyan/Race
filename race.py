from background import *
from Car import Car
import pygame
# pygame setup
pygame.init()
# make a clock
clock = pygame.time.Clock()

# set the resolution of our game window
WIDTH = 1440
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Make my background once
background = make_background1(screen)
#Make my car1
car1 = Car(screen,2,1)
car1_group = pygame.sprite.Group()
car1_group.add(car1)

#make car 2
car2 = Car(screen, 1,2)
car2_group = pygame.sprite.Group()
car2_group.add(car2)



# game loop
running = True
while running:
    # set max forward speed car1
    MAXf1 = 8
    # set max reverse speed car1
    MAXr1 = -4
    # set max forward speed car2
    MAXf2 = 8
    # set max reverse speed car2
    MAXr2 = -4




    # click to exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()
    #car1 controls
    if keys_pressed[pygame.K_LEFT]:
        car1.turn_left()
    if keys_pressed[pygame.K_RIGHT]:
        car1.turn_right()
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_DOWN]:
        if keys_pressed[pygame.K_UP]:
            MAXf1 = car1.track1_grass_slow(screen, MAXf1)
            car1.speed_upf(MAXf1)
        if keys_pressed[pygame.K_DOWN]:
            MAXr1 = car1.track1_grass_slow(screen, MAXr1)
            car1.speed_upr(MAXr1)
    else:
        car1.coast()
    #car2 controls
    if keys_pressed[pygame.K_a]:
        car2.turn_left()
    if keys_pressed[pygame.K_d]:
        car2.turn_right()
    if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_s]:
        if keys_pressed[pygame.K_w]:
            MAXf2 = car2.track1_grass_slow(screen, MAXf2)
            car2.speed_upf(MAXf2)
        if keys_pressed[pygame.K_s]:
            MAXr2 = car2.track1_grass_slow(screen, MAXr2)
            car2.speed_upr(MAXr2)
    else:
        car2.coast()

    if (pygame.sprite.groupcollide(car1_group, car2_group, False, False)):
        print("!")

        # if cars collide, change eachothers bearings to the others
        car2b = car2.bearing
        car2s = car2.speed
        car1b = car1.bearing
        car1s = car1.speed
        car1.bounce(car2b,car2s)
        car2.bounce(car1b,car1s)





    clock.tick(60)  # run at 60 FPS
    car1_group.update(screen)
    car2_group.update(screen)
    # draw the background on the screen
    screen.blit(background, (0, 0))
    car1_group.draw(screen)
    car2_group.draw(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()










