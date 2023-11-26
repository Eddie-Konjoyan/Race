import pygame
from random import randint

# this function will take 2 surface and center the 2nd surface on the first one
def center_surfaces(bg, fg):
    # get the bg width and height
    bg_width = bg.get_width()
    bg_height = bg.get_height()
    # get the front surface width and height
    fg_width = fg.get_width()
    fg_height = fg.get_height()
    # blit the text on the surface
    bg.blit(fg, (bg_width/2 - fg_width/2, bg_height/2-fg_height/2 ))

def make_background1(screen):
    scale = (80,80)
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    top_horizontal = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt04.png'),scale)
    bottom_horizontal = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt40.png'),scale)
    left_vert = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt21.png'),scale)
    right_vert = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt23.png'),scale)

    turn1_1 = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt10.png'), scale)
    turn1_2 = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt11.png'),scale)
    turn1_3 = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt29.png'),scale)
    turn1_inside = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt28.png'),scale)

    turn2_1 = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt47.png'),scale)
    turn2_2 = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt65.png'),scale)
    turn2_3 = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt64.png'),scale)
    turn2_inside = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt46.png'),scale)

    turn3_1 = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt63.png'),scale)
    turn3_2 = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt62.png'),scale)
    turn3_3 = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt44.png'),scale)
    turn3_inside = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt45.png'),scale)

    turn4_1 = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt26.png'),scale)
    turn4_2 = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt08.png'),scale)
    turn4_3 = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt09.png'),scale)
    turn4_inside = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt27.png'),scale)

# Start tiles
    start_top = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt87.png'),scale)
    start_bottom = pygame.transform.scale(pygame.image.load('PNG/Tiles/Asphalt road/road_asphalt89.png'),scale)
# Grass background
    grass = pygame.image.load('PNG/Tiles/grass/land_grass04.png')

    # get tile size info
    tile_width = grass.get_width()
    tile_height = grass.get_height()
    # make a background
    background = pygame.Surface((WIDTH,HEIGHT))
    # draw grass tiles
    for x in range(0,WIDTH,tile_width):
        for y in range(0,HEIGHT,tile_height):
            background.blit(grass, (x,y))


    # draw track
    track_width = turn1_1.get_width()
    track_height = turn1_1.get_height()
        #top left corner
    background.blit(turn4_2,(0,0))
    background.blit(turn4_1, (0,track_height))
    background.blit(turn4_3, (track_width, 0))
    background.blit(turn4_inside, (track_width, track_height))
        #middle leg
    i=2
    while i <= 7:
        background.blit(top_horizontal, (i*track_width, 0))
        background.blit(bottom_horizontal, (i*track_width, track_height))
        i+=1
        #start/finish line
    background.blit(start_top, (8*track_width,0))
    background.blit(start_bottom, (8*track_width,track_height))
        #middle leg cont
    i = 9
    while i <= 15:
        background.blit(top_horizontal, (i * track_width, 0))
        background.blit(bottom_horizontal, (i * track_width, track_height))
        i += 1
    background.blit(turn1_2, (17*track_width, 0))
    background.blit(turn1_1, (16*track_width, 0))
    background.blit(turn1_3, (17*track_width, track_height))
    background.blit(turn1_inside, (16*track_width, track_height))
        #left, right vert legs
    i= 2
    while i <= 7:
        background.blit(left_vert,(0,i*track_height))
        background.blit(left_vert,(16*track_width,i*track_height))
        background.blit(right_vert, (track_width, i * track_height))
        background.blit(right_vert, (17 * track_width, i * track_height))
        i+=1
        #bottom horizontal
    i = 2
    while i<16:
        background.blit(top_horizontal, (i * track_width, 8*track_height))
        background.blit(bottom_horizontal, (i * track_width, 9*track_height))
        i+=1
        # bottom right corner
    background.blit(turn2_2, (17 * track_width, 9*track_height))
    background.blit(turn2_1, (17 * track_width, 8*track_height))
    background.blit(turn2_3, (16 * track_width, 9*track_height))
    background.blit(turn2_inside, (16 * track_width, 8*track_height))
        #bottom left corner
    background.blit(turn3_2, (0, 9 * track_height))
    background.blit(turn3_1, (track_width, 9 * track_height))
    background.blit(turn3_3, (0, 8 * track_height))
    background.blit(turn3_inside, (track_width, 8 * track_height))

    return background


