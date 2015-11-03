import pygame,sys
import time
from pygame.locals import*
from random import randint
from Puntero import*


class Menu(pygame.sprite.Sprite):
    def __init__(self):
        self.jugar=pygame.image.load("imag/jugar.png")
        self.tutorial=pygame.image.load("imag/tutorial.png")
        self.puntaje=pygame.image.load("imag/puntaje.png")
        
        self.imagTutorial= pygame.image.load("imag/tutorial1.jpg")
        self.rectTutorial= self.imagTutorial.get_rect()
        self.rectTutorial.top = 0   # cambiar posicion
        self.rectTutorial.left = 0  #cambiar posicion
        self.estaTutorial = True
        self.back = pygame.image.load("imag/back.png")
        self.rectBack= self.back.get_rect()
        self.rectBack.left= 560
        self.rectBack.top= 415
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

    def ElTutorial(self,ventana,Raton):
        self.estaTutorial= True
        while self.estaTutorial== True:
            ventana.blit(self.imagTutorial,(0,0))
            ventana.blit(self.back,(self.rectBack))
            posX,posY=pygame.mouse.get_pos()
            Raton.dibujar(ventana,posX,posY)
            for evento in pygame.event.get():             
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if Raton.rectimagpuntero.colliderect(self.rectBack):
                    if pygame.mouse.get_pressed()==(1,0,0):
                        self.estaTutorial=False

            pygame.display.update()


            

            
