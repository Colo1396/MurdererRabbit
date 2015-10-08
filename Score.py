import pygame,sys
from pygame.locals import*


pygame.init()
class Score(pygame.sprite.Sprite):
    def __init__(self):
        self.imagscore= pygame.image.load("imag/score.png")
        self.rectscore=self.imagscore.get_rect()
        self.rectscore.left=435
        self.rectscore.top=15
        self.score=0

        


    def dibujarScore(self,ventana):
        self.fuente=pygame.font.Font('fonts/fuente.ttf',45)
        self.texto=self.fuente.render("=",0,(238,252,48))
        self.texto2=self.fuente.render(str (self.score),1,(238,252,48))
        ventana.blit(self.imagscore,self.rectscore)
        ventana.blit(self.texto,(500,self.rectscore.top))
        ventana.blit(self.texto2,(520,self.rectscore.top))
