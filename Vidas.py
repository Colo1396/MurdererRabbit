import pygame,sys
from pygame.locals import*

pygame.init()
class Vidas(pygame.sprite.Sprite):
    def __init__(self):
        self.imgvida=pygame.image.load("imag/corazongrande.png")
        self.rectvida=self.imgvida.get_rect()
        self.rectvida.left = 600
        self.rectvida.top=15
        self.vidas=10

        self.imgGAMEOVER=pygame.image.load("imag/gameover.png")
        

    def dibujarVida(self,ventana):
        self.fuente=pygame.font.Font('fonts/fuente.ttf',45)
        self.texto=self.fuente.render("=",0,(238,252,48))
        self.texto2=self.fuente.render(str (self.vidas),1,(238,252,48))
        ventana.blit(self.imgvida,self.rectvida)
        ventana.blit(self.texto,(650,self.rectvida.top))
        ventana.blit(self.texto2,(670,self.rectvida.top))

    def comprobarVidas(self,ventana,level):
        
        if self.vidas==0:
            pygame.event.clear() #Limpiar todo.
            perdio=True
            while perdio==True:
                ventana.blit(self.imgGAMEOVER,(0,0))
                pygame.mouse.set_visible(True)
                for evento in pygame.event.get():
                    ventana.blit(self.imgGAMEOVER,(0,0))
                    if evento.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if evento.type == KEYDOWN:
                        if evento.key == K_m:
                            level=0
                            perdio=False
                            self.vidas=2
                   
                pygame.display.update()        
                   
