import pygame
from gestionAssets.LoadingAssets import *
from files.Window import *
from screens.Screen import *
from pygame.locals import *
from game_classes.Button import *
from screens.ScreenDifficulte import *
from screens.ScreenJeu import *


class ScreenDifficulte(Screen):
    def __init__(self, window):
        super(ScreenDifficulte, self).__init__()
        self.loadingAssets = LoadingAssets()
        self.assets()
        self.show()
        self.update()
        self.window = window
        self.gameMode = -1 #par défault

    def assets(self):
        self.fond = self.loadingAssets.loadImage("assets/images/fondTetris.png")
        self.imageEasy = self.loadingAssets.loadImage("assets/images/easy.png")
        self.imageMedium = self.loadingAssets.loadImage("assets/images/medium.png")
        self.imageHard = self.loadingAssets.loadImage("assets/images/hard.png")
        self.logoTetris = self.loadingAssets.loadImage("assets/images/logoTetris.png")

    def show(self):
        self.button_facile = Button(350,300,self.imageEasy)
        self.button_normal = Button(350,425,self.imageMedium)
        self.button_dificile = Button(350,550,self.imageHard)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.button_facile,self.button_normal,self.button_dificile)

    def render(self):
        #on vide l'écran -> pour pas que les dessins se supperpose
        self.window.draw.fill((0,0,0))
        #dessiner les éléments:
        self.window.draw.blit(self.fond,(0,0))
        self.window.draw.blit(self.logoTetris,(350,100))

        self.all_sprites.draw(self.window.draw)

        self.all_sprites.update()
        pygame.display.flip()

    def update(self):
        #regarde si un evenement se produit (entrée clavier)
        for event in pygame.event.get(): #On parcours la liste de tous les événements reçus
            if event.type == pygame.QUIT:  #Si un de ces événements est de type QUIT
                 self.window.endGame() #On arrête la boucle
            if event.type == pygame.MOUSEBUTTONDOWN: #si on clique sur la fleche du bas, on change de screen
                 if event.button == 1 and event.pos[0] >= 350 and event.pos[0] <= 650 and event.pos[1] >= 300 and event.pos[1] <=400:
                     self.gameMode = 3 #multi ia
                     self.window.changeScreen(ScreenJeu(self.window, self.gameMode))
                 if event.button == 1 and event.pos[0] >= 350 and event.pos[0] <= 650 and event.pos[1] >= 425 and event.pos[1] <=525:
                     self.gameMode = 3 #multi ia
                     self.window.changeScreen(ScreenJeu(self.window, self.gameMode))
                 if event.button == 1 and event.pos[0] >=350  and event.pos[0] <= 650 and event.pos[1] >= 550 and event.pos[1] <= 650:
                     self.gameMode = 3 #multi ia
                     self.window.changeScreen(ScreenJeu(self.window, self.gameMode))
