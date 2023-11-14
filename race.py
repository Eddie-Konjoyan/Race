from background import *
from Car import Car
import pygame
# pygame setup
pygame.init()
# make a clock
clock = pygame.time.Clock()

# init font
FONT_SIZE = 36
FONT_COLOR = (0, 0, 0)
font = pygame.font.Font(None, FONT_SIZE)
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
running = 1

while running == 2 :
    # click to exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                # User pressed the Enter key, exit the loop to start the game
                running = 1

    # Clear the screen
    screen.fill((0,0,0))

    # Render and display "ENTER TO CONTINUE" text
    text_surface = font.render("PRESS ENTER TO CONTINUE", True, (255,255,255))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

# Quit Pygame
pygame.quit()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

while running == 1:
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
            running = 0

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
    bounce = 1
    if (pygame.sprite.groupcollide(car1_group, car2_group, False, False)):
        print("!")
        if bounce:
            # if cars collide, change eachothers bearings to the others
            (xdelta, ydelta, car2.bearing) = car1.bounce(car2.rect.centerx,car2.rect.centery,car2.bearing,car2.speed)
            car2.rect.centerx += xdelta
            car2.rect.centery += ydelta
            bounce =0
        else:
            pass

    #lap counter
    """ 321 countdown to start
    if car passes start line, lap timer
        if continue timer from 0 on new line
    after x laps display finish times and winner
        """



    clock.tick(60)  # run at 60 FPS
    car1_group.update(screen)
    car2_group.update(screen)
    # draw the background on the screen
    screen.blit(background, (0, 0))
    #text = font.render(f"Time: {elapsed_time:.2f} seconds", True, FONT_COLOR)
   # screen.blit(text, (10, 10))
    car1_group.draw(screen)
    car2_group.draw(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()










