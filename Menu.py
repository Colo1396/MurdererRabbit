import pygame,sys
import time
from pygame.locals import*
from random import randint
from Puntero import*


pygame.init()
class Menu(pygame.sprite.Sprite):
    def __init__(self):
        self.jugar=pygame.image.load("imag/jugar.png")
        self.tutorial=pygame.image.load("imag/tutorial.png")
        self.puntaje=pygame.image.load("imag/puntaje.png")
        self.rectjugar=self.jugar.get_rect()
        self.rectjugar.left=199
        self.rectjugar.top=368
        self.recttutorial=self.tutorial.get_rect()
        self.recttutorial.left=451
        self.recttutorial.top=368
        self.rectpuntaje=self.puntaje.get_rect()
        self.rectpuntaje.left=322
        self.rectpuntaje.top=446
    def dibujar(self,ventana):
        ventana.blit(self.jugar,self.rectjugar)
        ventana.blit(self.tutorial,self.recttutorial)
        ventana.blit(self.puntaje,self.rectpuntaje)
