# -*- coding: cp1252 -*-
import pygame,sys
import time
from pygame.locals import*
from random import randint



from Vidas import *
from Menu import*
from Global import*
from Funciones import*
from level1 import*

## Variables Globales

ancho = 800
alto = 600
ventana =pygame.display.set_mode((ancho,alto))

######### Funcion intro: 3 segundos#######
def intro():
        global ventana
        fond=pygame.image.load("imag/fondo1.jpg")
        PJ= pygame.image.load("imag/z/zi1.png")
        rect= PJ.get_rect()
        rect.left=325
        rect.top=200
        tiempo=0
        Fuente = pygame.font.Font('fonts/fuentefavorita.ttf',80)
        fuenteNumero = pygame.font.SysFont('fonts/fuentefavorita.ttf',50)
        preparado = fuenteNumero.render("Comenzando en",0,(0,20,255))
        while tiempo < 800:
                ventana.blit(fond,(0,0))
                ventana.blit(PJ,rect)
                tiempo = tiempo + 1
                if tiempo < 200:
                        ventana.blit(preparado,(270,30))
                        contador= Fuente.render(" 3 ",0,(255,0,0))
                        
                elif tiempo < 400:
                        ventana.blit(preparado,(270,30))
                        contador= Fuente.render(" 2 ",0,(255,255,0))
                elif tiempo < 600:
                        ventana.blit(preparado,(270,30))
                        contador= Fuente.render(" 1 ",0,(0,255,0))
                elif tiempo < 800:
                        contador= Fuente.render("A darle caña!!!",0,(255,160,0))
                if tiempo < 600:
                        ventana.blit(contador,(350,150))
                else:
                        ventana.blit(contador,(270,100))
                pygame.display.update() 

   
######TERMINAN LAS CLASES Y ARRANCAN LAS VARIABLES##########
def main():
        pygame.init()
        global ventana
        Global.level=0
        pygame.mixer.music.load("sonidos/Malmen Facing TheSky.ogg")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.3)


        pygame.display.set_caption("The Murderer Plant")
        fondoini=pygame.image.load("imag/tapa.jpg")
        fondo=pygame.image.load("imag/fondo1.jpg")
        
        Tapa=Menu()
       
        Raton=Puntero()
        while True:
                pygame.mouse.set_visible(False)
                while Global.level==0:
                        ventana.blit(fondoini,(0,0))
                        Tapa.dibujar(ventana)
                        posX,posY=pygame.mouse.get_pos()
                        Raton.dibujar(ventana,posX,posY)
                        for evento in pygame.event.get():
                                if evento.type == QUIT:
                                        pygame.quit()
                                        sys.exit()
                        #SI CHOCA CON BOTON JUGAR:
                        if Raton.rectimagpuntero.colliderect(Tapa.rectjugar):
                                if pygame.mouse.get_pressed()==(1,0,0):
                                        Global.level=1
                        if Raton.rectimagpuntero.colliderect(Tapa.recttutorial):
                                if pygame.mouse.get_pressed()==(1,0,0):
                                        Tapa.ElTutorial(ventana,Raton)
                        #SI CHOCA CON BOTON SALIR:
                        if Raton.rectimagpuntero.colliderect(Tapa.rectpuntaje):
                                if pygame.mouse.get_pressed()==(1,0,0):
                                        pygame.quit()
                                        sys.exit()
                        pygame.display.update()
                if Global.level==1:
                        intro()
                        level1(Raton)
                
                        

main()
