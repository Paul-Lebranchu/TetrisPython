from screens.Screen import *
from gestionAssets.LoadingAssets import *
from files.Window import *
from screens.ScreenJeu import *
from screens.ScreenDifficulte import *
from pygame.locals import *
from game_classes.Button import *
import pygame

class ScreenMultiLocal(Screen):
    def __init__(self, window):
        super(ScreenMultiLocal, self).__init__()
        self.loadingAssets = LoadingAssets()
        self.assets()
        self.show()
        self.update()
        self.window = window
        self.gameMode = -1 #par défault

    def assets(self):
        self.fond = self.loadingAssets.loadImage("assets/images/fondTetris.png")
        self.imageLocal = self.loadingAssets.loadImage("assets/images/local.png")
        self.imageVsIa = self.loadingAssets.loadImage("assets/images/vsIa.png")
        self.logoTetris = self.loadingAssets.loadImage("assets/images/logoTetris.png")


    def show(self):
        self.button_local = Button(350,300,self.imageLocal)
        self.button_ia = Button(350,425,self.imageVsIa)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.button_local,self.button_ia)

    def render(self):
        #on vide l'écran -> pour pas que les dessins se supperpose
        self.window.draw.fill((0,0,0))
        #on dessine
        self.window.draw.blit(self.fond,(0,0))
        self.window.draw.blit(self.logoTetris,(350,100))

        self.all_sprites.draw(self.window.draw)

        self.all_sprites.update()
        pygame.display.flip()

    def update(self):
        for event in pygame.event.get(): #On parcours la liste de tous les événements reçus
            if event.type == pygame.QUIT:  #Si un de ces événements est de type QUIT
                self.window.endGame() #On arrête la boucle;
            if event.type == pygame.MOUSEBUTTONDOWN: #si on clique sur la fleche du bas, on change de screen
                if event.button == 1 and event.pos[0] >=350 and event.pos[0] <= 650 and event.pos[1] >= 300 and event.pos[1] <= 400 :
                    self.gameMode = 2 #multi local
                    self.window.changeScreen(ScreenJeu(self.window, self.gameMode))
                if event.button == 1 and event.pos[0] >=350 and event.pos[0] <= 650 and event.pos[1] >= 425 and event.pos[1] <= 525 :
                    self.window.changeScreen(ScreenDifficulte(self.window))
