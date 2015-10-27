import pygame,sys
import time
from pygame.locals import*
from random import randint

class Puntero(pygame.sprite.Sprite):
    def __init__(self):
        self.imagpuntero=pygame.image.load("imag/puntero.png")
        self.rectimagpuntero=self.imagpuntero.get_rect()
        self.rectimagpuntero.left=0
        self.rectimagpuntero.top=0
    def dibujar(self,ventana,posX,posY):
        self.rectimagpuntero.left=posX
        self.rectimagpuntero.top=posY
        ventana.blit(self.imagpuntero,self.rectimagpuntero)
