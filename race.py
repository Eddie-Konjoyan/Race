import pygame.time

from background import *
from car import Car
from menus import *


from startfinish import Startfinish
from startfinish import Half
from barrier import *


# pygame setup
pygame.init()
# make a clock
clock = pygame.time.Clock()

# init font
FONT_SIZE = 70


font = pygame.font.Font("Teko-Regular.ttf", FONT_SIZE)
countdown = pygame.font.Font("Teko-Regular.ttf", 150)
# set the resolution of our game window
WIDTH = 1440
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Make my background once
background = make_background1(screen)
#Make car1
car1 = Car(screen,2,1)
car1_group = pygame.sprite.Group()
car1_group.add(car1)

#make car 2
car2 = Car(screen, 1,2)
car2_group = pygame.sprite.Group()
car2_group.add(car2)

# make invisible start/finish line
startFinish = Startfinish(screen)
startFinish_group = pygame.sprite.Group()
startFinish_group.add(startFinish)

# make barriers
barriers = makebarriers(screen)
barrier_group = pygame.sprite.Group()
for barrier in barriers:
    barrier_group.add(barrier)

# make invisible half lap line
half = Half(screen)
half_group = pygame.sprite.Group()
half_group.add(half)

#values for countdown function
countdown_values = ["READY...",3, 2, 1, "GO!"]
countdown_index = 0
countdown_timer = pygame.time.get_ticks()
countdown_interval = 1000  # 1 second

# Lap timer variables
timer_running = False
start_time = pygame.time.get_ticks()
end_time1= ""
end_time2 = ""


#init loop variables
loop = 0
running = True
start = 0

#for start screen
oner = False
twor = False
ret = False

#for lap counter
car1lap =0
car1hl = 1
car2lap = 0
car2hl = 1
newhs = False

#kill cars?
kill1 = False
kill2 = False

#bounce timer (only certian number of bounces per time frame
bounce_t = pygame.time.get_ticks()
def startfunc(oner, twor, ret):
    """Calls the start screen"""
    return start_screen(screen, oner, twor, ret, font, WIDTH, HEIGHT)



def mainloop(bounce_t,kill1,kill2,countdown_index,countdown_timer,timer_running,car1lap,car2lap,car1hl,car2hl,end_time1,end_time2,start):
    """Main loop
        runs while race is occuring"""
    if timer_running:
        if kill1 == False and kill2 == False:
            if (pygame.sprite.collide_mask(car1, car2)):
                bounce_tn = pygame.time.get_ticks()
                if bounce_tn>bounce_t+150:
                    bounce_t=bounce_tn
                  #collision between masks of the two cars
                   # if cars collide run bounce function
                    (xdelta, ydelta, car2.bearing) = car1.bounce(car2.rect.centerx, car2.rect.centery,
                                                                 car2.bearing, car2.speed)
                    #separate cars to prevent loss of control
                    car2.rect.centerx += xdelta * 2
                    car2.rect.centery += ydelta * 2

        for barrier in barrier_group:
            if (pygame.sprite.collide_mask(car1,barrier)):
                #if the mask of the car collides with the barrier

                #for each region of car 1 colliding with the barrier(4), and both directions of travel(2) for each region (8 tot)
                #make car parallel to the barrier in direction of travel
                # move car 1 off barrier to ensure no getting stuck
                if car1.rect.centerx < 190 and 190 < car1.rect.centery < HEIGHT - 190 and 0 <= math.sin(
                        (car1.bearing*math.pi)/180) <= 1:
                    car1.bearing = 90
                    car1.speed = .2 * car1.speed
                    car1.rect.centerx-=2

                elif car1.rect.centerx < 190 and 190 < car1.rect.centery < HEIGHT - 190 and -1 <= math.sin(
                        (car1.bearing*math.pi)/180) < 0:
                    car1.bearing = -90
                    car1.speed = .2 * car1.speed
                    car1.rect.centerx -= 2
                elif car1.rect.centerx > WIDTH - 190 and 190 < car1.rect.centery < HEIGHT - 190 and 0 <= math.sin(
                        (car1.bearing * math.pi) / 180) <= 1:
                    car1.bearing = 90
                    car1.speed = .2 * car1.speed
                    car1.rect.centerx += 2

                elif car1.rect.centerx > WIDTH - 190 and 190 < car1.rect.centery < HEIGHT - 190 and -1 <= math.sin(
                        (car1.bearing * math.pi) / 180) < 0:
                    car1.bearing = -90
                    car1.speed = .2 * car1.speed
                    car1.rect.centerx += 2
                elif 190 > car1.rect.centery and 190 < car1.rect.centerx < WIDTH - 190 and 0 <= math.cos(
                        (car1.bearing * math.pi) / 180)  <= 1:
                    car1.bearing = 0
                    car1.speed = .2 * car1.speed
                    car1.rect.centery -= 2
                elif 190 > car1.rect.centery and 190 < car1.rect.centerx < WIDTH - 190 and -1 <= math.cos(
                        (car1.bearing * math.pi) / 180) < 0:
                    car1.bearing = 180
                    car1.speed = .2 * car1.speed
                    car1.rect.centery -=2
                elif HEIGHT - 190 < car1.rect.centery and 190 < car1.rect.centerx < WIDTH - 190 and 0 <= math.cos(
                        (car1.bearing * math.pi) / 180) <= 1:
                    car1.bearing = 0
                    car1.speed = .2 * car1.speed
                    car1.rect.centery +=2
                elif HEIGHT - 190 < car1.rect.centery and 190 < car1.rect.centerx < WIDTH - 190 and -1 <= math.cos(
                        (car1.bearing * math.pi) / 180) < 0:
                    car1.bearing = 180
                    car1.speed = .2 * car1.speed
                    car1.rect.centery +=2

            if (pygame.sprite.collide_mask(car2,barrier)):
                # if the mask of the car collides with the barrier

                # for each region of car 2 colliding with the barrier(4), and both directions of travel(2) for each region (8 tot)
                # make car parallel to the barrier in direction of travel
                # move car 2 off barrier to ensure no getting stuck
                if car2.rect.centerx< 190 and 190 < car2.rect.centery < HEIGHT - 190 and 0 <= math.sin((car2.bearing * math.pi) / 180) <= 1:
                    car2.bearing = 90
                    car2.speed = .2 * car2.speed
                    car2.rect.centerx -= 2

                elif car2.rect.centerx < 190 and 190 < car2.rect.centery < HEIGHT - 190 and -1 <= math.sin((car2.bearing * math.pi) / 180) < 0:
                    car2.bearing = -90
                    car2.speed = .2 * car2.speed
                    car2.rect.centerx -= 2

                elif car2.rect.centerx > WIDTH-190 and 190 < car2.rect.centery < HEIGHT - 190 and 0 <= math.sin((car2.bearing * math.pi) / 180) <= 1:
                    car2.bearing = 90
                    car2.speed = .2 * car2.speed
                    car2.rect.centerx += 2

                elif car2.rect.centerx > WIDTH-190 and 190 < car2.rect.centery < HEIGHT - 190 and -1 <= math.sin((car2.bearing * math.pi) / 180) < 0:
                    car2.bearing = -90
                    car2.speed = .2 * car2.speed
                    car2.rect.centerx += 2
                elif 190 > car2.rect.centery and 190 < car2.rect.centerx < WIDTH - 190 and 0 <= math.cos((car2.bearing * math.pi) / 180) <= 1:
                    car2.bearing = 0
                    car2.speed = .2 * car2.speed
                    car2.rect.centery -= 2
                elif 190 > car2.rect.centery and 190 < car2.rect.centerx < WIDTH - 190 and -1 <= math.cos((car2.bearing * math.pi) / 180) < 0:
                    car2.bearing = 180
                    car2.speed = .2 * car2.speed
                    car2.rect.centery -= 2
                elif HEIGHT-190 < car2.rect.centery and 190 < car2.rect.centerx < WIDTH - 190 and 0 <= math.cos((car2.bearing * math.pi) / 180) <= 1:
                    car2.bearing = 0
                    car2.speed = .2 * car2.speed
                    car2.rect.centery += 2
                elif HEIGHT-190 < car2.rect.centery and 190 < car2.rect.centerx < WIDTH - 190 and -1 <= math.cos((car2.bearing * math.pi) / 180) < 0:
                    car2.bearing = 180
                    car2.speed = .2 * car2.speed
                    car2.rect.centery += 2
        if (pygame.sprite.groupcollide(car1_group,half_group, False, False)):
            #Car 1 collides with the halfway mark, increasing the halflap variable
            if car1hl == car1lap:
                car1hl+= 1
            else:
                pass
        if (pygame.sprite.groupcollide(car2_group,half_group, False, False)):
            # Car 2 collides with the halfway mark, increasing the halflap variable
            if car2hl == car2lap:
                car2hl+= 1
            else:
                pass
        if (pygame.sprite.groupcollide(car1_group,startFinish_group, False, False)):
            #Car 1 collides with the start line
            if car1lap < 6:
                #if car lap is less than 6, and the car has passed finish, increase the lap by one
                if car1hl == car1lap+1:
                    if 0 <= car1lap < 6:
                        car1lap += 1

            elif car1lap ==6:
                #if the car has completed 5 laps and passes finish end car1's time, increase the lap, and then kill the car
                end_time1= str(round(((pygame.time.get_ticks()-start_time)/1000),1))
                car1lap +=1
                kill1 = True

            else:
                pass
        if (pygame.sprite.groupcollide(car2_group,startFinish_group, False, False)):
            #Car 2 collides with the start line
            if car2lap < 6:
                #if car lap is less than 6, and the car has passed finish, increase the lap by one
                if car2hl == car2lap+1:
                    if 0 <= car2lap < 6:
                        car2lap += 1

            elif car2lap == 6:
                #if the car has completed 5 laps and passes finish end car2's time, increase the lap, and then kill the car
                end_time2 = str(round(((pygame.time.get_ticks()-start_time)/1000),1))
                car2lap += 1
                kill2 = True
            else:
                pass
        if car1lap < 6:
            #display timer
            time = str(round(((pygame.time.get_ticks()-start_time)/1000),1))
            timer1 = font.render(time,
                                        True,
                                        (255, 255, 255))
            text_rect3 = timer1.get_rect(center=(WIDTH // 3, HEIGHT // 2))
            screen.blit(timer1, text_rect3)
        if car2lap < 6:
            #display timer
            time = str(round(((pygame.time.get_ticks()-start_time)/1000),1))
            timer2 = font.render(time,
                                        True,
                                        (255, 255, 255))
            text_rect4 = timer2.get_rect(center=(WIDTH*2 // 3, HEIGHT // 2))
            screen.blit(timer2, text_rect4)
        if 0 < car1lap < 6:
            #display the lap number
            text_surface1 = font.render(f"P1: LAP {car1lap}/5",
                                                True,
                                                (255, 255, 255))

            text_rect1 = text_surface1.get_rect(center=(WIDTH // 3, HEIGHT // 3))
            screen.blit(text_surface1, text_rect1)

        if car1lap < 1:
            #display first lap
            text_surface1 = font.render("P1: LAP 1/5",
                                            True,
                                            (255, 255, 255))
            text_rect1 = text_surface1.get_rect(center=(WIDTH // 3, HEIGHT // 3))
            screen.blit(text_surface1, text_rect1)
        if car1lap >= 6:
            #display car1 as finished
            text_surface1 = font.render("P1: FINISH",
                                        True,
                                        (255, 255, 255))
            text_rect1 = text_surface1.get_rect(center=(WIDTH // 3, HEIGHT // 3))
            screen.blit(text_surface1, text_rect1)
            timer1 = font.render(end_time1,
                                 True,
                                 (255, 255, 255))
            text_rect3 = timer1.get_rect(center=(WIDTH // 3, HEIGHT // 2))
            screen.blit(timer1, text_rect3)
        if 0 < car2lap < 6:
            #display lap
            text_surface2 = font.render(f"P2: LAP {car2lap}/5",
                                        True,
                                        (255, 255, 255))

            text_rect2 = text_surface2.get_rect(center=(WIDTH*2 // 3, HEIGHT // 3))
            screen.blit(text_surface2, text_rect2)

        if car2lap < 1:
            #display lap 1
            text_surface2 = font.render("P2: LAP 1/5",
                                        True,
                                        (255, 255, 255))
            text_rect2 = text_surface2.get_rect(center=(WIDTH*2 // 3, HEIGHT // 3))
            screen.blit(text_surface2, text_rect2)
        if car2lap >= 6:
            #display finish
            text_surface2 = font.render("P2: FINISH",
                                        True,
                                        (255, 255, 255))
            text_rect2 = text_surface2.get_rect(center=(WIDTH*2 // 3, HEIGHT // 3))
            screen.blit(text_surface2, text_rect2)
            timer2 = font.render(end_time2,
                                 True,
                                 (255, 255, 255))
            text_rect4 = timer2.get_rect(center=(WIDTH * 2 // 3, HEIGHT // 2))
            screen.blit(timer2, text_rect4)
        if end_time2 and end_time1:
            #if both cars are finished, exit the main loop and enter the finish loop.
            start = 2


    clock.tick(60)  # run at 60 FPS
    car1_group.update(screen)
    car2_group.update(screen)
    # draw the background on the screen

    barrier_group.draw(screen)
    car1_group.draw(screen)
    car2_group.draw(screen)

    return(bounce_t,car1lap,car2lap,car1hl,car2hl,end_time1,end_time2,start,kill1,kill2)


def endfunc(newhs,end_time1,end_time2):

        #if car2 won check to see if new highscore (if new write to file), then display end screen
        if end_time2 < end_time1:
            with open('highscore') as hs:
                contents = hs.read()
            if float(end_time2) < float(contents):
                with open('highscore', 'w') as file_object:
                    file_object.write(end_time2)
                newhs = True
            end_screen(newhs,screen, font, 2, end_time2, WIDTH, HEIGHT)

        # if car1 won check to see if new highscore (if new write to file), then display end screen
        elif end_time1 < end_time2:
            with open('highscore') as hs:
                contents = hs.read()
            if float(end_time1) < float(contents):
                with open('highscore', 'w') as file_object:
                    file_object.write(end_time1)
                newhs = True
            end_screen(newhs,screen, font, 1, end_time1, WIDTH, HEIGHT)

        # if tie check to see if new highscore (if new write to file), then display end screen for a tie
        else:
            with open('highscore') as hs:
                contents = hs.read()
            if float(end_time1) < float(contents):
                with open('highscore', 'w') as file_object:
                    file_object.write(end_time1)
                newhs = True
            end_screen_tie(newhs,screen,end_time1, font, WIDTH, HEIGHT)



#Main game running loop
while running:

    events = []
    events = pygame.event.get()
    # click to exit
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if start == 0: #start screen
        start = startfunc(oner, twor, ret)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    # User pressed the Enter key, inticator true
                    oner = True

                if event.key == pygame.K_UP:
                    # user pressed the up key, indicator true
                    twor = True
                if event.key == pygame.K_RETURN:
                    # user pressed the return key, indicator true
                    ret = True

    elif start == 1 :
        if kill1:
            car1.kill()
        if kill2:
            car2.kill()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            if not timer_running:
                # Start the countdown
                countdown_index = 0
                countdown_timer = pygame.time.get_ticks()

        # set max forward speed car1
        MAXf1 = 8
        # set max reverse speed car1
        MAXr1 = -4
        # set max forward speed car2
        MAXf2 = 8
        # set max reverse speed car2
        MAXr2 = -4

        # car1 controls



        screen.blit(background, (0, 0))
        if not timer_running and countdown_index < len(countdown_values):
            # Display countdown
            current_time = pygame.time.get_ticks()
            if current_time - countdown_timer >= countdown_interval:
                countdown_timer = current_time
                countdown_index += 1
            #displays coundown
            if countdown_index < len(countdown_values):
                countdown_text = str(countdown_values[countdown_index])
                countdown_text_render = countdown.render(countdown_text, True, (255, 255,255))
                countdown_rect = countdown_text_render.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                screen.blit(countdown_text_render, countdown_rect)
        if countdown_index == len(countdown_values):
            #starts race
            if timer_running == False:
                start_time = pygame.time.get_ticks()
                timer_running = True
            if keys_pressed[pygame.K_LEFT]:
                car1.turn_left()
            if keys_pressed[pygame.K_RIGHT]:
                car1.turn_right()
            if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_DOWN]:
                if keys_pressed[pygame.K_UP]:
                    #speed up to the max speed dertermined by if on grass or not
                    MAXf1 = car1.track1_grass_slow(screen, MAXf1)
                    car1.speed_upf(MAXf1)
                if keys_pressed[pygame.K_DOWN]:
                    # speed up to the max speed dertermined by if on grass or not
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
                    # speed up to the max speed dertermined by if on grass or not
                    MAXf2 = car2.track1_grass_slow(screen, MAXf2)
                    car2.speed_upf(MAXf2)
                if keys_pressed[pygame.K_s]:
                    # speed up to the max speed dertermined by if on grass or not
                    MAXr2 = car2.track1_grass_slow(screen, MAXr2)
                    car2.speed_upr(MAXr2)
            else:
                car2.coast()
        #run main loop code
        bounce_t,car1lap, car2lap,car1hl,car2hl, end_time1,end_time2,start,kill1,kill2 = mainloop(bounce_t,kill1,kill2,countdown_index, countdown_timer, timer_running, car1lap, car2lap, car1hl, car2hl, end_time1,end_time2,start)

    elif start == 2:
        #run endfunc code
        endfunc(newhs, end_time1, end_time2)

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()









