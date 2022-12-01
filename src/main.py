import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self):
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Joguinho de testes que não está pronto')
		self.clock = pygame.time.Clock()
		self.level = Level()

		#Village music
		pygame.mixer.music.load("../audio/village.ogg")
		pygame.mixer.music.set_volume(0.2)
		pygame.mixer.music.play(-1)

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()	