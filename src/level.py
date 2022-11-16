import pygame
from settings import *
from tile import Tile
from player import Player


class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YsortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

	def create_map(self):
		for row_index, row in enumerate(WORLD_MAP):
			for col_index, col in enumerate(row):
				x = col_index * TILESIZE
				y = row_index * TILESIZE
				if col == 'x':
					Tile((x,y), [self.visible_sprites, self.obstacle_sprites])
				if col == 'p':
					self.player = Player((x,y), [self.visible_sprites], self.obstacle_sprites)

	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()

class YsortCameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()

		self.display_surface = pygame.display.get_surface()
		self.offset = pygame.math.Vector2()

	def custom_draw(self, player):

		# Getting the Offset to move the camera every time the player crosses the map border
		screenx = self.display_surface.get_size()[0]
		screeny = self.display_surface.get_size()[1]
		self.offset.x = (player.rect.centerx // screenx) * screenx
		self.offset.y = (player.rect.centery // screeny) * screeny

		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery): # This line sorts the hitboxes so the sprite with the higher y position appears over the others during the sprite overlap
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image, offset_pos)