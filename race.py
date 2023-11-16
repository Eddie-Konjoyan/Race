from background import *
from Car import Car
from helpers import *
import pygame
import math
# pygame setup
pygame.init()
# make a clock
clock = pygame.time.Clock()

# init font
FONT_SIZE = 70
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
oner = False
twor = False
ret = False

while running:
    events = pygame.event.get()
    # click to exit
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    if start != True:
        start = start_screen(screen, oner, twor, ret, font, WIDTH, HEIGHT)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                 # User pressed the Enter key, exit the loop to start the game
                    oner = True

                if event.key == pygame.K_UP:
                    twor = True
                if event.key == pygame.K_RETURN:
                    ret = True



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

                        """
                        def elastic_collision(car1, car2):
                            mass = 10
                            relative_velocity = car2.velo - car1.velo
                            distance_vector = pygame.Vector2(car2.rect.center) - pygame.Vector2(car1.rect.center)
                            distance = distance_vector.length()

                            normal_vector = distance_vector.normalize()

                            # Elastic collision formula
                            impulse = 2 * mass * (relative_velocity.dot(normal_vector)) / (2 * mass)
                            car1.speed += impulse * normal_vector.magnitude()
                            car2.speed -= impulse * normal_vector.magnitude()
                            car1.bearing =  2 * normal_vector.as_polar()[1] -car1.bearing
                            car2.bearing = 2*  normal_vector.as_polar()[1] -car2.bearing
;
                        collisions = pygame.sprite.groupcollide(car1_group,car2_group,False, False)
                        for sprite in collisions:
                            elastic_collision(car1,car2)
                           
                                # Calculate the vector from ball1 to the other sprite
                                collision_vector = pygame.math.Vector2(car2.rect.center) - pygame.math.Vector2(
                                    car1.rect.center)

                                # Calculate the dot product to find the component of velocity along the collision vector
                                dot_product = collision_vector.x * car1.speed* math.cos((car1.bearing*math.pi)/180)+ collision_vector.y *  car1.speed* math.sin((car1.bearing*math.pi)/180)
                                # Adjust the velocity to eliminate the component along the collision vector
                                car1speedx = dot_product * collision_vector.x / collision_vector.length_squared()
                                car1speedy = dot_product * collision_vector.y / collision_vector.length_squared()
                                car1.speed -= math.sqrt((car1speedx**2)+(car1speedy**2)) /2
                                car2.velox +=
                                # Calculate the vector from ball1 to the other sprite
                            if sprite == car1:
                                collision_vector2 = pygame.math.Vector2(car1.rect.center) - pygame.math.Vector2(
                                    car2.rect.center)

                                # Calculate the dot product to find the component of velocity along the collision vector
                                dot_product2 = collision_vector2.x * car2.speed* math.cos((car2.bearing*math.pi)/180)+ collision_vector2.y *  car2.speed* math.sin((car2.bearing*math.pi)/180)

                                # Adjust the velocity to eliminate the component along the collision vector
                                car2speedx = dot_product2 * collision_vector2.x / collision_vector2.length_squared()
                                car2speedy = dot_product2 * collision_vector2.y / collision_vector2.length_squared()
                                car2.speed -= math.sqrt((car2speedx**2)+(car2speedy**2))
                               """

                clock.tick(60)  # run at 60 FPS
                car1_group.update(screen)
                car2_group.update(screen)
                # draw the background on the screen


                car1_group.draw(screen)
                car2_group.draw(screen)
                # flip() the display to put your work on screen



    pygame.display.flip()

pygame.quit()









