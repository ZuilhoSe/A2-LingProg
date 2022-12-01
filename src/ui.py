import pygame as pg
from settings import *

class UI:
	def __init__(self,player):
		"""Initializes the UI

		:param player: the player object
		:type player: Player
		"""		

		self.display_surface=pg.display.get_surface()
		self.font = pg.font.Font(UI_FONT,UI_FONT_SIZE)
		self.player = player
		self.max_health=self.player.max_health
		self.health=self.player.health



	def display(self,player):
		"""Displays the UI

		:param player: the player object
		:type player: Player
		"""		
		self.hearts(player)

	def hearts(self,player):
		"""Displays the player's health

		:param player: the player object
		:type player: Player
		"""        

		total_hearts=self.max_health//4
		total_full_hearts=self.health//4
		empty_hearts=total_hearts-total_full_hearts
		wich_quarter_heart=self.health%4
		there_is_quarter_heart=int(wich_quarter_heart!=0)
		self.health=self.player.health
		for empty in range(empty_hearts-there_is_quarter_heart):
			self.display_surface.blit(pg.transform.scale(pg.image.load(EMPTY_HEART),(48,48)),((empty+total_full_hearts+there_is_quarter_heart)
			*75+30,25))
		for heart in range(total_full_hearts):
			self.display_surface.blit(pg.transform.scale(pg.image.load(FULL_HEART),(48,48)),(heart*75+30,25))
		if wich_quarter_heart==1:
			self.display_surface.blit(pg.transform.scale(pg.image.load(QUARTER_HEART),(48,48)),((total_full_hearts)*75+30,25))
		elif wich_quarter_heart==2:
			self.display_surface.blit(pg.transform.scale(pg.image.load(HALF_HEART),(48,48)),((total_full_hearts)*75+30,25))
		elif wich_quarter_heart==3:
			self.display_surface.blit(pg.transform.scale(pg.image.load(QUARTER_3_HEART),(48,48)),((total_full_hearts)*75+30,25))