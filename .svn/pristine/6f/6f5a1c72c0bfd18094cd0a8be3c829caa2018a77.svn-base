from screens.Screen import *
from gestionAssets.LoadingAssets import *
from files.Window import *
from screens.ScreenDifficulte import *
from screens.ScreenMultiLocal import *
from pygame.locals import *
from game_classes.Button import *
import pygame

class ScreenMenu(Screen):
    def __init__(self, window):
        super(ScreenMenu, self).__init__()
        self.loadingAssets = LoadingAssets()
        self.assets()
        self.show()
        self.update()
        self.window = window
        self.gameMode = -1 #par défault

    def assets(self):
        self.fond = self.loadingAssets.loadImage("assets/images/fondTetris.png")
        self.imageModeSolo = self.loadingAssets.loadImage("assets/images/modeSolo.png")
        self.imageModeMulti = self.loadingAssets.loadImage("assets/images/modeMulti.png")
        self.imageModeOnline = self.loadingAssets.loadImage("assets/images/modeOnline.png")
        self.imageEasy = self.loadingAssets.loadImage("assets/images/easy.png")
        self.imageMedium = self.loadingAssets.loadImage("assets/images/medium.png")
        self.imageHard = self.loadingAssets.loadImage("assets/images/hard.png")
        self.imageLocal = self.loadingAssets.loadImage("assets/images/local.png")
        self.imageVsIa = self.loadingAssets.loadImage("assets/images/vsIa.png")
        self.logoTetris = self.loadingAssets.loadImage("assets/images/logoTetris.png")

    def show(self):
        self.button_solo = Button(350,300,self.imageModeSolo)
        self.button_multi = Button(350,425, self.imageModeMulti)
        self.button_online = Button(350,550,self.imageModeOnline)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.button_online,self.button_solo,self.button_multi)

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
            if event.type == MOUSEBUTTONDOWN: #Si un de ces événements est de type MOUSEBUTTONDOWN (clic souris)
                if event.button == 1 and event.pos[0] >= 350 and event.pos[0] <= 650 and event.pos[1] <=400 and event.pos[1] >=300:
                    self.gameMode = 1 #solo
                    self.window.changeScreen(ScreenJeu(self.window, self.gameMode))
                if event.button == 1 and event.pos[0] >= 350 and event.pos[0] <= 650 and event.pos[1] <=525 and event.pos[1] >=425:
                    self.window.changeScreen(ScreenMultiLocal(self.window))
                if event.button == 1 and event.pos[0] >= 350 and event.pos[0] <= 650 and event.pos[1] <=650 and event.pos[1] >=550:
                    self.gameMode = 4 #online
                    self.window.changeScreen(ScreenJeu(self.window,self.gameMode))
