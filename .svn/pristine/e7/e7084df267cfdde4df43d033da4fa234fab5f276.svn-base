from screens.Screen import *
from gestionAssets.LoadingAssets import *
from files.Window import *
from pygame.locals import *
from game_classes.Button import *
import pygame

class ScreenMort(Screen):
    def __init__(self,window):
        super(ScreenMort, self).__init__()
        self.loadingAssets = LoadingAssets()
        self.assets()
        self.show()
        self.update()
        self.window = window


    def assets(self):
        self.fond = self.loadingAssets.loadImage("assets/images/fondTetris.png")
        self.quit = self.loadingAssets.loadImage("assets/images/exit.png")
        self.recomencer = self.loadingAssets.loadImage("assets/images/continue.png")


    def show(self):
        self.button_Recomencer = Button(350,425, self.recomencer)
        self.button_Quit = Button(350,550,self.quit)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.button_Recomencer,self.button_Quit)

    def render(self):
        self.window.draw.fill((0,0,0))

        self.window.draw.blit(self.fond,(0,0))

        self.all_sprites.draw(self.window.draw)

        self.all_sprites.update()
        pygame.display.flip()

    def update(self):
        from screens.ScreenMenu import ScreenMenu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.window.endGame()
            if event.type == MOUSEBUTTONDOWN: #Si un de ces événements est de type MOUSEBUTTONDOWN (clic souris)
                if event.button == 1 and event.pos[0] >= 350 and event.pos[0] <= 650 and event.pos[1] <=525 and event.pos[1] >=425:
                    self.window.changeScreen(ScreenMenu(self.window))
                if event.button == 1 and event.pos[0] >= 350 and event.pos[0] <= 650 and event.pos[1] <=650 and event.pos[1] >=550:
                    self.window.endGame()
