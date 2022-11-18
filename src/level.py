import pygame
import support
from settings import *
from tile import Tile
from player import Player
from weapon import Weapon


class Level:
	def __init__(self):
		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YsortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# Attack sprites
		self.current_attack = None
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

	def create_map(self):
		maps_csv = {
			'border': support.import_csv_layout('../layouts/mapa_border.csv'),
			'boxes': support.import_csv_layout('../layouts/mapa_boxes.csv'),
			'door': support.import_csv_layout('../layouts/mapa_door.csv'),
			'dungeon_wall': support.import_csv_layout('../layouts/mapa_dungeon_wall.csv'),
			'dungeon': support.import_csv_layout('../layouts/mapa_dungeon.csv'),
			'fireable': support.import_csv_layout('../layouts/mapa_fireable.csv'),
			'grass': support.import_csv_layout('../layouts/mapa_grass.csv'),
			'house_tiles': support.import_csv_layout('../layouts/mapa_house_tiles.csv'),
			'houses': support.import_csv_layout('../layouts/mapa_houses.csv'),
			'iceable': support.import_csv_layout('../layouts/mapa_iceable.csv'),
			'nature': support.import_csv_layout('../layouts/mapa_nature.csv'),
			'rockable': support.import_csv_layout('../layouts/mapa_rockable.csv'),
			'spiritable': support.import_csv_layout('../layouts/mapa_spiritable.csv'),
		}
		tiles_graphics = {
			'grass': support.import_tiles('../graphics/grass/grass.png'),
			'boxes': support.import_tiles('../graphics/objects/boxes/boxes.png'),
			'door': support.import_tiles('../graphics/objects/door/door.png'),
			'fireable': support.import_tiles('../graphics/objects/fireable/fireable.png'),
			'iceable': support.import_tiles('../graphics/objects/iceable/iceable.png'),
			'rockable': support.import_tiles('../graphics/objects/rockable/rockable.png'),
			'spiritable': support.import_tiles('../graphics/objects/spiritable/spiritable.png'),
			'nature': support.import_tiles('../graphics/tilemap/TilesetNature.png'),
			'house': support.import_tiles('../graphics/tilemap/TilesetHouse.png'),
		}

		print(tiles_graphics['grass'][0])

		for style, layout in maps_csv.items():
			for row_index, row in enumerate(layout):
				for col_index, col in enumerate(row):
					x = col_index * TILESIZE
					y = row_index * TILESIZE
					if col != '-1':
						#if style == 'border':
							#Tile((x,y), [self.visible_sprites,self.obstacle_sprites], 'obstacle')
						if style == 'grass':
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'grass', tiles_graphics['grass'][int(col)])
						if style == 'boxes':
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object', tiles_graphics['boxes'][int(col)])
						if style == 'fireable':
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object', tiles_graphics['fireable'][int(col)])
						if style == 'iceable':
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object', tiles_graphics['iceable'][int(col)])
						if style == 'rockable':
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object', tiles_graphics['rockable'][int(col)])
						if style == 'spiritable':
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object', tiles_graphics['spiritable'][int(col)])
						if style == 'nature':
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'nature', tiles_graphics['nature'][int(col)])
						if style == 'houses':
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'house', tiles_graphics['house'][int(col)])
						if style == 'house_tiles':
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'house', tiles_graphics['house'][int(col)])
						

		self.player = Player((3000,2000),[self.visible_sprites],self.obstacle_sprites, self.create_attack, self.end_attack())

	# Methods to create and kill attack's sprites
	def create_attack(self):
		self.current_attack = Weapon(self.player, [self.visible_sprites])

	def end_attack(self):
		if self.current_attack:
			self.current_attack.kill()
		self.current_attack = None

	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()

class YsortCameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()

		self.display_surface = pygame.display.get_surface()
		self.offset = pygame.math.Vector2()

		# creating the floor
		self.floor_surf = pygame.image.load('../graphics/tilemap/mapa.png').convert()
		self.floor_surf = pygame.transform.scale(self.floor_surf, (7680,5760))
		self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

	    

	def custom_draw(self, player):

		# Getting the Offset to move the camera every time the player crosses the map border
		screenx = self.display_surface.get_size()[0]
		screeny = self.display_surface.get_size()[1]
		self.offset.x = (player.rect.centerx // screenx) * screenx
		self.offset.y = (player.rect.centery // screeny) * screeny

		# drawing the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf,floor_offset_pos)

		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery): # This line sorts the hitboxes so the sprite with the higher y position appears over the others during the sprite overlap
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image, offset_pos)