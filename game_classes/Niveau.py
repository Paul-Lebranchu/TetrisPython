import pygame

class Niveau():
    def __init__(self,niveau, textNiveau):
        self.niveau = niveau
        self.textNiveau = textNiveau
        self.nbLignesKilled = 0

    def augmenterNiveau(self, nbLignesKilled):
        self.nbLignesKilled += nbLignesKilled
        if(self.nbLignesKilled >= 10):
            self.nbLignesKilled = 0
            self.niveau += 1

    def affichage_TextNiveau(self,surface,posX,posY):
        self.font = pygame.font.SysFont('arial', 25)#Choix de la police
        self.label = self.font.render(self.textNiveau, 1,(255,255,255))#Choix tu texte
        surface.blit(self.label, (posX,posY ))#Affichage du texte

    def affichage_Niveau(self,surface,posX,posY):
        self.font = pygame.font.SysFont('arial', 25)#Choix de la police
        self.label = self.font.render(str(self.niveau), 1,(255,255,255))#Choix tu texte
        surface.blit(self.label, (posX,posY ))#Affichage du texte

    def niveauActuel(self):
        return self.niveau
