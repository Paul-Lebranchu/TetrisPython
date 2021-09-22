import pygame
import random
#from game_classes.ScreenJeu import *
from game_classes.Shape import *

pygame.init()

#faire la carte d'identité de la pièce
class Tetrominos():
    def __init__(self,x, y,xps,yps):
        #initialisation des blocs pour tracer le tetrominos
        self.rect = "" #pièce
        self.rects ="" #pièce suivante

        self.block_size = 30 #taille des blocks
        self.BSS = 15 #taille des blocks suivant, plus petit pour faciliter l'affichage

        self.color = [100,20,100] #couleur blocks : temporaire
        self.color_suivante = [255,255,0] #couleur du block suivant
        self.piece = "" #variable stockant une pièce

        self.heightP = ""
        self.widthP = ""

        self.px = x #position X de la pièce
        self.py = y #position Y de la pièce

        self.psx = xps  #position X de la pièce suivante
        self.psy = yps #position Y de la pièce suivante

        self.grille = ""#utiliser dans le cadre de la rotation

        self.murG = "" #mur de gauche pour la collision
        self.murD = "" #mur de droite pour la collision
        self.murB = "" #mur du bas pour la collision

        self.collisionMG = ""#collision avec mur de gauche
        self.collisionMD = ""#collision avec mur de droite
        self.collisionMB = ""#collision avec mur du bas

        self.collisionp = "" #gère la collision des pièces

        self.newcoll = ""#en cas de collision

        self.listrect = list() #liste où on stocke chaque carré du tetrominos

        self.pos = "" #donné stockant les positions de la pièce

        self.temps = "" #pour la gestion de la chute des pièces

        self.lastMove =""

    """"""
    #récupérer une pièce
    def selection_piece(self):
        #prend une pièces au hasard de la variable pieces du fichier shape.py
        self.piece = random.choice(pieces)
        return self.piece


    """"""
    #rotation
    def rotation(self,piece):

        #on initialise la hauteur puis la largeur de la pièce sélectionner
        self.heightP = len(piece)
        self.widthP = len(piece[0])

        #la variable grille devient une liste
        self.grille = list()

        #la grille devient un liste en 2D qui aura les mêmes dimensions que la prochaine forme de la pièce
        for i in range(self.widthP):
            self.grille.append([0]*self.heightP)

        #grille prend la valeur de la prochaine "forme" de la pièce
        for y in range (self.heightP):
            for x in range (self.widthP):
                self.grille[x][y] = piece[y][self.widthP-1-x]

        #on donne sa nouvelle forme à la pièce et on "return" la pièce
        piece = self.grille
        return piece

    """"""
    #gérer le déplacement

        #déplacement vers la gauche
    def deplacementG(self,piece):
        #retire la taille du block à la position x (ligne) -> décalage vers la gauche
        self.px -= self.block_size
        self.lastMove = "GAUCHE"


    """"""
        #déplacment vers la droite
    def deplacementD(self,piece):
        #rajoute la taille du block à la position x (ligne) -> décalage vers la droite
       self.px += self.block_size
       self.lastMove = "DROITE"

    """"""
        #simulation d'une accélération de la chute de la pièce
    def chute_accel(self,piece):

        #rajoute la taille du block à la position y (ligne) -> décalage vers le bas
        self.py += self.block_size
        self.lastMove = "BAS"

    def remonter_piece(self,piece):

        
        self.py -= self.block_size

    """"""
    #gère l'affichage de la pièce: ne marche pas actuellement
    def affiche_piece(self,surface,piece):
        #on initialise la hauteur puis la largeur de la pièce sélectionner
        self.heightP = len(piece)
        self.widthP = len(piece[0])

        self.listrect = list()
        # on parcours les lignes et les colonnes d'une pièce selectionnée et si une case du tableau est
        # égale à 1, alors on dessine un carré. Toutes les cases contenant un 1 forme le tetrominos
        for i in range (self.heightP):
            for j in range (self.widthP):
                if piece[i][j] == '1':
                    #le +4*self.block_size est là pour faire commencer la pièce environ au milieu de la grille
                    self.rect = pygame.Rect((j*self.block_size)+self.px+4*self.block_size,(i*self.block_size)+self.py,self.block_size,self.block_size)
                    self.listrect.append(self.rect)
                    pygame.draw.rect(surface,self.color,self.rect)

    """"""
    #affichage de la pièce suivante
    def PS_affichage(self,surface,piece):
        #on initialise la hauteur puis la largeur de la pièce sélectionner
        self.heightP = len(piece)
        self.widthP = len(piece[0])

        #même fonction que pour l'affichage de la pièce sauf qu'on change les positions px et py
        for i in range (self.heightP):
            for j in range (self.widthP):
                if piece[i][j] == '1':
                    self.rects = pygame.Rect((j*self.BSS)+self.psx,(i*self.BSS)+self.psy,self.BSS,self.BSS)
                    pygame.draw.rect(surface,self.color_suivante,self.rects)

    """"""
    #gère la collision avec le mur de gauche
    def collision_murG(self,sx,sy,surface):
        #création du mur gauche de la grille
        self.murG = pygame.Rect(sx-self.block_size,sy,self.block_size,self.block_size*20)

        #la fonction collidelisteall permet de tester si il y a collision entre un "rect" (ici murB) et
        #une liste (ici listrect), renvoie [] si il n'y a pas de collision et [x] si il y en a (x = nombre de collision détecter)
        self.collisionMG = self.murG.collidelistall(self.listrect)

        #si il y a collision, avec le mur droit, on décale
        if self.collisionMG != []:
            self.px += self.block_size


        return (self.collisionMG)

    """"""
    #gère la collision avec le mur de droite
    def collision_murD(self,sx,sy,surface):
        #création du mur gauche de la grille
        self.murD = pygame.Rect(sx+(self.block_size*10),sy,self.block_size,self.block_size*20)

        #la fonction collidelisteall permet de tester si il y a collision entre un "rect" (ici murD) et
        #une liste (ici listrect)
        self.collisionMD = self.murD.collidelistall(self.listrect)

        if self.collisionMD != []:
            
            self.px -= self.block_size

        return (self.collisionMD)

    """"""
    #gère la collision avec le mur du bas
    def collision_murB(self,sx,sy,grille,grille2,posit,test,surface):
        #création du mur gauche de la grille
        self.murB = pygame.Rect(sx,sy+(self.block_size*19),self.block_size*10,self.block_size)


        self.collisionMB = self.murB.collidelistall(self.listrect)

        if self.collisionMB != []:
            
            self.newcoll = self.collisionMB
            grille.ajout_piece(posit,test,sx,sy)
            grille.suppr_lign()
            if grille2 != None:
                grille.malus_lign(grille2)
            return self.newcoll

        return (self.collisionMB)

    """"""
    def collision_p(self,caseoccupe,surface,grille,grille2,posit,test,x,y):
        #on parcours les différentes caseoccupé de la grille et on voit si il y a collision
        for i in  range (len(caseoccupe)):
            self.collisionp = caseoccupe[i].collidelistall(self.listrect)

            #définis ce qui se passe lorsqu'il y a collision
            if self.collisionp != [] and self.lastMove == "BAS":
                
                self.newcoll = self.collisionp
                #on parcours le tableau des position x,y ([j][0]) et on prend la valeur qui est dedans
                #on y retire 1 pour que la pièce apparaise à la case précédent la collision

                for j in range(len(posit)):
                    posit[j][0][0] -= 1

                #ajout de la pièce et la grille et suppression de ligne si nécessaire
                grille.ajout_piece(posit,test,x,y)
                grille.suppr_lign()
                if grille2 != None:
                    grille.malus_lign(grille2)
                return self.newcoll

            if self.collisionp != [] and self.lastMove == "GAUCHE":
                print (self.collisionp)
                
                self.px += self.block_size
                return []

            if self.collisionp != [] and self.lastMove == "DROITE":
                print(self.collisionp)
                
                self.px -= self.block_size
                return []

        return self.collisionp

    """"""
    #tableau renvoyant la position de la pièce
    def pos_piece(self,piece,y,x):
        #y: position de la grille par rapport aux haut de la fenetre
        #x : position par rapport au coté gauche de la fenetre

        self.pos = list()

        self.heightP = len(piece)
        self.widthP = len(piece[0])

        for i in range (self.heightP):
            for j in range (self.widthP):
                if piece[i][j] == '1':
                    self.pos.append([[(self.py-y)//30+i],[(self.px-x)//30+j+4]])
                    #renvoie dans l'ordre le numéro de la ligne puis le numéro de la colonne
                    #le numéro de la ligne sera compris

        return self.pos
