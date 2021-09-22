from screens.Screen import *
from gestionAssets.LoadingAssets import *
from files.Window import *
from pygame.locals import *
import pygame

class ScreenAmelioration(Screen):
    def __init__(self,window):
        super(ScreenAmelioration, self).__init__()
        self.loadingAssets = LoadingAssets()
        self.assets()
        self.show()
        self.update()
        self.window = window


    def assets(self):
        self.fond = self.loadingAssets.loadImage("assets/images/fondTetris.png")
        self.amelio = self.loadingAssets.loadImage("assets/images/amelioration.png")

    def show(self):
        pass;

    def render(self):
        self.window.draw.fill((0,0,0))

        self.window.draw.blit(self.fond,(0,0))
        self.window.draw.blit(self.amelio,(200,125))

        pygame.display.flip()

    def update(self):
        from screens.ScreenMenu import ScreenMenu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.window.endGame()
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.window.changeScreen(ScreenMenu(self.window))
