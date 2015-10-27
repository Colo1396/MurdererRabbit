import pygame,sys
from pygame.locals import*


class Score(pygame.sprite.Sprite):
    def __init__(self):
        self.imagscore= pygame.image.load("imag/score.png")
        self.rectscore=self.imagscore.get_rect()
        self.rectscore.left=435
        self.rectscore.top=15
        self.score=8

        


    def dibujarScore(self,ventana):
        self.fuente=pygame.font.Font('fonts/fuentefavorita.ttf',50)
        self.texto=self.fuente.render("=",0,(70,00,250))
        self.texto2=self.fuente.render(str (self.score),1,(70,00,250))
        ventana.blit(self.imagscore,(420,17))
        ventana.blit(self.texto,(480,10))
        ventana.blit(self.texto2,(505,10))
