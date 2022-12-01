import pygame 
from settings import *

class Tile(pygame.sprite.Sprite):
	"""This class defines the tiles that will be used in the game. It inherits from pygame.sprite.Sprite class."""
	def __init__(self,pos,groups,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE))):
		super().__init__(groups)
		self.sprite_type = sprite_type
		self.image = surface
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-10)

class Box(Tile):
	"""This class defines the boxes that will be used in the game. It inherits from Tile class."""
	def __init__(self, pos, groups, sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE))):
		super().__init__(pos,groups,sprite_type,surface)
	
	def slide(self, direction):
		"""Function that slides the box in the direction the player is moving.

		:param direction: Direction the player is moving.
		:type direction: str
		"""
		if direction == 'left':
			self.rect.x -= 3 #Half the player's speed
			self.hitbox.center = self.rect.center
			self.check_collision('left')
		elif direction == 'right':
			self.rect.x += 3 #Half the player's speed
			self.hitbox.center = self.rect.center
			self.check_collision('right')
		elif direction == 'up':
			self.rect.y -= 3 #Half the player's speed
			self.hitbox.center = self.rect.center
			self.check_collision('up')
		elif direction == 'down':
			self.rect.y += 3 #Half the player's speed
			self.hitbox.center = self.rect.center
			self.check_collision('down')

	def check_collision(self, direction):
		"""Function that checks if the box is colliding with another box or a wall.
		
		:param direction: Direction the box is moving.
		:type direction: str
		"""
		for obstacle in self.groups()[1]:
			if id(obstacle) != id(self): #Checks if the obstacle is not the box itself
				if obstacle.hitbox.colliderect(self.hitbox):
					if direction == 'left':
						self.hitbox.left = obstacle.hitbox.right
						self.rect.center = self.hitbox.center
					elif direction == 'right':
						self.hitbox.right = obstacle.hitbox.left
						self.rect.center = self.hitbox.center
					elif direction == 'up':
						self.hitbox.top = obstacle.hitbox.bottom
						self.rect.center = self.hitbox.center
					elif direction == 'down':
						self.hitbox.bottom = obstacle.hitbox.top
						self.rect.center = self.hitbox.center