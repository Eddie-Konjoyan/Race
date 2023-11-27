import pygame
import math
from background import *

import background


class Startfinish(pygame.sprite.Sprite):
    """Creates an invisible start/finish line sprite."""
    def __init__(self,screen):
        super().__init__()
        WIDTH = screen.get_width()
        self.rect = (((WIDTH/2)-5),0,10,160)

class Half(pygame.sprite.Sprite):
    """Creates an invisible halfway around the track line sprite."""
    def __init__(self,screen):
        super().__init__()
        WIDTH = screen.get_width()
        HEIGHT = screen.get_height()
        self.rect = (((WIDTH/2)-5),(HEIGHT-160),10,160)