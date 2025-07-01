from pygame.locals import *
import pygame as pg
import sys, os

class MyGameText:
    def _init_(self):
        print("Inicializando biblioteca...")
        
    def create_text(self, msg, size, color, font=None):

        if font == None:
            font = "comicsansms"
            
        font = pg.font.SysFont(font, size, True, False)
        mensagem = f"{msg}"
        text_formatted = font.render(mensagem, False, color)
        return text_formatted