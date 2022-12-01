import pygame
import support
from settings import *
from tile import Tile, Box
from player import Player
from weapon import Weapon
from enemy import Enemy
from ui import UI
from particles import AnimationPlayer
from random import randint

class Level:
	"""Setting up the map and the sprites
	"""
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
  
		# UI setup
		self.ui=UI(self.player)

		# Particles setup
		self.animation_player = AnimationPlayer()
  
	def create_map(self):
		"""Create the map and the player"""

		#Importing the layouts
		layout = {
			'border': support.import_csv_layout('../layouts/mapa_border.csv'),
			'iceable': support.import_csv_layout('../layouts/mapa_iceable.csv'),
			'fireable': support.import_csv_layout('../layouts/mapa_fireable.csv'),
			'rockable': support.import_csv_layout('../layouts/mapa_rockable.csv'),
			'spiritable': support.import_csv_layout('../layouts/mapa_spiritable.csv'),
			'grass': support.import_csv_layout('../layouts/mapa_grass.csv'),
			'house_elements': support.import_csv_layout('../layouts/mapa_house_elements.csv'),
			'dungeon_wall': support.import_csv_layout('../layouts/mapa_dungeon_wall.csv'),
			'dungeon': support.import_csv_layout('../layouts/mapa_dungeon.csv'),
			'house_tiles': support.import_csv_layout('../layouts/mapa_house_tiles.csv'),
			'boxes': support.import_csv_layout('../layouts/mapa_boxes.csv'),
			'nature': support.import_csv_layout('../layouts/mapa_nature.csv'),
			'door': support.import_csv_layout('../layouts/mapa_door.csv'),
			'houses': support.import_csv_layout('../layouts/mapa_houses.csv'),
			'entities': support.import_csv_layout('../layouts/mapa_entities.csv'),
		}

		#Creating the sprites
		graphics = {
			'grass': support.import_tiles('../graphics/grass/grass.png'),
			'house_tileset': support.import_tiles('../graphics/tilemap/TilesetHouse.png'),
			'nature_tileset': support.import_tiles('../graphics/tilemap/TilesetNature.png'),
			'element_tileset': support.import_tiles('../graphics/tilemap/TilesetElement.png'),
			'box_tileset': support.import_tiles('../graphics/objects/boxes/boxes.png'),
			'door_tileset': support.import_tiles('../graphics/objects/door/door.png'),
			'dungeon_tileset': support.import_tiles('../graphics/tilemap/TilesetDungeon.png'),
			'dungeon_interior_tileset': support.import_tiles('../graphics/tilemap/TilesetInterior.png'),
			'spiritable_tileset': support.import_tiles('../graphics/objects/spiritable/spiritable.png'),
			'rockable_tileset': support.import_tiles('../graphics/objects/rockable/rockable.png'),
			'fireable_tileset': support.import_tiles('../graphics/objects/fireable/fireable.png'),
			'iceable_tileset': support.import_tiles('../graphics/objects/iceable/iceable.png'),
		}
		#Iterating over each layout and positioning the sprites
		for style, layout in layout.items():
			for row_index, row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1': #Case where the tile is not empty
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style == 'border':
							Tile((x,y), [self.obstacle_sprites],'invisible')
						if style == 'grass':
							grass_tile = graphics['grass'][int(col)]
							Tile((x,y), [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites],'grass', grass_tile)
						if style == 'nature':
							nature_tile = graphics['nature_tileset'][int(col)]
							Tile((x,y), [self.visible_sprites, self.obstacle_sprites],'nature', nature_tile)
						if style == 'house_elements':
							house_tile = graphics['element_tileset'][int(col)]
							Tile((x,y), [self.visible_sprites, self.obstacle_sprites],'house_element', house_tile)
						if style == 'house_tiles':
							house_tile = graphics['house_tileset'][int(col)]
							Tile((x,y), [self.visible_sprites, self.obstacle_sprites],'house_tile', house_tile)
						if style == 'houses':
							house_tile = graphics['house_tileset'][int(col)]
							Tile((x,y), [self.visible_sprites, self.obstacle_sprites],'house', house_tile)
						if style == 'boxes':
							box_tile = graphics['box_tileset'][int(col)]
							Box((x,y), [self.visible_sprites, self.obstacle_sprites],'box', box_tile)
						if style == 'door':
							door_tile = graphics['door_tileset'][0]
							Tile((x,y), [self.visible_sprites, self.obstacle_sprites],'door', door_tile)
						if style == 'dungeon':
							dungeon_tile = graphics['dungeon_tileset'][int(col)]
							Tile((x,y), [self.visible_sprites, self.obstacle_sprites],'dungeon', dungeon_tile)
						if style == 'dungeon_wall':
							dungeon_tile = graphics['dungeon_interior_tileset'][int(col)]
							Tile((x,y), [self.visible_sprites, self.obstacle_sprites],'dungeon_wall', dungeon_tile)
						if style == 'spiritable':
							spiritable_tile = graphics['spiritable_tileset'][int(col)]
							Tile((x,y), [self.visible_sprites, self.obstacle_sprites],'spiritable', spiritable_tile)
						if style == 'rockable':
							rockable_tile = graphics['rockable_tileset'][int(col)]
							Tile((x,y), [self.visible_sprites, self.obstacle_sprites],'rockable', rockable_tile)
						if style == 'fireable':
							fireable_tile = graphics['fireable_tileset'][int(col)]
							Tile((x,y), [self.visible_sprites, self.obstacle_sprites],'fireable', fireable_tile)
						if style == 'iceable':
							iceable_tile = graphics['iceable_tileset'][int(col)]
							Tile((x,y), [self.visible_sprites, self.obstacle_sprites],'iceable', iceable_tile)
						if style == 'entities':
							if col == '4': #Player
								print('Player')
								self.player = Player((x,y), [self.visible_sprites],
                          				self.obstacle_sprites, 
                              			self.create_attack, 
                                 		self.end_attack)
							else:
								if col == '0':
									monsters_name = 'raccoon'
								elif col == '1':
									monsters_name = 'flam'
								elif col == '2':
									monsters_name = 'snake'
								elif col == '3':
									monsters_name = 'squid'
								# elif col == '5':
								# 	monsters_name = 'giant_flam'
								# elif col == '6':
								# 	monsters_name = 'giant_raccoon'
								Enemy(monsters_name,(x,y),
									[self.visible_sprites,self.attackable_sprites],
									self.obstacle_sprites,
									self.damage_player,
									self.death_particles)

	# Methods to create and kill attack's sprites
	def create_attack(self):
		self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])

	def end_attack(self):
		if self.current_attack:
			self.current_attack.kill()
		self.current_attack = None
  
	def player_attack(self):
		if self.attack_sprites:
			for attack in self.attack_sprites:
				# Check if the attack is colliding with an enemy
				collisions = pygame.sprite.spritecollide(attack, self.attackable_sprites, False)
				
				for target_sprite in collisions:
					if target_sprite.sprite_type == 'grass' and self.player.weapon_index == 1:
						pos = target_sprite.rect.center
						offset = pygame.math.Vector2(0,75)
						for leaf in range(randint(3,6)):
							self.animation_player.create_grass_particles(pos - offset, [self.visible_sprites])
						target_sprite.kill()
					
					elif target_sprite.sprite_type == 'enemy':
						target_sprite.get_damage(self.player, attack.sprite_type)
    
	def damage_player(self, amount, attack_type):
		if self.player.vulnerable and not self.player.dashing:
			self.player.get_damage(amount)
			self.player.vulnerable = False
			self.player.hurt_time = pygame.time.get_ticks()
			self.animation_player.create_default_particles(attack_type, self.player.rect.center, [self.visible_sprites])

	def death_particles(self, particle_type, pos):
		self.animation_player.create_default_particles(particle_type, pos, self.visible_sprites)

	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()
		self.visible_sprites.enemy_update(self.player)
		self.player_attack()
		self.ui.display(self.player)

class YsortCameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()

		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		# creating the floor
		self.floor_surf = pygame.image.load('../graphics/tilemap/mapa.png').convert()
		self.floor_surf = pygame.transform.scale(self.floor_surf, (7680,5760))
		self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

	    

	def custom_draw(self, player):

		# getting the offset
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# drawing the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf,floor_offset_pos)

		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery): # This line sorts the hitboxes so the sprite with the higher y position appears over the others during the sprite overlap
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image, offset_pos)
	
	def enemy_update(self,player):
		enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
		for enemy in enemy_sprites:
			enemy.enemy_update(player)
