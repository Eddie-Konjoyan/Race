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
car1 = Car(screen,2)
car1_group = pygame.sprite.Group()
car1_group.add(car1)

# game loop
running = True
while running:
    # click to exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_LEFT]:
        car1.turn_left()
    if keys_pressed[pygame.K_RIGHT]:
        car1.turn_right()
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_DOWN]:
        if keys_pressed[pygame.K_UP]:
            car1.speed_upf()
        if keys_pressed[pygame.K_DOWN]:
            car1.speed_upr()
    else:
        car1.coast()


    clock.tick(60)  # run at 60 FPS
    car1_group.update()
    # draw the background on the screen
    screen.blit(background, (0, 0))
    car1_group.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()









