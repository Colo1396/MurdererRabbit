import pygame,sys
import time,math
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
from Chocador import*

ancho = 800
alto = 600

ventana =pygame.display.set_mode((ancho,alto))
apretarA=pygame.image.load("imag/a.png")

def level1(Raton):
    global ventana
    Global.combo=0
    Chocador1 = Chocador(1)
    Chocador2 = Chocador(2)
    Chocador3 = Chocador(3)
    listaChocador = [Chocador1,Chocador2,Chocador3]
    Player1=Player()
    Conejo=Enemigo()
    Puntaje=Score()
    Raton=Puntero()
    ContaVidas=Vidas()
    pygame.mixer.music.load("sonidos/Malmen Facing TheSky.ogg")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.3)
    timeup=pygame.mixer.Sound("sonidos/timeup.ogg")
    timeup.set_volume(0.3)
    velocidad=1
    BarraVelocidad=Barra()

    Yuyos=AppenImpedimento()
    Yuyos.dibujarAppenImpedimento()
    pygame.display.set_caption("The Murderer Carrot: KILL KILL KILL")
    fondo=pygame.image.load("imag/fondo1.jpg")
    tiempo = pygame.time.get_ticks()/1000
    t = tiempo  # guardo el tiempo actual
    n=1 	#
    segundos=0
    Global.seg=32
    Fuente=pygame.font.Font('fonts/fuentefavorita.ttf',50)
    tomar=False
    while Global.level==1:
        ventana.blit(fondo,(0,0))
################## TIEMPO ########################
        tiempo = (pygame.time.get_ticks()/1000) - t # aca resto el tiempo guardado     
        if tiempo==n:
            segundos=Global.seg
        else:
            Global.seg= Global.seg-1
            n=tiempo
        if Global.seg==0:
            ContaVidas.vidas=0
        contador= Fuente.render("Tiempo: "+str(segundos),0,(70,00,250))
        ventana.blit(contador,(570,10))

        
##############################
        BarraVelocidad.dibujarBarra(ventana)
        #ContaVidas.dibujarVida(ventana)
        Puntaje.dibujarScore(ventana)
        if len(Yuyos.listaImpedimento)>0:
            for x in Yuyos.listaImpedimento:
                x.dibujarImpedimento(ventana)
                if Conejo.conejoGolpeado==False:
                    EvaluarGolpe(x,Player1,Conejo,Puntaje,Global,ventana)
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
        ## control de chocadores
        num=1
        for ChocadorL in listaChocador:
            ChocadorL.llamarChocador(num)
            ChocadorL.movimiento(ventana)
            num= num +1
            if Player1.rectcolisionante.colliderect(ChocadorL.rectChocador):
                ChocadorL.sonidoChoque.play()
                Player1.choco=True
        if Player1.choco==True:
            Player1.choque(ventana)
        if Player1.choco!=True:           
            if Player1.rectcolisionante.top<Conejo.rectconejo.top+175:
                Player1.dibujar(ventana)
        probConejo(ventana,Conejo,ContaVidas,Global)
        if Player1.choco!= True:
            if Player1.rectcolisionante.top>=Conejo.rectconejo.top+175:
                Player1.dibujar(ventana)
            
        for evento in pygame.event.get():
            pygame.event.set_blocked(pygame.MOUSEMOTION)
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key==K_a:
                    if Global.combo>=3:
                        tomar=True
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
                    pausa=pygame.image.load("Imag/pausa.jpg")
                    while pausado:
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
                                if evento.key==K_i:
                                    pygame.quit()
                                    sys.exit()
                        
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
        if Player1.choco!=True:
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


#DIBUJOS DEL RELOJ PARA AUMENTAR TIEMPO
        if Global.combo==1:
            pygame.draw.rect(ventana,(237,28,36),(82,90,7,18))
        if Global.combo==2:
            pygame.draw.rect(ventana,(237,28,36),(82,90,7,18))
            pygame.draw.rect(ventana,(255,244,0),(97,79,7,29))
        if Global.combo>=3:
            pygame.draw.rect(ventana,(237,28,36),(82,90,7,18))
            pygame.draw.rect(ventana,(255,244,0),(97,79,7,29))
            pygame.draw.rect(ventana,(34,177,76),(112,70,7,38))
            ventana.blit(apretarA,(125,56))
            if tomar==True:
                timeup.play()
                Global.seg+=10
                Global.combo=0
                tomar=False
        ContaVidas.comprobarVidas(ventana,Global,Raton,Puntaje) #NUEVO envio la clase Global como parametro y no hace falta llamarla desde la funcion con un import
        pygame.display.update()

