#ici la gestion de score
import pygame

class Score():
    def __init__(self,score, textScore):
        self.score = score
        self.textScore = textScore

    def augmenterScore(self, nbLignesKilled, niveau):
        self.score += (25*nbLignesKilled+100*(nbLignesKilled-1))*niveau

    def affichage_TextScore(self,surface,posX,posY):
        self.font = pygame.font.SysFont('arial', 25)#Choix de la police
        self.label = self.font.render(self.textScore, 1,(255,255,255))#Choix tu texte
        surface.blit(self.label, (posX,posY ))#Affichage du texte

    def affichage_Score(self,surface,posX,posY):
        self.font = pygame.font.SysFont('arial', 25)#Choix de la police
        self.label = self.font.render(str(self.score), 1,(255,255,255))#Choix tu texte
        surface.blit(self.label, (posX,posY ))#Affichage du texte





#dans la gestion de la ligne cassée, avoir une fonction qui récupère le score et quil y ajoute 25 points
#si on est a kill 10 lignes, on passe au niveau suivant et chaque ligne valent 25 points de + par rapport au level précédent
