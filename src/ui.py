"""Module that creates the UI"""

import pygame as pg
import sys
from settings import *
import time

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

	def get_font(self, size):
		return pg.font.Font("../graphics/HUD/Font/NormalFont.ttf", size)

	def display(self,player):
		"""Displays the UI

		:param player: the player object
		:type player: Player
		"""		
		self.hearts_draw()
		self.mana_draw()
		self.weapon_draw()
		self.magic_draw()

	def hearts_draw(self):
		"""Displays the player's health

		:param player: the player object
		:type player: Player
		""" 
		self.health=self.player.health
		full_heart=pg.image.load(FULL_HEART)
		empty_heart=pg.image.load(EMPTY_HEART)
		half_heart=pg.image.load(HALF_HEART)
		quarter_heart=pg.image.load(QUARTER_HEART)
		quarter_3_heart=pg.image.load(QUARTER_3_HEART)
		full_heart=pg.transform.scale(full_heart,(48*RATIO,48*RATIO))
		empty_heart=pg.transform.scale(empty_heart,(48*RATIO,48*RATIO))
		half_heart=pg.transform.scale(half_heart,(48*RATIO,48*RATIO))
		quarter_heart=pg.transform.scale(quarter_heart,(48*RATIO,48*RATIO))
		quarter_3_heart=pg.transform.scale(quarter_3_heart,(48*RATIO,48*RATIO))

		total_hearts=self.max_health//4
		total_full_hearts=self.health//4
		empty_hearts=total_hearts-total_full_hearts
		wich_quarter_heart=self.health%4
		there_is_quarter_heart=int(wich_quarter_heart!=0)



		for empty in range(empty_hearts-there_is_quarter_heart):
			self.display_surface.blit(empty_heart,(((empty+total_full_hearts+there_is_quarter_heart)
			*75+30)*RATIO,25*RATIO))
		for heart in range(total_full_hearts):
			self.display_surface.blit(full_heart,((heart*75+30)*RATIO,25*RATIO))
		if wich_quarter_heart==1:
			self.display_surface.blit(quarter_heart,(((total_full_hearts)*75+30)*RATIO,25*RATIO))
		elif wich_quarter_heart==2:
			self.display_surface.blit(half_heart,(((total_full_hearts)*75+30)*RATIO,25*RATIO))
		elif wich_quarter_heart==3:
			self.display_surface.blit(quarter_3_heart,(((total_full_hearts)*75+30)*RATIO,25*RATIO))

	def mana_draw(self):
		total=self.player.max_mana
		total_full=int(self.player.mana)

		empty=total-total_full
		
		rows_of_full=total_full//5
		remaining_full=total_full%5
		rows_of_empty=empty//5
		remaining_empty=empty%5
		there_is_remaining=int(remaining_full!=0)
		full_mana=pg.image.load(FULL_MANA)
		empty_mana=pg.image.load(EMPTY_MANA)
		full_mana=pg.transform.scale(full_mana,(32*RATIO,32*RATIO))
		empty_mana=pg.transform.scale(empty_mana,(32*RATIO,32*RATIO))



		for row in range(rows_of_full):
			for mana in range(5):
				self.display_surface.blit(full_mana,((mana*75+30)*RATIO,(row*50+75)*RATIO))
		for mana in range(remaining_full):
			self.display_surface.blit(full_mana,((mana*75+30)*RATIO,(rows_of_full*50+75)*RATIO))
		for mana in range(remaining_empty):
			self.display_surface.blit(empty_mana,(((mana+remaining_full)*75+30)*RATIO,(rows_of_full*50+75)*RATIO))
		for row in range(rows_of_empty):
			for mana in range(5):
				self.display_surface.blit(empty_mana,((mana*75+30)*RATIO,((row+rows_of_full+there_is_remaining)*50+75)*RATIO))
		
	def display_dialogue_box(self):
		"""Displays the dialogue box
		"""		
		dialogue_box = pg.image.load('../graphics/HUD/Dialog/DialogueBoxSimple.png')
		self.dialogue_box_x = dialogue_box.get_width()
		self.dialogue_box_y = dialogue_box.get_height()	
		dialogue_box = pg.transform.scale(dialogue_box, (self.dialogue_box_x*4, self.dialogue_box_y*4))
		self.display_surface.blit(dialogue_box, dialogue_box.get_rect(center=(int(WIDTH/2), int(HEIGTH-self.dialogue_box_y*2))))

	def display_dialogue(self, text_list):
		"""Displays the dialogue

		:param text_list: the text to be displayed
		:type text_list: list
		"""		
		self.display_dialogue_box()
		begin_y = HEIGTH - self.dialogue_box_y*4 + 50
		for text in text_list:
			text = text.replace('\n', '')
			text = text.upper()
			text = self.get_font(12).render(text, True, "#000000")
			text_x = text.get_width()
			text_y = text.get_height()
			text = pg.transform.scale(text, (text_x*2, text_y*2))
			self.display_surface.blit(text, text.get_rect(center=(int(WIDTH/2), begin_y)))
			begin_y += text_y + 40

	def weapon_draw(self):
		"""Displays the player's weapon

		:param player: the player object
		:type player: Player
		"""
		icon_sprite = pg.image.load("../graphics/HUD/NinePathRect/DialogueBubble.png")
		icon_sprite = pg.transform.scale(icon_sprite, (int(0.7*WIDTH/10),int(0.7*WIDTH/10)))
		weapon_sprite=weapon_data[self.player.weapon]["graphic"]
		weapon_sprite=pg.transform.scale(pg.image.load(weapon_sprite),(int(18*RATIO),int(42*RATIO)))
		weapon_sprite=pg.transform.rotate(weapon_sprite,-45)
		self.display_surface.blit(icon_sprite,(9*(WIDTH/10),(HEIGTH/40)))
		self.display_surface.blit(weapon_sprite,(int(9.18*(WIDTH/10)),int(2.3*(HEIGTH/40))))
		if self.player.weapon_standby:
			cooldown=pg.image.load("../graphics/HUD/NinePathRect/cooldown_mask.png")
			cooldown=pg.transform.scale(cooldown,(int(0.7*(WIDTH/10)),int(0.7*(WIDTH/10))))
			cooldown.set_alpha(150)		
			self.display_surface.blit(cooldown,(9*(WIDTH/10),(HEIGTH/40)))

	def magic_draw(self):
		"""Displays the player's magic

		:param player: the player object
		:type player: Player
		"""		

		icon_sprite = pg.image.load("../graphics/HUD/NinePathRect/DialogueBubble.png")
		icon_sprite = pg.transform.scale(icon_sprite, (int(0.7*WIDTH/10),int(0.7*WIDTH/10)))
		if self.player.magic: 
			magic_sprite=magic_data[self.player.magic]["graphic"]
			magic_sprite=pg.image.load(magic_sprite)
			magic_sprite=pg.transform.scale(magic_sprite,(int(48*RATIO),int(48*RATIO)))
		if self.player.magic!=None:
			self.display_surface.blit(icon_sprite,(int(8*(WIDTH/10)),int((HEIGTH/40))))
			self.display_surface.blit(magic_sprite,(int(8.18*(WIDTH/10)),int(2.3*(HEIGTH/40))))
			if self.player.magic_standby and self.player.mana>=magic_data[self.player.magic]["cost"]:
				cooldown=pg.image.load("../graphics/HUD/NinePathRect/cooldown_mask.png")
				cooldown=pg.transform.scale(cooldown,(int(0.7*WIDTH/10),int(0.7*WIDTH/10)))
				cooldown.set_alpha(150)		
				self.display_surface.blit(cooldown,(int(8*(WIDTH/10)),int((HEIGTH/40))))
			if self.player.mana<magic_data[self.player.magic]["cost"]:
					no_mana=pg.image.load("../graphics/HUD/NinePathRect/no_mana_mask.png")
					no_mana=pg.transform.scale(no_mana,(int(0.7*WIDTH/10),int(0.7*WIDTH/10)))
					no_mana.set_alpha(150)		
					self.display_surface.blit(no_mana,(int(8*(WIDTH/10)),int((HEIGTH/40))))