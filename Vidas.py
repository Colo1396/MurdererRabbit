import pygame,sys
from pygame.locals import*
from FuncionesArchivos import *
from Global import* #NO HACE FALTA HACER ESTO PORQUE SE LO MANDO COMO PARAMETRO AHORA

class Vidas(pygame.sprite.Sprite):
    def __init__(self):
        self.imgvida=pygame.image.load("imag/corazongrande.png")
        self.rectvida=self.imgvida.get_rect()
        self.rectvida.left = 600
        self.rectvida.top=15
        self.vidas=10000
        
        self.imgGAMEOVER=pygame.image.load("imag/GameOver/FinDelJuego.JPG")
        self.sonidotecla=pygame.mixer.Sound("sonidos/tecla.ogg")

        #imgnewscore=pygame.image.load("imag/GameOver/NewScore.JPG")
        

    def dibujarVida(self,ventana):
        self.fuente=pygame.font.Font('fonts/fuente.ttf',45)
        self.texto=self.fuente.render("=",0,(50,50,250))
        self.texto2=self.fuente.render(str (self.vidas),1,(50,50,250))
        ventana.blit(self.imgvida,self.rectvida)
        ventana.blit(self.texto,(650,self.rectvida.top))
        ventana.blit(self.texto2,(670,self.rectvida.top))

    def comprobarVidas(self,ventana,Global,Raton,Puntaje):
        Global.score=False
        Global.newscore=False
        if self.vidas==0:
            pygame.event.clear() #Limpiar todo.
            perdio=True
            compruebascore(Puntaje,ventana)
            if Global.newscore==True:
                newscore(ventana,Puntaje,Raton)
            #sonidotecla=pygame.mixer.Sound("sonidos/tecla.mp3")
            while perdio==True:
                
                self.botmenu=pygame.image.load("imag/GameOver/menu1.png")
                self.botcred=pygame.image.load("imag/GameOver/cred1.png")
                self.botexit=pygame.image.load("imag/GameOver/exit1.png")
                self.botscore=pygame.image.load("imag/GameOver/score1.png")
                ventana.blit(self.imgGAMEOVER,(0,0))
                ventana.blit(self.botmenu,(91,455))#Dibujo el boton menu
                ventana.blit(self.botscore,(206,455)) #dibujo el boton score
                ventana.blit(self.botcred,(263,514)) #dibujo el boton creditos
                ventana.blit(self.botexit,(126,514)) #dibujo el boton exit
                
                posX,posY=pygame.mouse.get_pos()


                #SI COLISIONA CON MENU
                if Raton.rectimagpuntero.colliderect(131,471,64,28):
                    
                    self.botmenu=pygame.image.load("imag/GameOver/menu2.png")
                    ventana.blit(self.botmenu,(91,455))
                    
                    if pygame.mouse.get_pressed()==(1,0,0):
                        self.sonidotecla.play()
                        Global.score=False
                        Global.level=0
                        perdio=False

                #SI COLISIONA CON SCORE:
                elif Raton.rectimagpuntero.colliderect(247,472,60,41):
                    self.botscore=pygame.image.load("imag/GameOver/score2.png")
                    
                    ventana.blit(self.botscore,(206,455))
                    if pygame.mouse.get_pressed()==(1,0,0):
                        self.sonidotecla.play()
                        Global.score=True
                        self.imgGAMEOVER=pygame.image.load("imag/GameOver/FDJscores.jpg")
                        
                            
                #SI COLISIONA CON CREDITS:
                elif Raton.rectimagpuntero.colliderect(314,534,90,39):
                    self.botcred=pygame.image.load("imag/GameOver/cred2.png")
                    
                    ventana.blit(self.botcred,(263,514))
                    if pygame.mouse.get_pressed()==(1,0,0):
                        self.sonidotecla.play()
                        Global.score=False
                        self.imgGAMEOVER=pygame.image.load("imag/GameOver/FDScred.jpg")
                    
                    
                #SI COLISIONA CON EXIT:
                elif Raton.rectimagpuntero.colliderect(184,536,73,36):
                    self.botexit=pygame.image.load("imag/GameOver/exit2.png")
                    
                    ventana.blit(self.botexit,(126,514)) #Boton brillando
                    if pygame.mouse.get_pressed()==(1,0,0):
                        self.sonidotecla.play()
                        Global.score=False
                        pygame.quit()
                        sys.exit()

                    
                for evento in pygame.event.get():
                    if evento.type == QUIT:
                        pygame.quit()
                        sys.exit()
                        
                status(ventana,Global)    
                Raton.dibujar(ventana,posX,posY)       
                pygame.display.update()

def status(ventana,Global):
    if Global.score==True:
        mostrarscores(ventana)
    
