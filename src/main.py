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
		self.volume=pygame.mixer.music.set_volume(VOLUME/10)
		self.game_over= False
		#Village music
		pygame.mixer.music.load("../audio/village.ogg")
		pygame.mixer.music.play(-1)

	def menu(self):
		self.menu=Menus()
		if self.menu.main_menu():
			self.run()

	def run(self):
		while True:
			if self.level.player.alive:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_RETURN:
							self.is_paused = not self.is_paused
							self.pause_menu=Menus()
							self.pause_menu.pause_menu()
				while self.is_paused:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
							sys.exit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								self.is_paused = not self.is_paused

			while not self.level.player.alive:
				self.game_over_menu=Menus()
				self.game_over_menu.game_over_menu()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_RETURN:
							#Note the player restarts with the life you 
							#set up initialy but that shouldn't be a problem
							#since the player should start with full life
							self.level.player.alive=True
							volume=self.game_over_menu.game_over_menu()
							new_game = Game()
							new_game.volume=pygame.mixer.music.set_volume(volume/10)
							new_game.run()



			self.screen.fill('black')
			self.level.run()

			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.menu()