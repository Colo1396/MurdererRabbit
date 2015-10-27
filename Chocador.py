import pygame,sys
import time
from pygame.locals import*
from random import randint

class Chocador(pygame.sprite.Sprite):
    def __init__(self,posicion):
        self.imagenChocador=pygame.image.load("imag/chocador.png")
        self.rectChocador=self.imagenChocador.get_rect()
        self.velocidad = randint(3,4)
        self.hayChocador = False
        self.posicion= posicion
        self.sonidoChoque= pygame.mixer.Sound("sonidos/choque.ogg")     
        self.sonidoChoque.set_volume(0.05)
    def movimiento(self,ventana):
        if self.hayChocador == True:
            self.rectChocador.top=self.rectChocador.top + self.velocidad
            self.dibujar(ventana)
            self.seFue()
        else:
            pass
    def dibujar(self,ventana):
        ventana.blit(self.imagenChocador,self.rectChocador)
    def seFue(self):
        if self.rectChocador.top > 600:
            self.hayChocador= False
        
    def llamarChocador(self,num):
        
        if self.hayChocador== False:
            tz= randint(1,100)
            if tz == 5:
                if num==1:
                    posX= 200
                    posY= 80
                    self.hayChocador= True
                elif num==2:
                    posX= 370
                    posY = 80
                    self.hayChocador= True
                elif num== 3:
                    posX = 550
                    posY= 80
                    self.hayChocador= True
                if self.hayChocador==True:
                    self.rectChocador.left=posX
                    self.rectChocador.top=posY
                self.retardoChocador=0
        else:
            pass
        
                
            
   
