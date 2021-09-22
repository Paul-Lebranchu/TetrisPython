import pygame
from screens.ScreenJeu import *
from screens.ScreenMenu import *
#from WindowConfiguration import *

WIDTH = 1000
HEIGHT = 700
class Window():
    def __init__(self):
        pygame.init()
        self.fenetre()
        self.screen = ScreenMenu(self) #1er screen a afficher

        self.startGame()

    def startGame(self):
        #variable permettant de démarer la boule (et donc le jeu)
        self.continuer = True
        self.boucleJeu()

    def endGame(self):
        #variable permettant d'arreter la boucle (le jeu s'arrete)
        self.continuer = False

    def fenetre(self):
        #initialisation de la fenêtre (taille)
        self.size = width,height = WIDTH,HEIGHT
        #création de la fenetre
        self.draw = pygame.display.set_mode(self.size)

    def changeScreen(self, screenToGo):
        self.screen = screenToGo

    def boucleJeu(self):
        while self.continuer == True:
            #les fonctions qui sont appelés lorsque le jeu est lancé
            self.screen.update()

            self.screen.render()

            pygame.display.flip()
        #quitter pygame (et du coup) le jeu
        pygame.quit();
