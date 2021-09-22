import pygame


class Button(pygame.sprite.Sprite):

    def __init__(self,x,y, image):
        # Appelle le constructeur de sprite
        pygame.sprite.Sprite.__init__(self)

        # Change l'image qu'affiche le sprite
        self.image = image
        #self.image = pygame.Surface([300, 100])
        # Remplis d'une couleur
        #self.image.fill((100, 100, 100, 255))

        # Récupère la position de l'image (et d'autres trucs)
        self.rect = self.image.get_rect()
        #Change la position
        self.rect.x = x
        self.rect.y = y
