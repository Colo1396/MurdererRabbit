import pygame,sys
from pygame.locals import*

#from Global import* #NO HACE FALTA HACER ESTO PORQUE SE LO MANDO COMO PARAMETRO AHORA

pygame.init()
class Vidas(pygame.sprite.Sprite):
    def __init__(self):
        self.imgvida=pygame.image.load("imag/corazongrande.png")
        self.rectvida=self.imgvida.get_rect()
        self.rectvida.left = 600
        self.rectvida.top=15
        self.vidas=1

        self.imgGAMEOVER=pygame.image.load("imag/GameOver/FinDelJuego.png")
        self.botmenu=pygame.image.load("imag/GameOver/MENUAP.png")
        self.botcred=pygame.image.load("imag/GameOver/CREDITSAP.png")
        self.botexit=pygame.image.load("imag/GameOver/EXITAP.png")
        self.botscore=pygame.image.load("imag/GameOver/SCOREAP.png")
        

    def dibujarVida(self,ventana):
        self.fuente=pygame.font.Font('fonts/fuente.ttf',45)
        self.texto=self.fuente.render("=",0,(238,252,48))
        self.texto2=self.fuente.render(str (self.vidas),1,(238,252,48))
        ventana.blit(self.imgvida,self.rectvida)
        ventana.blit(self.texto,(650,self.rectvida.top))
        ventana.blit(self.texto2,(670,self.rectvida.top))

    def comprobarVidas(self,ventana,Global,Raton):
        
        if self.vidas==0:
            pygame.event.clear() #Limpiar todo.
            perdio=True
            while perdio==True:
                ventana.blit(self.imgGAMEOVER,(0,0))
                posX,posY=pygame.mouse.get_pos()


                #SI COLISIONA CON MENU
                if Raton.rectimagpuntero.colliderect(222,464,80,32):
                    ventana.blit(self.botmenu,(212,454))
                    if pygame.mouse.get_pressed()==(1,0,0):
                        Global.level=0
                        perdio=False

                #SI COLISIONA CON SCORE:
                if Raton.rectimagpuntero.colliderect(334,462,85,34):
                    ventana.blit(self.botscore,(330,454))

                    
                #SI COLISIONA CON CREDITS:
                if Raton.rectimagpuntero.colliderect(256,521,92,46):
                    ventana.blit(self.botcred,(244,511))

                    
                #SI COLISIONA CON EXIT:
                if Raton.rectimagpuntero.colliderect(385,523,99,43):
                    ventana.blit(self.botexit,(378,511))
                    if pygame.mouse.get_pressed()==(1,0,0):
                        pygame.quit()
                        sys.exit()
                    
                for evento in pygame.event.get():
                    if evento.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    
                Raton.dibujar(ventana,posX,posY)       
                            
                            
                   
                pygame.display.update()        
                   
