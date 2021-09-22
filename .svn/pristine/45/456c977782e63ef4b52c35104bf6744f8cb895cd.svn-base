#################
#coding: utf-8
#################
import pygame
import random
from game_classes.Tetrominos import *

from screens.ScreenMort import *

from files.Window import *
from screens.Screen import *
from pygame.locals import *


class Grid(): #Classe pour l'affichage et la création de la grille

    def __init__(self,posX,posY,pseudo,window, augmenterScoreFonction):

        #Variable ramené dans la classe
        self.sx = posX#Position X de la grille
        self.sy = posY#Position Y de la grille
        self.pseudo = pseudo#Pseudo du joueur
        #Variable
        self.data = "0" #Nombre dans la grille
        self.grid = [] #Grille
        self.rows = 20#Lignes
        self.cols = 10#Colones
        self.block_size = 30 #Taille d'un bloc de la grille
        self.grid_width = self.cols*self.block_size #Largeur de la grille
        self.grid_height = self.rows*self.block_size #Hauteur de la grille
        self.font = ""#Police
        self.label = ""#Texte
        self.rect = ""
        self.color = [255,255,255]
        self.width = 1

        #rajout pour le jeu

        self.colorpiece = [255,10,10]

        self.listoccupe =""
        self.rectorigine = pygame.Rect(0,0,1,1)

        self.window = window

        self.lastTime = 0

        self.augmenterScoreFonction = augmenterScoreFonction

        self.ligneEstSupp = False

        #Return

    ##########################################################

    #Fonction pour l'affichage d'un texte
    def text(self,surface):
        #Text Joueur
        self.font = pygame.font.SysFont('arial', 25)#Choix de la police
        self.label = self.font.render(self.pseudo, 1,(255,255,255))#Choix tu texte
        surface.blit(self.label, (self.sx+self.grid_width/2-25, 10))#Affichage du texte

    ##########################################################

    #Fonction pour la création de la grille
    def creation_grille(self):
        for row in range(self.rows):#Ligne
            self.grid.append([])
            for column in range(self.cols):
                self.grid[row].append(random.choice(self.data))#Injection des zéro dans la grille

        print("Nouvelle Grid : \n") #Affichage de la grille dans la console
        for element in self.grid: #Parcours de la grille
            print(element) #Affichage

        return self.grid #Return de la grille

    ##########################################################

    #Fonction pour l'affichage de la grille
    def affichage_grille(self,surface):

        #création d'une liste qui contiendra les rect de toutes les cases occupés
        self.listoccupe = list()
        #on initialise un objet de type rect dans la liste pour ne pas avoir d'erreur car la liste
        #ne contient pas d'objet de type (nécessaire au collision)
        self.listoccupe.append(self.rectorigine)

        #Dessin des cases de la grille
        for i in range(self.rows):
            for j in range(self.cols):
                if (self.grid[i][j]=="0"):
                    self.rect = pygame.Rect((j * self.block_size) + self.sx,(i*self.block_size) + self.sy, self.block_size, self.block_size)
                    pygame.draw.rect(surface,self.color,self.rect,self.width)
                #si la case est égale à "1", ça signifie quelle est occupé par un block d'un tetrominos,on doit donc dessiner ce block
                elif (self.grid[i][j]=="1"):
                    self.rect = pygame.Rect((j * self.block_size) + self.sx,(i*self.block_size) + self.sy, self.block_size, self.block_size)
                    self.rectpiece = pygame.Rect((j * self.block_size) + self.sx,(i*self.block_size) + self.sy, self.block_size, self.block_size)
                    #on dessine la pièce puis on redessine la grille par dessus
                    pygame.draw.rect(surface,self.colorpiece,self.rectpiece)
                    pygame.draw.rect(surface,self.color,self.rect,self.width)

                    #ajoute les cases occupé dans la liste des cases occupé
                    self.listoccupe.append(self.rect)

    """"""
    #fonction insérant la pièce dans la grille
    def ajout_piece(self,posit,test,x,y):
        #on parcours un tableau contenant les positions de la pièce dans la grille et on convertis ces
        #positions en 1 pour les faire apparaitres dans la grille
        for i in posit:
            k = i[0][0]
            l = i[1][0]

            #on renvoie la piece à sa position de départ
            test.px = x
            test.py = y
            if k<20 and l<10: 
                self.grid[k][l]="1"

    """"""
    def suppr_lign(self):
        #parcours la les lignes de la grille
        lignesKilled = 0
        for i in range(len(self.grid)):
            # si tout une ligne est rempli de 1, on la supprime la ligne en question puis on ajoute une nouvelle ligne de 0
            # au début de la grille
            if self.grid[i] == ["1","1","1","1","1","1","1","1","1","1"]:
                self.newli = [["0","0","0","0","0","0","0","0","0","0"]]
                del self.grid[i]
                self.grid = self.newli + self.grid
                lignesKilled += 1
                self.ligneEstSupp = True;

        if(lignesKilled != 0):
            self.augmenterScoreFonction(lignesKilled)

    """"""# voir à utiliser cette fonction--------------------------!!!!!!!
    def malus_lign(self,grille2ndJoueur):#def malus_lign(self,grille2ndJoueur)
        for i in range(len(self.grid)):
            if self.ligneEstSupp == True:
                zeroAléa = random.randint(0,self.cols-1)
                ligneMal = [["1","1","1","1","1","1","1","1","1","1"]]
                ligneMal[0][zeroAléa] = "0"
                del grille2ndJoueur.grid[0]
                grille2ndJoueur.grid = grille2ndJoueur.grid + ligneMal
                self.ligneEstSupp = False
                print(grille2ndJoueur)
	#ajout
    def grillePleine(self):
        if self.grid[0][5] == "1":
            self.window.changeScreen(ScreenMort(self.window))

    ##########################################################
    def affichage_Tetro(self,xps,yps):
        self.tetroGrille = Tetrominos (self.sx,self.sy,xps,yps)
            #prendre deux pièces
        self.piece = self.tetroGrille.selection_piece()
        self.piece_suivante = self.tetroGrille.selection_piece()

    def time(self):
        lastTime = pygame.time.get_ticks()

    

    def update(self,DROITE,GAUCHE,HAUT,BAS, niveau,grilleAdverse,events):

        #position de depart de la pièce dans chaque grille (a virer ailleurs et à modif)
        pos1 = self.tetroGrille.pos_piece(self.piece,self.sy,self.sx)
        

        #mur pour chaque joueur: évite que les cases ne sortent de la grille
        self.tetroGrille.collision_murG(self.sx,self.sy,self.window.draw)
        self.tetroGrille.collision_murD(self.sx,self.sy,self.window.draw)
        
        self.collb1 = self.tetroGrille.collision_murB(self.sx,self.sy,self,grilleAdverse,pos1,self.tetroGrille,self.window.draw)
        self.collp1 = self.tetroGrille.collision_p(self.listoccupe,self.window.draw,self,grilleAdverse,pos1,self.tetroGrille,self.sx,self.sy)
        #on met le temps qui passe dans une variable time
        time = pygame.time.get_ticks()

        self.tetroGrille.affiche_piece(self.window.draw,self.piece)
        self.tetroGrille.PS_affichage (self.window.draw,self.piece_suivante)

        
		#lorsque la pièce entre en collision avec une autre pièce ou le mur du bas, la pièce suivante deviens la nouvelle pièce et on retire une pièce suivante
        if self.collp1 != [] or self.collb1 != []:
            self.piece = self.piece_suivante
            self.piece_suivante = self.tetroGrille.selection_piece()

        #si time - last time est supérieur à 1sec (1000ms)
        if time-self.lastTime >= (1000-25*niveau):

            #toutes les secondes,on fait descendre la pièce en appellant la fonction chute_accel
            self.tetroGrille.chute_accel(self.piece)

            self.lastTime = time

        self.grillePleine()
###################################################### EVENEMENTS
        for event in events:
            if event.type == pygame.QUIT:  #Si un de ces événements est de type QUIT
                self.window.continuer = False #On arrête la boucle
            if event.type == KEYDOWN:
                #controle joueur 1
                if event.key == HAUT:
                    #la variable self.piece sera modifier pour obtenir la nouvelle position retourner par
                    #la fonction rotation
                    self.piece = self.tetroGrille.rotation(self.piece)

                if event.key == BAS:
                    
                    self.tetroGrille.chute_accel(self.piece)

                if event.key == DROITE:
                    
                    self.tetroGrille.deplacementD(self.piece)

                if event.key == GAUCHE:
                    
                    self.tetroGrille.deplacementG(self.piece)
