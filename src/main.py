import pygame, sys
from settings import *
from level import Level
from menus import Menus


class Game:
	def __init__(self):
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Joguinho de testes que não está pronto')
		self.clock = pygame.time.Clock()
		self.level = Level()
		self.is_paused=False
		#Village music
		pygame.mixer.music.load("../audio/village.ogg")
		pygame.mixer.music.set_volume(VOLUME/10)
		pygame.mixer.music.play(-1)

	def menu(self):
		self.menu=Menus()
		# print(self.menu.main_menu())
		if self.menu.main_menu() == "play":
			self.run()

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						self.is_paused = not self.is_paused
						self.pause=Menus()
						self.pause.pause_menu()	
			while self.is_paused:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_RETURN:
							self.is_paused = not self.is_paused

			self.screen.fill('black')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.menu()