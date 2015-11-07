import pygame,sys
import time
from pygame.locals import*
from random import randint

from Enemigo import*
from Vidas import*


tx=0
tz=0
def EvaluarGolpe(x,Player1,Conejo,Puntaje,Global,ventana):
        if Player1.rectgolpeizq.colliderect(x.rectyuyo) and Player1.orientacion==0 and Player1.golpe==True and Conejo.conejoExpuesto==x.IDnumero:
            Conejo.conejoGolpeado=True
            Conejo.sonidoconejogolpe.play()
            Puntaje.score+=1
            Global.combo+=1
            
        elif Player1.rectgolpeder.colliderect(x.rectyuyo) and Player1.orientacion==1 and Player1.golpe==True and Conejo.conejoExpuesto==x.IDnumero :
            Conejo.conejoGolpeado=True
            Conejo.sonidoconejogolpe.play()
            Puntaje.score+=1
            Global.combo+=1
           
        elif Player1.rectgolpear.colliderect(x.rectyuyo) and Player1.orientacion==2 and Player1.golpe==True and Conejo.conejoExpuesto==x.IDnumero :
            Conejo.conejoGolpeado=True
            Conejo.sonidoconejogolpe.play()
            Puntaje.score+=1
            Global.combo+=1
           
        elif Player1.rectgolpeab.colliderect(x.rectyuyo) and Player1.orientacion==3 and Player1.golpe==True and Conejo.conejoExpuesto==x.IDnumero :
            Conejo.conejoGolpeado=True
            Conejo.sonidoconejogolpe.play()
            Puntaje.score+=1
            Global.combo+=1
        else:
            pass




        
        
def probConejo(ventana,Conejo,ContaVidas,Global):
        global tx
        global tz
        if Conejo.hayConejo==False:
            while tx == tz:
                tx = randint(1,10)
            tz = tx
            if tx == 1:
                posX=50
                posY=200
            elif tx == 2:
                posX=115
                posY=70
            elif tx == 3:
                posX=115
                posY=320
            elif tx == 4:
                posX=275
                posY=145
            elif tx == 5:
                posX=300
                posY=380
            elif tx == 6:
                posX=450
                posY=35
            elif tx == 7:
                posX=450
                posY=270
            elif tx == 8:
                posX=620
                posY=120
            elif tx == 9:
                posX=620
                posY=350
            elif tx == 10:
                posX=680
                posY=230
            Conejo.conejoExpuesto=tx-1 #menos uno porque los pastos se numeran de 0 a 9
            Conejo.rectconejo.left=posX
            Conejo.rectconejo.top=posY
            Conejo.hayConejo=True
            Conejo.conejoGolpeado=False
            Conejo.soundSalida.play()
        Conejo.dibujarEnemigo(ventana,ContaVidas,Global)
