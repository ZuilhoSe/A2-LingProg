import pygame, sys
from settings import *
from level import Level
from menus import menu

class Game:
	def __init__(self):
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Joguinho de testes que não está pronto')
		self.clock = pygame.time.Clock()
		self.level = Level()
		self.menu=menu
		self.is_paused=False
		self.volume=pygame.mixer.music.set_volume(VOLUME/10)
		#Village music
		pygame.mixer.music.load("../audio/village.ogg")
		pygame.mixer.music.play(-1)

	def start(self):
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
							self.menu.pause_menu()
				while self.is_paused:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
							sys.exit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								self.is_paused = not self.is_paused
							if event.key == pygame.K_ESCAPE:
								self.is_paused = not self.is_paused
								self.menu.main_menu()
							if event.key == pygame.K_q:
								pygame.quit()
								sys.exit()
							if event.key == pygame.K_r:
								volume=self.menu.volume
								new_game=Game()
								new_game.volume=pygame.mixer.music.set_volume(volume/10)
								new_game.run()
							
			while not self.level.player.alive:
				self.menu.game_over_menu()
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
							volume=self.menu.volume
							new_game = Game()
							new_game.volume=pygame.mixer.music.set_volume(volume/10)
							new_game.run()
						if event.key == pygame.K_ESCAPE:
							self.level.player.alive=True
							volume=self.menu.vol()
							new_game = Game()
							new_game.volume=pygame.mixer.music.set_volume(volume/10)
							self.menu.main_menu()
							new_game.run()
						if event.key == pygame.K_q:
							pygame.quit()
							sys.exit()
							
			self.screen.fill('black')
			self.level.run()

			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.start()