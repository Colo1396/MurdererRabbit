import pygame,sys
import time
from pygame.locals import*
from random import randint

class Global(object):
    def __init__(self):
        self.level=0
        self.score=False
        self.newscore=False
