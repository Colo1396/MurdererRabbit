import pygame,sys
import time
from pygame.locals import*
from random import randint

pygame.init()
class Barra(pygame.sprite.Sprite):
    def __init__(self):
        self.colorRect=(100,255,100)
        self.valorx=316

        self.barra=pygame.image.load("imag/barra.png")
        self.rectbarra=self.barra.get_rect()
        self.rectbarra.left=15
        self.rectbarra.top=15

    def dibujarBarra(self,ventana):
        if self.valorx > 316:
            self.valorx = 316
        if self.valorx < 0:
            self.valorx = 0
        #COMPROBAR COLORES PARA BARRA
        if self.valorx >=200:
            self.colorRect=(175,250,100)
        elif self.valorx >= 175:
            self.colorRect=(225,250,100)
        elif self.valorx >= 150:
            self.colorRect=(250,250,100)
        elif self.valorx >= 125:
            self.colorRect=(250,230,75)
        elif self.valorx >= 100:
            self.colorRect=(255,210,60)
        elif self.valorx >= 75:
            self.colorRect=(255,150,40)
        elif self.valorx >= 50:
            self.colorRect=(255,110,60)
        elif self.valorx >= 30:
            self.colorRect=(255,50,2)
        else:
            self.colorRect=(255,0,0)
        self.Rectangulo=pygame.draw.rect(ventana,self.colorRect,(15,15,self.valorx,36))
        ventana.blit(self.barra,self.rectbarra)
