import pygame,sys
import time

from pygame.locals import*
from random import randint


class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sonidoconejogolpe=pygame.mixer.Sound("sonidos/conejogolpe.ogg")
        self.tiepoRefresco=2
        self.i=0
        self.listaconejo = ["imag/c/c1.png","imag/c/c2.png","imag/c/c3.png","imag/c/c4.png","imag/c/c5.png","imag/c/c6.png","imag/c/c7.png","imag/c/c8.png","imag/c/c9.png"]
        self.listaconejogolpeado = ["imag/c/cg1.png","imag/c/cg2.png","imag/c/cg3.png","imag/c/cg4.png","imag/c/cg5.png","imag/c/cg6.png","imag/c/cg7.png","imag/c/cg8.png","imag/c/cg9.png"]
        self.estadoConejo=self.listaconejo
        self.conejo=pygame.image.load(self.estadoConejo[self.i])#de rango 0 a 8
        self.rectconejo=self.conejo.get_rect()

        self.conejoGolpeado=False
        self.conejoExpuesto=0   #es el numero del agujero en el que sale
        self.hayConejo=False    #como el dibujarEnemigo se dibuja constantemente, para que no suceda hasta que el conejo se esconda, este flag se pone en true al llamarlo, y cuando termine el proceso se pone en false solo
        self.flagsube=True
        self.expuesto = 0   #por cada ciclo de procesos aumenta uno, con esto se controla cuanto tiempo va a aparecer el conejo
        self.tiempoexpuesto = 50
        self.soundSalida= pygame.mixer.Sound("sonidos/pop.ogg")
        self.rectconejo.left=0
        self.rectconejo.top=0

    def dibujarEnemigo(self,ventana,ContaVidas,Global):
        if self.conejoGolpeado==False:
            self.estadoConejo=self.listaconejo
        else:
            self.estadoConejo=self.listaconejogolpeado
        if self.hayConejo==True:
            if self.tiepoRefresco==0:
                self.tiepoRefresco=2
                if self.flagsube==True:
                    if self.i<len(self.listaconejo):
                        self.conejo=pygame.image.load(self.estadoConejo[self.i])
                        self.i+=1
                    else:
                        self.conejo=pygame.image.load(self.estadoConejo[len(self.listaconejo)-1])
                        self.expuesto+=1
                        if self.expuesto==self.tiempoexpuesto:
                            self.expuesto=0
                            self.flagsube=False
                else:
                    if self.i>0:
                        self.i-=1
                        self.conejo=pygame.image.load(self.estadoConejo[self.i])
                    else:
                        self.flagsube=True
                        self.hayConejo=False
                        if self.conejoGolpeado == False:
                            ContaVidas.vidas-=1
                            Global.combo=0
                            
            else:
                self.tiepoRefresco-=1
                
            ventana.blit(self.conejo,self.rectconejo)
