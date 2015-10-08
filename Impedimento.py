import pygame,sys
import time
from pygame.locals import*
from random import randint

pygame.init()
class Impedimento(pygame.sprite.Sprite):
    def __init__(self,Xaux,Yaux,ID):
        self.IDnumero=ID
        self.yuyo = pygame.image.load("imag/impedimento.png")
        self.rectyuyo=self.yuyo.get_rect()
        self.corrimientoX=10
        self.corrimientoY=148
        self.rectyuyo.left=Xaux+self.corrimientoX
        self.rectyuyo.top=Yaux+self.corrimientoY

    def dibujarImpedimento(self,ventana):
        ventana.blit(self.yuyo,self.rectyuyo)

class AppenImpedimento(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.listaImpedimento=[]
        self.i=0
    def dibujarAppenImpedimento(self):
        self.coordenadasX=[50,115,115,275,300,450,450,620,620,680]
        self.coordenadasY=[200,70,320,145,380,35,270,120,350,230]
        for self.i in range (10):
            bloque=Impedimento(self.coordenadasX[self.i],self.coordenadasY[self.i],self.i)
            self.listaImpedimento.append(bloque)


