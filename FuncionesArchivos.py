import pygame,sys
from pygame.locals import*
from Global import *


def compruebascore(Puntaje,ventana):
    f = open("scores.txt","r") #Crea el objeto de tipo "FILE" y abre el txt en modo lectura (ya tiene que estar creado el archivo)
    ajuste = 1 #variable reguladora
    puntostxt=f.read(2) #puntos es igual a los 2 primeros bytes que lee (el score) PERO LEE FORMATO CADENA
    puntos=int(puntostxt) #Transformo los 2 bytes CADENA a ENTERO para poder comparar despues
    comprueba2(puntos,f,Puntaje) #comprobamos que nuestro puntaje no sea mayor a este numero (que seria el Numero 1 en el TOP 10 de puntajes)
    linea=f.readline() #Leemos la linea entera hasta el \n mas cercano
    while linea!= "": 
        puntostxt=f.read(2)
        puntos=int(puntostxt)
        comprueba2(puntos,f,Puntaje)
        linea=f.readline()
        ajuste += 1
        if ajuste == 10: #ESTO ES PORQUE: Al final del algoritmo, me estaba leyendo 1 vez de mas, pero no habia datos,
                         # entonces cuando comparaba. me decia "(NADA) es menor que SCORE entocnes hay record."
            break
    f.close()
   
    
def comprueba2(puntos,f,Puntaje):
    print puntos,Puntaje.score #COMPARAMOS LOS RECORDS Y NUESTRO PUNTAJE
    if Puntaje.score > puntos:
        print "Nuevo Record"
        Global.newscore=True
    else:
        print "No Record"

def mostrarscores(ventana):
    f=open("scores.txt","r")
    o=open("scores.txt","r")
    posX=100
    posY=125
    ajuste = 1
    linea=o.readline()
    contador=1
    f.seek(0)
    fuente=pygame.font.Font('fonts/fuentefavorita.ttf',55) #Cargamos la fuente para mostrar los archivos
    texto=fuente.render(f.readline(),0,(70,174,18))
    ventana.blit(texto,(100,posY))
    posY += 36
    while linea != "":
        texto=fuente.render(f.readline(),0,(70,174,18))
        ventana.blit(texto,(posX,posY))
        posY += 36
        linea=o.readline()
        contador+=1
        if contador == 5:
            posX = 300
            posY = 125
    f.close()
    o.close()
    
def newscore(ventana):
    imgnewscore=pygame.image.load("imag/GameOver/NewScore.png")
    ventana.blit(imgnewscore,(0,0))
    newscore=True
    contador = 0
    while newscore:
        contador += 1
        if contador == 11150:
            newscore=False
