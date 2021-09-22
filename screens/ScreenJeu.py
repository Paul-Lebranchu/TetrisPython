import pygame
from gestionAssets.LoadingAssets import *
from files.Window import *
from game_classes.Grid import *
from game_classes.Tetrominos import *
from screens.Screen import *
from screens.ScreenAmelioration import *
from game_classes.Score import *
from game_classes.Niveau import *

class ScreenJeu(Screen):
    def __init__(self, window, gameMode):
    #def __init__(self, window,gameMode): -> plus tard
        super(ScreenJeu, self).__init__()
        self.window = window
        self.loadingAssets = LoadingAssets()
        self.assets()
        self.show()
        self.gameMode = gameMode

    def assets(self):
        #import des images de test
        self.fond = self.loadingAssets.loadImage("assets/images/fondTetris.png")

    def augmenterScore(self, nbLignes):
        self.niveau.augmenterNiveau(nbLignes)
        self.score.augmenterScore(nbLignes, self.niveau.niveauActuel())

    def augmenterScoreJ1(self, nbLignes):
        self.niveauJ1.augmenterNiveau(nbLignes)
        self.scoreJ1.augmenterScore(nbLignes, self.niveauJ1.niveauActuel())

    def augmenterScoreJ2(self, nbLignes):
        self.niveauJ2.augmenterNiveau(nbLignes)
        self.scoreJ2.augmenterScore(nbLignes, self.niveauJ2.niveauActuel())

    def joueur(self,grilleDuJoueur,posTetroX,posTetroY):
        #affichage de la grille
        grilleDuJoueur.creation_grille()
        #Tetrominos
        grilleDuJoueur.affichage_Tetro(posTetroX,posTetroY)
        #time
        grilleDuJoueur.time()

    def show(self):
        #création de la grille par défault
        self.grille = Grid(320,70,"Joueur",self.window, self.augmenterScore)
        self.joueur(self.grille,655,140)

        #création de la grille du joueur 1
        self.grilleJ1 = Grid(40,70,"Joueur1",self.window, self.augmenterScoreJ1)
        self.joueur(self.grilleJ1,380,140)

        #création de la grille du joueur 2
        self.grilleJ2 = Grid(525,70,"Joueur2",self.window, self.augmenterScoreJ2)
        self.joueur(self.grilleJ2,855,140)


        #création de la zone score
        self.score = Score(0, "Score")
        self.scoreJ1 = Score(0, "Score")
        self.scoreJ2 = Score(0, "Score")

        #création du niveau
        self.niveau = Niveau(1, "Niveau")
        self.niveauJ1 = Niveau(1, "Niveau")
        self.niveauJ2 = Niveau(1, "Niveau")

    def renderAffichage(self,grilleDuJoueur,scoreJoueur,niveauJoueur,scoreX,textScoreY,afficheScoreY,textNiveauX,niveauY,afficheNiveauX):
            #Apelle du texte J1
            grilleDuJoueur.text(self.window.draw)
            #Affiche de la grille  du joueur
            grilleDuJoueur.affichage_grille(self.window.draw)
            #affiche score
            scoreJoueur.affichage_TextScore(self.window.draw, scoreX,textScoreY)
            scoreJoueur.affichage_Score(self.window.draw,scoreX,afficheScoreY)
            #affichage niveau
            niveauJoueur.affichage_TextNiveau(self.window.draw, textNiveauX,niveauY)
            niveauJoueur.affichage_Niveau(self.window.draw,afficheNiveauX,niveauY)

    def render(self):
        #on vide l'écran -> pour pas que les dessins se supperpose
        self.window.draw.fill((0,0,0))
        #dessiner les éléments:
        self.window.draw.blit(self.fond,(0,0))

        events = []
        for event in pygame.event.get():
            events.append(event)

        if self.gameMode == 1:
            ####################################################################### Joueur solo
            #update du joueur
            self.grille.update(K_RIGHT,K_LEFT,K_UP,K_DOWN,self.niveau.niveauActuel(),None,events)
            #appel de la fonction qui affiche tout le jeu du joueur
            self.renderAffichage(self.grille,self.score,self.niveau,650,200,235,650,100,730)

        elif self.gameMode == 2:
            ####################################################################### Joueur 1
            #update du joueur 1
            self.grilleJ1.update(K_d,K_q,K_z,K_s,self.niveauJ1.niveauActuel(),self.grilleJ2,events)
            #appel de la fonction qui affiche tout le jeu du joueur 1
            self.renderAffichage(self.grilleJ1,self.scoreJ1,self.niveauJ1,375,200,235,375,100,455)

            ####################################################################### Joueur 2
            #update du joueur 2
            self.grilleJ2.update(K_RIGHT,K_LEFT,K_UP,K_DOWN,self.niveauJ2.niveauActuel(),self.grilleJ1,events)
            #appel de la fonction qui affiche tout le jeu du joueur 2
            self.renderAffichage(self.grilleJ2,self.scoreJ2,self.niveauJ2,850,200,235,850,100,930)

        elif self.gameMode == 3:
            ####################################################################### IA (provisoire)
            self.window.changeScreen(ScreenAmelioration(self.window))
            ####################################################################### Joueur

        elif self.gameMode == 4: #Réseau
            ####################################################################### Joueur 1
            self.window.changeScreen(ScreenAmelioration(self.window))
            ####################################################################### Joueur 2
