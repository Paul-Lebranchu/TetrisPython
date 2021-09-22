import pygame
#from os import path

#img_dir = path.join(path.dirname(__file__), '../assets/img')
#music_dir = path.join(path.direname(__file__), '../assets/music')

class LoadingAssets():

	def __init__(self):
		pass;

	def loadImage(self,name):
		#Chargement des sprites=
		assets = pygame.image.load(name).convert_alpha()
		return assets

	def loadSound(self,name):
		pass;
