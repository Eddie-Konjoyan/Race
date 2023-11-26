from background import *
from Car import Car
from helpers import *
import pygame
import math

from startfinish import Startfinish
from startfinish import Half
from barrier import *
import pygame_menu

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

barriers = makebarriers(screen)
barrier_group = pygame.sprite.Group()
for barrier in barriers:
    barrier_group.add(barrier)


half = Half(screen)
half_group = pygame.sprite.Group()
half_group.add(half)

#values for countdown function
countdown_values = ["READY...",3, 2, 1, "GO!"]
countdown_index = 0
countdown_timer = pygame.time.get_ticks()
countdown_interval = 1000  # 1 second

# Lap timer variables
laptimer = pygame.time.get_ticks()
timer_running = False
start_time = laptimer
end_time1= ""
end_time2 = ""
lap_time =0
ltimes1 = [0]
ltimes2 = [0]

# game loop
restart = False
loop = 0
running = True
start = 0
oner = False
twor = False
ret = False
car1lap =0
car1hl = 1
car2lap = 0
car2hl = 1
def startfunc(oner, twor, ret):
    return start_screen(screen, oner, twor, ret, font, WIDTH, HEIGHT)



def mainloop(countdown_index,countdown_timer,timer_running,car1lap,car2lap,car1hl,car2hl,end_time1,end_time2,start):
    if timer_running:
        bounce = 1
        if (pygame.sprite.collide_mask(car1, car2)):
            if bounce:
                # if cars collide, change eachothers bearings to the others
                (xdelta, ydelta, car2.bearing) = car1.bounce(car2.rect.centerx, car2.rect.centery,
                                                             car2.bearing, car2.speed)
                car2.rect.centerx += xdelta * 2
                car2.rect.centery += ydelta * 2
                bounce = 0
            else:
                pass
        for barrier in barrier_group:
            if (pygame.sprite.collide_mask(car1,barrier)):
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
            if car1hl == car1lap:
                car1hl+= 1
            else:
                pass
        if (pygame.sprite.groupcollide(car2_group,half_group, False, False)):

            if car2hl == car2lap:
                car2hl+= 1
            else:
                pass
        if (pygame.sprite.groupcollide(car1_group,startFinish_group, False, False)):
            print("1collide")
            nowtime1 = pygame.time.get_ticks()
            print(f'Car1lap: {car1lap}')
            print(f'Car1hl{car1hl}')
            if car1lap < 5:
                if car1hl == car1lap+1:

                    if 0 <= car1lap < 5:
                        print("func")
                        car1lap += 1
                        print(car1lap)

            elif car1lap ==5:
                end_time1= str(round(((pygame.time.get_ticks()-start_time)/1000),1))
                car1lap +=1
                car1.kill()

            else:
                pass
            print(f'Car1l2{car1lap}')
        if (pygame.sprite.groupcollide(car2_group,startFinish_group, False, False)):
            print("2collide")
            nowtime2 = pygame.time.get_ticks()

            if car2lap < 5:
                if car2hl == car2lap+1:

                    if 0 < car2lap < 5:
                        car2lap += 1
                    elif car2lap < 1:
                        car2lap += 1
            elif car2lap == 5:
                end_time2 = str(round(((pygame.time.get_ticks()-start_time)/1000),1))
                car2lap += 1
                car2.kill()
            else:
                pass
        if car1lap < 5:
            time = str(round(((pygame.time.get_ticks()-start_time)/1000),1))
            timer1 = font.render(time,
                                        True,
                                        (255, 255, 255))
            text_rect3 = timer1.get_rect(center=(WIDTH // 3, HEIGHT // 2))
            screen.blit(timer1, text_rect3)
        if car2lap < 5:
            time = str(round(((pygame.time.get_ticks()-start_time)/1000),1))
            timer2 = font.render(time,
                                        True,
                                        (255, 255, 255))
            text_rect4 = timer2.get_rect(center=(WIDTH*2 // 3, HEIGHT // 2))
            screen.blit(timer2, text_rect4)
        if 0 < car1lap < 5:
            text_surface1 = font.render(f"P1: LAP{car1lap}",
                                                True,
                                                (255, 255, 255))

            text_rect1 = text_surface1.get_rect(center=(WIDTH // 3, HEIGHT // 3))
            screen.blit(text_surface1, text_rect1)

        if car1lap < 1:


            text_surface1 = font.render("P1: LAP1",
                                            True,
                                            (255, 255, 255))
            text_rect1 = text_surface1.get_rect(center=(WIDTH // 3, HEIGHT // 3))
            screen.blit(text_surface1, text_rect1)
        if car1lap >= 5:

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
        if 0 < car2lap < 5:
            text_surface2 = font.render(f"P2: LAP{car2lap}",
                                        True,
                                        (255, 255, 255))

            text_rect2 = text_surface2.get_rect(center=(WIDTH*2 // 3, HEIGHT // 3))
            screen.blit(text_surface2, text_rect2)

        if car2lap < 1:

            text_surface2 = font.render("P2: LAP1",
                                        True,
                                        (255, 255, 255))
            text_rect2 = text_surface2.get_rect(center=(WIDTH*2 // 3, HEIGHT // 3))
            screen.blit(text_surface2, text_rect2)
        if car2lap >= 5:

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
            start = 2


    clock.tick(60)  # run at 60 FPS
    car1_group.update(screen)
    car2_group.update(screen)
    # draw the background on the screen

    barrier_group.draw(screen)
    car1_group.draw(screen)
    car2_group.draw(screen)

    return(car1lap,car2lap,car1hl,car2hl,end_time1,end_time2,start)
    # flip() the display to put your work on screen

def endfunc(restart,end_time1,end_time2):
        if end_time2 < end_time1:
            end_screen(screen, font, 2, end_time2, WIDTH, HEIGHT)
        elif end_time1 < end_time2:
            end_screen(screen, font, 1, end_time1, WIDTH, HEIGHT)
        else:
            end_screen_tie(screen, font, WIDTH, HEIGHT)



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

        """"DOESNT WORK ON RERUN
        -
        -
        -
        -
        -
        -
        -
        -
        -
        -
        --
        -
        -
        -
        -
        -
        -
        -
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
                countdown_text_render = font.render(countdown_text, True, (255, 0, 0))
                countdown_rect = countdown_text_render.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                screen.blit(countdown_text_render, countdown_rect)
        if countdown_index == len(countdown_values):
            if timer_running == False:
                start_time = pygame.time.get_ticks()
                timer_running = True
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

        car1lap,car2lap,car1hl,car2hl, end_time1,end_time2,start = mainloop(countdown_index, countdown_timer, timer_running, car1lap, car2lap, car1hl, car2hl, end_time1,
                 end_time2,start)
        print(f"Main loop lap1: {car1lap}")

    elif start == 2:
        endfunc(restart, end_time1, end_time2)


    pygame.display.flip()

pygame.quit()









