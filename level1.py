import pygame,sys
import time
from pygame.locals import*
from random import randint

from Player import*
from Enemigo import*
from BarraEnergia import*
from Impedimento import*
from Score import*
from Vidas import*
from Funciones import*
from Global import*

ancho = 800
alto = 600

ventana =pygame.display.set_mode((ancho,alto))

def level1(Raton):
    global ventana
    pygame.init()
    Player1=Player()
    Conejo=Enemigo()
    Puntaje=Score()
    ContaVidas=Vidas()
    pygame.mixer.music.load("sonidos/Malmen Facing TheSky.ogg")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.3)
    velocidad=1
    BarraVelocidad=Barra()
    Yuyos=AppenImpedimento()
    Yuyos.dibujarAppenImpedimento()
    pygame.display.set_caption("The Murderer Plant: Level 1")
    fondo=pygame.image.load("imag/fondo1.jpg")
    while Global.level==1:
        ventana.blit(fondo,(0,0))
        BarraVelocidad.dibujarBarra(ventana)
        ContaVidas.dibujarVida(ventana)
        Puntaje.dibujarScore(ventana)
        if len(Yuyos.listaImpedimento)>0:
            for x in Yuyos.listaImpedimento:
                x.dibujarImpedimento(ventana)
                if Conejo.conejoGolpeado==False:
                    EvaluarGolpe(x,Player1,Conejo,Puntaje)
                if Player1.rectcolisionante.colliderect(x.rectyuyo):
                    Player1.rectusuario.left=Player1.posXanterior
                    Player1.rectusuario.top=Player1.posYanterior
                    Player1.rectcolisionante.left=Player1.posXanterior+70
                    Player1.rectcolisionante.top=Player1.posYanterior+160
                    Player1.rectgolpeizq.left=Player1.posXanterior+55
                    Player1.rectgolpeizq.top=Player1.posYanterior+160
                    Player1.rectgolpeder.left=Player1.posXanterior+110
                    Player1.rectgolpeder.top=Player1.posYanterior+160
                    Player1.rectgolpear.left=Player1.posXanterior+70
                    Player1.rectgolpear.top=Player1.posYanterior+140
                    Player1.rectgolpeab.left=Player1.posXanterior+70
                    Player1.rectgolpeab.top=Player1.posYanterior+180
                    
        if Player1.rectcolisionante.top<Conejo.rectconejo.top+175:
            Player1.dibujar(ventana)
        probConejo(ventana,Conejo,ContaVidas)
        if Player1.rectcolisionante.top>=Conejo.rectconejo.top+175:
            Player1.dibujar(ventana)
            
        for evento in pygame.event.get():
            pygame.event.set_blocked(pygame.MOUSEMOTION)
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key==K_LEFT:
                    Player1.izq=True
                    Player1.der=False
                if evento.key==K_RIGHT:
                    Player1.izq=False
                    Player1.der=True
                if evento.key==K_UP:
                    Player1.up=True
                    Player1.down=False
                if evento.key==K_DOWN:
                    Player1.up=False
                    Player1.down=True
                if evento.key==K_s:
                    Player1.corre=True
                if evento.key==K_SPACE and Player1.golpe==False:
                        Player1.sonidogolpe.play()
                        Player1.golpe=True
                        Player1.i=0
                        Player1.refresco=0
                if evento.key==K_p:
                    Player1.izquierda=False
                    Player1.derecha=False
                    Player1.arriba=False
                    Player1.abajo=False
                    Player1.correr=False
                    pausado = True
                    while pausado:
                        pausa=pygame.image.load("Imag/pausa.jpg")
                        for evento in pygame.event.get():
                            ventana.blit(pausa,(0,0))
                            pygame.display.update()
                            if evento.type == QUIT:
                                pygame.quit()
                                sys.exit()
                            if evento.type == KEYDOWN:
                                if evento.key==K_o:
                                    pausado = False
                                    pygame.display.update() 
            if evento.type == KEYUP:
                if evento.key==K_s:
                    Player1.corre=False
                if evento.key==K_LEFT:
                    Player1.izq=False
                if evento.key==K_RIGHT:
                    Player1.der=False
                if evento.key==K_UP:
                    Player1.up=False
                if evento.key==K_DOWN:
                    Player1.down=False

        if Player1.corre==True:
            if BarraVelocidad.valorx>10:
                velocidad = 3
                Player1.tiempoRefresco=5
                BarraVelocidad.valorx-=1
            else:
                Player1.tiempoRefresco=10
                velocidad = 1
        else:
            velocidad = 1
            Player1.tiempoRefresco=10
            BarraVelocidad.valorx+=2
            
        if Player1.golpe!=True:
            Player1.moviendose(velocidad)
            Player1.limitemapa()
            Player1.nextimage()
        else:
            Player1.golpenextimage()
            
#SI PONEMOS ESTO SE BUGEA TODO. DEJARLO APAGADO         pygame.event.clear()   #esto borra todos los eventos de la cola
        if Player1.golpe==False:
            if( pygame.key.get_pressed()[pygame.K_LEFT] and Player1.up==False and Player1.der==False and Player1.down==False):
                Player1.orientacion = 0
            if( pygame.key.get_pressed()[pygame.K_RIGHT] and Player1.izq==False and Player1.up==False and Player1.down==False):
                Player1.orientacion = 1
            if( pygame.key.get_pressed()[pygame.K_UP] and Player1.izq==False and Player1.der==False and Player1.down==False):
                Player1.orientacion = 2
            if( pygame.key.get_pressed()[pygame.K_DOWN] and Player1.izq==False and Player1.der==False and Player1.up==False):
                Player1.orientacion = 3
        ContaVidas.comprobarVidas(ventana,Global,Raton) #NUEVO envio la clase Global como parametro y no hace falta llamarla desde la funcion con un import
        pygame.display.update() 
