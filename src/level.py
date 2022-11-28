import pygame
import support
from settings import *
from tile import Tile
from player import Player
from weapon import Weapon
from enemy import Enemy
from ui import UI


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
  
		# UI setup
		self.ui=UI(self.player)
  
	def create_map(self):
		for row_index, row in enumerate(WORLD_MAP):
			for col_index, col in enumerate(row):
				x = col_index * TILESIZE
				y = row_index * TILESIZE
				if col == 'x':
					Tile((x,y), [self.visible_sprites, self.obstacle_sprites])
				if col == 'p':
					self.player = Player((x,y), [self.visible_sprites],
                          				self.obstacle_sprites, 
                              			self.create_attack, 
                                 		self.end_attack)
				if col == 'e':
					Enemy('squid',(x,y),
           				  [self.visible_sprites,self.attackable_sprites],
                 		  self.obstacle_sprites,
                     	  self.damage_player)
					

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
					if target_sprite.sprite_type == 'grass':
						target_sprite.kill()
					elif target_sprite.sprite_type == 'enemy':
						target_sprite.get_damage(self.player, attack.sprite_type)
    
    
	def damage_player(self, amount, atttack_type):

		if self.player.vulnerable:
			self.player.get_damage(amount)
			self.player.vulnerable = False
			self.player.hurt_time = pygame.time.get_ticks()
			print('Player health:', self.player.health)

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
