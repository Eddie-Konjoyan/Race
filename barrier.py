import pygame
import math

import background


class Barrier(pygame.sprite.Sprite):
    def __init__(self, rotation,x,y):
        super().__init__()
        scale = (190, 40)
        self.image_o = pygame.transform.scale(pygame.image.load('PNG/Objects/barrier_red.png'),scale)
        self.image = pygame.transform.rotate(self.image_o,rotation)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
def makebarriers(screen):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    barriers = []
    barrier1 = Barrier(0,(WIDTH/2 +30),190)
    barrier2 = Barrier(0,(WIDTH/2 - 200), 190)
    barrier3 = Barrier(0, (WIDTH / 2 - 440), 190)
    barrier4 = Barrier(0, (WIDTH / 2 +260), 190)

    barrier5 = Barrier(0, (WIDTH / 2 +30), HEIGHT-230)
    barrier6 = Barrier(0, (WIDTH / 2 - 200), HEIGHT-230)
    barrier7 = Barrier(0, (WIDTH / 2 - 440), HEIGHT-230)
    barrier8 = Barrier(0, (WIDTH / 2 + 260), HEIGHT-230)

    barrier9 = Barrier(90, 190, 190)
    barrier10 = Barrier(90, 190, 420)


    barrier11 = Barrier(90, WIDTH-245, 190)
    barrier12 = Barrier(90, WIDTH-245, 420)

    barriers.append(barrier1)
    barriers.append(barrier2)
    barriers.append(barrier3)
    barriers.append(barrier4)

    barriers.append(barrier5)
    barriers.append(barrier6)
    barriers.append(barrier7)
    barriers.append(barrier8)

    barriers.append(barrier9)
    barriers.append(barrier10)

    barriers.append(barrier11)
    barriers.append(barrier12)

    return barriers