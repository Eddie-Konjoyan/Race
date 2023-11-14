from background import *
from Car import Car
import pygame
# pygame setup
pygame.init()
# make a clock
clock = pygame.time.Clock()

# init font
FONT_SIZE = 100
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


countdown_values = ["READY...",3, 2, 1, "GO!"]
countdown_index = 0
countdown_timer = pygame.time.get_ticks()
countdown_interval = 1000  # 1 second

# Lap timer variables
timer_running = False
start_time = 0
lap_times = []

# game loop
running = True
start = False

while running:
    events = pygame.event.get()
    # click to exit
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    if start == False:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        # User pressed the Enter key, exit the loop to start the game
                        start = True

            # Clear the screen
            screen.fill((0,0,0))

            # Render and display "ENTER TO CONTINUE" text
            text_surface = font.render("PRESS ENTER TO CONTINUE", True, (255,255,255))
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text_surface, text_rect)
    else:

                # set max forward speed car1
                MAXf1 = 8
                # set max reverse speed car1
                MAXr1 = -4
                # set max forward speed car2
                MAXf2 = 8
                # set max reverse speed car2
                MAXr2 = -4


                keys_pressed = pygame.key.get_pressed()
                #car1 controls

                if keys_pressed[pygame.K_SPACE]:
                    if not timer_running:
                        # Start the countdown
                        countdown_index = 0
                        countdown_timer = pygame.time.get_ticks()


               # if car1_group or car2_grou
                    # Stop the timer and record lap time
                  #  timer_running = False
                  #  lap_time = pygame.time.get_ticks() - start_time
                 #   lap_times.append(lap_time)
                """ 321 countdown to start
                if car passes start line, lap timer
                    if continue timer from 0 on new line
                after x laps display finish times and winner
                    """
                screen.blit(background, (0, 0))
                if not timer_running and countdown_index < len(countdown_values):
                    # Display countdown
                    current_time = pygame.time.get_ticks()
                    if current_time - countdown_timer >= countdown_interval:
                        countdown_timer = current_time
                        countdown_index += 1

                    if countdown_index < len(countdown_values):
                        countdown_text = str(countdown_values[countdown_index])
                        countdown_text_render = font.render(countdown_text, True, (255,0,0))
                        countdown_rect = countdown_text_render.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                        screen.blit(countdown_text_render, countdown_rect)
                if countdown_index == len(countdown_values):
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
                        # car2 controls
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
                            if bounce:
                                # if cars collide, change eachothers bearings to the others
                                (xdelta, ydelta, car2.bearing) = car1.bounce(car2.rect.centerx, car2.rect.centery,
                                                                             car2.bearing, car2.speed)
                                car2.rect.centerx += xdelta * 3
                                car2.rect.centery += ydelta * 3
                                bounce = 0
                            else:
                                pass



                clock.tick(60)  # run at 60 FPS
                car1_group.update(screen)
                car2_group.update(screen)
                # draw the background on the screen


                car1_group.draw(screen)
                car2_group.draw(screen)
                # flip() the display to put your work on screen



    pygame.display.flip()

pygame.quit()









