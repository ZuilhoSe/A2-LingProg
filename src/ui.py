import pygame as pg
from settings import *

class UI:
	def __init__(self,player):
		self.display_surface=pg.display.get_surface()
		self.font = pg.font.Font(UI_FONT,UI_FONT_SIZE)
		self.max_health=player.max_health
		self.health=player.health
		self.max_mana=player.max_mana
		self.mana=player.mana

	def display(self,player):
		self.hearts(player)
		self.player_mana(player)

	def hearts(self,player):
		total_hearts=self.max_health//4
		total_full_hearts=self.health//4
		empty_hearts=total_hearts-total_full_hearts
		wich_quarter_heart=self.health%4
		there_is_quarter_heart=int(wich_quarter_heart!=0)
		for empty in range(empty_hearts-there_is_quarter_heart):
			self.display_surface.blit(pg.transform.scale(pg.image.load(EMPTY_HEART).
			convert_alpha(),(48,48)),((empty+total_full_hearts+there_is_quarter_heart)
			*75+30,25))
		for heart in range(total_full_hearts):
			self.display_surface.blit(pg.transform.scale(pg.image.load(FULL_HEART).
			convert_alpha(),(48,48)),(heart*75+30,25))
		if wich_quarter_heart==1:
			self.display_surface.blit(pg.transform.scale(pg.image.load(QUARTER_HEART).
			convert_alpha(),(48,48)),((total_full_hearts)*75+30,25))
		elif wich_quarter_heart==2:
			self.display_surface.blit(pg.transform.scale(pg.image.load(HALF_HEART).
			convert_alpha(),(48,48)),((total_full_hearts)*75+30,25))
		elif wich_quarter_heart==3:
			self.display_surface.blit(pg.transform.scale(pg.image.load(QUARTER_3_HEART).
			convert_alpha(),(48,48)),((total_full_hearts)*75+30,25))


	def player_mana(self,player):	
		total_mana=self.max_mana
		total_full_mana=self.mana
		empty_mana=total_mana-total_full_mana
		for empty in range(empty_mana):
			self.display_surface.blit(pg.transform.scale(pg.image.load(EMPTY_MANA).
			convert_alpha(),(36,44)),((empty+total_full_mana)*75+285,25))
		for mana in range(total_full_mana):
			self.display_surface.blit(pg.transform.scale(pg.image.load(FULL_MANA).
			convert_alpha(),(36,44)),(mana*75+285,25))