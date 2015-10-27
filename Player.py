import pygame,sys
import time
from pygame.locals import*
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.izq=False
        self.der=False
        self.up=False
        self.down=False
        self.corre=False
        self.golpe=False
        self.sonidogolpe=pygame.mixer.Sound("sonidos/golpe.ogg")

        self.reposoAgotamiento=0
        self.esperaAgotamiento=0
        self.tiempoRefresco=2   #es un contador que disminuye, para controlar el cambio de las imagenes en listapasosz
        self.refresco=self.tiempoRefresco
        self.orientacion=0 #de 0 a 3, siendo 0:izq, 1:derecha, 2:arriba, 3:abajo
        self.i=0
        self.listapasosz=[  ["imag/z/zi1.png","imag/z/zi2.png","imag/z/zi3.png","imag/z/zi4.png","imag/z/zi5.png","imag/z/zi6.png","imag/z/zi7.png","imag/z/zi8.png","imag/z/zi9.png","imag/z/zi10.png","imag/z/zi11.png","imag/z/zi12.png"],
                            ["imag/z/zd1.png","imag/z/zd2.png","imag/z/zd3.png","imag/z/zd4.png","imag/z/zd5.png","imag/z/zd6.png","imag/z/zd7.png","imag/z/zd8.png","imag/z/zd9.png","imag/z/zd10.png","imag/z/zd11.png","imag/z/zd12.png"],
                            ["imag/z/zar1.png","imag/z/zar2.png","imag/z/zar3.png","imag/z/zar4.png","imag/z/zar5.png","imag/z/zar6.png","imag/z/zar7.png","imag/z/zar8.png","imag/z/zar9.png","imag/z/zar10.png","imag/z/zar11.png","imag/z/zar12.png"],
                            ["imag/z/zab1.png","imag/z/zab2.png","imag/z/zab3.png","imag/z/zab4.png","imag/z/zab5.png","imag/z/zab6.png","imag/z/zab7.png","imag/z/zab8.png","imag/z/zab9.png","imag/z/zab10.png","imag/z/zab11.png","imag/z/zab12.png"]]

        self.listagolpez=[  ["imag/z/zgi1.png","imag/z/zgi2.png","imag/z/zgi3.png","imag/z/zgi4.png","imag/z/zgi5.png"],
                            ["imag/z/zgd1.png","imag/z/zgd2.png","imag/z/zgd3.png","imag/z/zgd4.png","imag/z/zgd5.png"],
                            ["imag/z/zgar1.png","imag/z/zgar2.png","imag/z/zgar3.png","imag/z/zgar4.png","imag/z/zgar5.png"],
                            ["imag/z/zgab1.png","imag/z/zgab2.png","imag/z/zgab3.png","imag/z/zgab4.png","imag/z/zgab5.png"]]
        self.choco = False
        self.refrescoChoque=0
        self.p=0
        self.listaChoco=["imag/choque/zan1.png","imag/choque/zan2.png","imag/choque/zan3.png","imag/choque/zan4.png","imag/choque/zan5.png","imag/choque/zan6.png","imag/choque/zan7.png","imag/choque/zan8.png","imag/choque/zan9.png","imag/choque/zan10.png"]
        self.imagChoco = pygame.image.load(self.listaChoco[self.p])
        
        self.usuario=pygame.image.load(self.listapasosz[self.orientacion][self.i])#el primero de rango 0 a 3, el segundo 0 a 11
        self.rectusuario=self.usuario.get_rect()
        self.rectusuario.left=325
        self.rectusuario.top=200

        self.posXanterior=self.rectusuario.left
        self.posYanterior=self.rectusuario.top

        self.colisionante=pygame.image.load("imag/colisionante.png")
        self.rectcolisionante=self.colisionante.get_rect()
        self.rectcolisionante.left=self.rectusuario.left+70
        self.rectcolisionante.top=self.rectusuario.top+160

        self.golpeizq=pygame.image.load("imag/golpelateral1.png")
        self.rectgolpeizq=self.golpeizq.get_rect()
        self.rectgolpeizq.left=self.rectusuario.left+55
        self.rectgolpeizq.top=self.rectusuario.top+160

        self.golpeder=pygame.image.load("imag/golpelateral1.png")
        self.rectgolpeder=self.golpeder.get_rect()
        self.rectgolpeder.left=self.rectusuario.left+110
        self.rectgolpeder.top=self.rectusuario.top+160

        self.golpear=pygame.image.load("imag/golpelateral2.png")
        self.rectgolpear=self.golpear.get_rect()
        self.rectgolpear.left=self.rectusuario.left+70
        self.rectgolpear.top=self.rectusuario.top+140

        self.golpeab=pygame.image.load("imag/golpelateral2.png")
        self.rectgolpeab=self.golpeab.get_rect()
        self.rectgolpeab.left=self.rectusuario.left+70
        self.rectgolpeab.top=self.rectusuario.top+180

    def moviendose(self,velocidad):
        if self.izq==True:
            self.orientacion=0
            self.posXanterior=self.rectusuario.left
            self.rectusuario.left-=velocidad
            self.rectcolisionante.left-=velocidad
            self.rectgolpeizq.left-=velocidad
            self.rectgolpeder.left-=velocidad
            self.rectgolpear.left-=velocidad
            self.rectgolpeab.left-=velocidad
        if self.der==True:
            self.orientacion=1
            self.posXanterior=self.rectusuario.left
            self.rectusuario.left+=velocidad
            self.rectcolisionante.left+=velocidad
            self.rectgolpeizq.left+=velocidad
            self.rectgolpeder.left+=velocidad
            self.rectgolpear.left+=velocidad
            self.rectgolpeab.left+=velocidad
        if self.up==True:
            self.orientacion=2
            self.posYanterior=self.rectusuario.top
            self.rectusuario.top-=velocidad
            self.rectcolisionante.top-=velocidad
            self.rectgolpeizq.top-=velocidad
            self.rectgolpeder.top-=velocidad
            self.rectgolpear.top-=velocidad
            self.rectgolpeab.top-=velocidad
        if self.down==True:
            self.orientacion=3
            self.posYanterior=self.rectusuario.top
            self.rectusuario.top+=velocidad
            self.rectcolisionante.top+=velocidad
            self.rectgolpeizq.top+=velocidad
            self.rectgolpeder.top+=velocidad
            self.rectgolpear.top+=velocidad
            self.rectgolpeab.top+=velocidad
        
    def dibujar(self,ventana):
        ventana.blit(self.usuario,self.rectusuario)
        ventana.blit(self.colisionante,self.rectcolisionante)
        ventana.blit(self.golpeizq,self.rectgolpeizq)
        ventana.blit(self.golpeder,self.rectgolpeder)
        ventana.blit(self.golpear,self.rectgolpear)
        ventana.blit(self.golpeab,self.rectgolpeab)


    def limitemapa(self):
        self.limiteDerecha =770
        self.limiteIzquierda = 10
        self.limiteTop = 150
        self.limiteDown = 580

        if self.rectcolisionante.left<self.limiteIzquierda:
            self.rectusuario.left=self.posXanterior
            self.rectcolisionante.left=self.rectusuario.left+70
            self.rectcolisionante.top=self.rectusuario.top+160
            self.rectgolpeizq.left=self.rectusuario.left+55
            self.rectgolpeizq.top=self.rectusuario.top+160
            self.rectgolpeder.left=self.rectusuario.left+110
            self.rectgolpeder.top=self.rectusuario.top+160
            self.rectgolpear.left=self.rectusuario.left+70
            self.rectgolpear.top=self.rectusuario.top+140
            self.rectgolpeab.left=self.rectusuario.left+70
            self.rectgolpeab.top=self.rectusuario.top+180
        if self.rectcolisionante.left>self.limiteDerecha:
            self.rectusuario.left=self.posXanterior
            self.rectcolisionante.left=self.rectusuario.left+70
            self.rectcolisionante.top=self.rectusuario.top+160
            self.rectgolpeizq.left=self.rectusuario.left+55
            self.rectgolpeizq.top=self.rectusuario.top+160
            self.rectgolpeder.left=self.rectusuario.left+110
            self.rectgolpeder.top=self.rectusuario.top+160
            self.rectgolpear.left=self.rectusuario.left+70
            self.rectgolpear.top=self.rectusuario.top+140
            self.rectgolpeab.left=self.rectusuario.left+70
            self.rectgolpeab.top=self.rectusuario.top+180

        if self.rectcolisionante.top>self.limiteDown:
            self.rectusuario.top=self.posYanterior
            self.rectcolisionante.left=self.rectusuario.left+70
            self.rectcolisionante.top=self.rectusuario.top+160
            self.rectgolpeizq.left=self.rectusuario.left+55
            self.rectgolpeizq.top=self.rectusuario.top+160
            self.rectgolpeder.left=self.rectusuario.left+110
            self.rectgolpeder.top=self.rectusuario.top+160
            self.rectgolpear.left=self.rectusuario.left+70
            self.rectgolpear.top=self.rectusuario.top+140
            self.rectgolpeab.left=self.rectusuario.left+70
            self.rectgolpeab.top=self.rectusuario.top+180
        if self.rectcolisionante.top<self.limiteTop:
            self.rectusuario.top=self.posYanterior
            self.rectcolisionante.left=self.rectusuario.left+70
            self.rectcolisionante.top=self.rectusuario.top+160
            self.rectgolpeizq.left=self.rectusuario.left+55
            self.rectgolpeizq.top=self.rectusuario.top+160
            self.rectgolpeder.left=self.rectusuario.left+110
            self.rectgolpeder.top=self.rectusuario.top+160
            self.rectgolpear.left=self.rectusuario.left+70
            self.rectgolpear.top=self.rectusuario.top+140
            self.rectgolpeab.left=self.rectusuario.left+70
            self.rectgolpeab.top=self.rectusuario.top+180

    def nextimage(self):
        if self.izq or self.der or self.up or self.down :
            if self.refresco==0:
                if self.i>=len(self.listapasosz[0]):
                    self.i=0
                self.usuario=pygame.image.load(self.listapasosz[self.orientacion][self.i])
                self.i+=1
                self.refresco=2 #deberia decir =tiempoRefresco, pero no actualiza. SOLUCIONAR
            else:
                self.refresco-=1
    def golpenextimage(self):
        if self.refresco==0:
            self.refresco=2
            if self.i>=len(self.listagolpez[0]):
                if self.esperaAgotamiento!=5:
                    self.esperaAgotamiento+=1
                    self.usuario=pygame.image.load(self.listagolpez[self.orientacion][self.i-1])
                else:
                    if self.reposoAgotamiento!=5:
                        self.reposoAgotamiento+=1
                        self.usuario=pygame.image.load(self.listapasosz[self.orientacion][0])
                    else:
                        self.i=0
                        self.esperaAgotamiento=0
                        self.reposoAgotamiento=0
                        self.usuario=pygame.image.load(self.listapasosz[self.orientacion][0])
                        self.golpe=False
            else:
                self.usuario=pygame.image.load(self.listagolpez[self.orientacion][self.i])
                self.i+=1
        else:
            self.refresco-=1

    def choque(self,ventana):
        if self.refrescoChoque==0:
            if self.p >= len(self.listaChoco):
                self.p=0
                self.choco= False
            self.imagChoco= pygame.image.load(self.listaChoco[self.p])
            self.p+=1
            self.refrescoChoque = 10
        else:
            self.refrescoChoque-=1
        ventana.blit(self.imagChoco,self.rectusuario)



    
