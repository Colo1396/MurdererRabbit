import pygame,sys
import time
from pygame.locals import*
from random import randint




from Menu import*
from Global import*
from Funciones import*
from level1 import*

## Variables Globales

ancho = 800
alto = 600
ventana =pygame.display.set_mode((ancho,alto))

######### Funciones sueltas

   
######TERMINAN LAS CLASES Y ARRANCAN LAS VARIABLES##########
def main():
        #label: juego
        global ventana
        Global.level=0
        pygame.init()
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
                        if Raton.rectimagpuntero.colliderect(Tapa.rectjugar):
                                if pygame.mouse.get_pressed()==(1,0,0):
                                        Global.level=1
                        pygame.display.update()
                if Global.level==1:
                        level1(Raton)

main()
