# -*- coding: cp1252 -*-

import pygame,sys,os
from pygame.locals import*
from Global import *
from Puntero import *

class Letras(pygame.sprite.Sprite):
    def __init__(self):
        self.letra = "A"
        self.i = 0
        self.lista = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

        
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
    if Puntaje.score > puntos:
        Global.newscore=True
   

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
    
def newscore(ventana,Puntaje,Raton):
    
    imgarriba=pygame.image.load("imag/arr.PNG")
    imgabajo=pygame.image.load("imag/ab.PNG")
    imgder=pygame.image.load("imag/der.png")
    imgizq=pygame.image.load("imag/izq.png")
    imgnewscore=pygame.image.load("imag/GameOver/NewScore.JPG")
    fuente=pygame.font.Font('fonts/fuentefavorita.ttf',75)
    textoscore=fuente.render(str(Puntaje.score),0,(232,141,0))

    Global.posic=1
    primera = Letras()
    segunda = Letras()
    tercera = Letras()
    
    nombrando = True    
    
 
    while nombrando == True:
        posX,posY=pygame.mouse.get_pos()
        
        
        letraA=fuente.render(primera.lista[primera.i],0,(70,174,18))
        letraB=fuente.render(segunda.lista[segunda.i],0,(70,174,18))
        letraC=fuente.render(tercera.lista[tercera.i],0,(70,174,18))
        
        
            #EN POSICION 1
        if Global.posic==1:
            for evento in pygame.event.get():
                if evento.type == KEYDOWN:
                    if evento.key==K_UP:
                        primera.i += 1
                        if primera.i>=len(primera.lista):
                            primera.i=0

                    if evento.key==K_DOWN:
                        if primera.i<=0:
                            primera.i=len(primera.lista)
                            
                        primera.i -= 1
                    if evento.key==K_RIGHT:
                        Global.posic=2
                    if evento.key==K_LEFT:
                        Global.posic=3

            #EN POSICION 2
        if Global.posic==2:
            for evento in pygame.event.get():
                if evento.type == KEYDOWN:
                    if evento.key==K_UP:
                        segunda.i += 1
                        if segunda.i>=len(segunda.lista):
                            segunda.i=0
                    
                    if evento.key==K_DOWN:
                        if segunda.i<=0:
                            segunda.i=len(segunda.lista)
                            
                        segunda.i -= 1
                    if evento.key==K_RIGHT:
                        Global.posic=3
                    if evento.key==K_LEFT:
                        Global.posic=1

            #EN POSICION 3

        if Global.posic==3:
            for evento in pygame.event.get():
                if evento.type == KEYDOWN:
                    if evento.key==K_UP:
                        tercera.i += 1
                        if tercera.i>=len(tercera.lista):
                            tercera.i=0
                        
                    if evento.key==K_DOWN:
                        if tercera.i<=0:
                            tercera.i=len(tercera.lista)
                            
                        tercera.i -= 1
                    if evento.key==K_RIGHT:
                        Global.posic=1
                    if evento.key==K_LEFT:
                        Global.posic=2
                            
        ventana.fill((0,0,0))
        ventana.blit(imgnewscore,(0,0))
        ventana.blit(textoscore,(470,77))
        if Global.posic==1:
            ventana.blit(imgarriba,(526,177)) #494
            ventana.blit(imgabajo,(526,260))
        if Global.posic==2:
            ventana.blit(imgarriba,(558,177)) #526
            ventana.blit(imgabajo,(558,260))
        if Global.posic==3:
            ventana.blit(imgarriba,(590,177)) #558
            ventana.blit(imgabajo,(590,260))
        ventana.blit(letraA,(522,188)) #490 355
        ventana.blit(letraB,(554,188)) #522 355
        ventana.blit(letraC,(586,188)) #554 355
        ventana.blit(imgizq,(487,220))
        ventana.blit(imgder,(625,220))
        Raton.dibujar(ventana,posX,posY)

        if Raton.rectimagpuntero.colliderect(101,323,180,67): #BOTON DE GUARDAR SCORE
            if pygame.mouse.get_pressed()==(1,0,0):
                nombre=(primera.lista[primera.i] + segunda.lista[segunda.i] + tercera.lista[tercera.i])
                guardardatos(Puntaje,nombre)
                nombrando=False
        
        pygame.display.update()
    
    
    
def guardardatos(Puntaje,nombre):
    f = open("scores.txt","a")
    scoremarcado=["\n"+str(Puntaje.score)," ",nombre+"\n"]
    f.writelines(scoremarcado)
    #Hasta aca solo agregamos el score final a lo ultimo de la lista, falta ordenar todo.
    f.close()
    ordenar()
    
    
    
def ordenar(): #Recordar que solo entra aca SI o solo SI hubo un record que guardar
    f=open("scores.txt","r") #Abrimos el archivo de scores 2 veces, una para el control de lineas
    k=open("scores.txt","r") #y la otra para leer linea por linea los scores con sus nombres
    n=open("ordenados.txt","w") #creamos el archivo donde se guardaran todos los scores ordenados
    i=0 #variables de control
    m=1
    linea=[["01","000"],["02","000"],["03","000"],["04","000"],["05","000"],["06","000"],["07","000"],["08","000"],["09","000"],["10","000"],["11","000"]] #Bueno, esto es una lista de listas no? jaja aca se guardan 1 por 1 los scores que "lee" del archivo
    linea[i]=f.readline() # linea [0] = al primer score que lee del archivo
    kread=k.readline() # K es la variable de control para no mover el cursor del archivo dentro del mismo y perderme
        
    while kread != "":
        i+=1 #Le damos +1 a i
        linea[i]=f.readline() #ahora seria linea[1] = segundo score que lee y asi hasta los 10 
        kread=k.readline() #lee otra linea pero del archivo K (para no leer del archivo F y moverme sin leer datos
        if i==10:
            break #SI i == 10 (osea, si ya leyo todos los resultados posibles) romper el while
    #Recordar que antes de entrar en ordenar() el programa agrego AL FINAL DEL ARCHIVO el nuevo "record"
    linea.sort(reverse=True) #aca se ORDENAN quedando el nuevo record en su posicion correspondiente
    del linea[10] #aca se borra el ULTIMO record, que seria el 11. Siendo el [0] el maximo record y el [9] el menor record. el [10] sobra y seria el menor de todos, entonces se borra
    i=0 #reiniciamos la variable de control
    escribir=linea[i] #ahora comenzamos a escrbir en el archivo "ordenados" desde linea[0] hasta linea[9] (de 0 a 9 son los 10 records ordenados)
    n.writelines(escribir) #escribimos
    i+=1
    while i <= 9:
        escribir=linea[i]
        if i == 9: # "Si este es el ultimo record entonces:"
            escribir=linea[i][:-1] #esto es para quitarle EL ULTIMO CARACTER A EL ULTIMO RECORD QUE SE ESCRIBE ¿Porque? Porque se escriben todos con un salto de linea, para que el siguiente record se vea abajo. Pero el ultimo record si tiene "salto de linea" entonces tira error a la hora de la proxima lectura del archivo
            n.writelines(escribir)
            i+=1
        else:
            n.writelines(escribir)
            i+=1
    k.close() #cerramos
    f.close() #los 3
    n.close() #archivos (en realidad son 2)
    os.remove("scores.txt") #Removemos el viejo "SCORES" sin el ultimo record
    os.rename("ordenados.txt","scores.txt") #renombramos "ORDENADOS" y le ponemos nombre "Score"

    #En resumen, el programa hace lo siguiente:
    #Cada vez que se termina una partida, se revisa en el archivo de scores si MI NUEVO SCORE, es mayor que alguno de los que estan adentro del archivo.
    #Cuando se hace un record, se activa un flag en la clase "Global" que es "newrecord" (Revisar archivo "Global.py")
    #Si es asi, se lo agrega AL FINAL DEL ARCHIVO, pudiendo quedar "35,32,30,26,25,24,23,22,21,10,33" (33 SERIA el nuevo record, pero queda atras de todo por la forma en la que lo agrego)
    #Luego, se vuelven a leer todos los scores en una lista de listas, (los POR AHORA 11 scores[Recordar que es un TOP 10 con 1 agregado al final])
    #se ordena la lista, quedando el menor record al final, y se lo elimina
    #Luego se escriben en un archivo llamado "ordenados" todos los elementos de la lista de listas.
    #se elimina el archivo SCORES y al archivo ORDENADOS se lo renombra como SCORES, quedando asi, un solo archivo de scores con el nuevo score ingresado donde le corresponde ir.

        
        
        


    
