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

	def get_font(self, size):
		return pg.font.Font("../graphics/HUD/Font/NormalFont.ttf", size)

	def display(self,player):
		"""Displays the UI

		:param player: the player object
		:type player: Player
		"""		
		self.hearts_draw(player)
		self.mana_draw(player)
		self.weapon_draw(player)

	def hearts_draw(self,player):
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

	def mana_draw(self,player):
		total_mana=self.player.max_mana
		total_full_mana=int(self.player.mana)
		empty_mana=total_mana-total_full_mana

		for empty in range(empty_mana):
			self.display_surface.blit(pg.transform.scale(pg.image.load(EMPTY_MANA),(32,32)),((empty+total_full_mana)
			*75+30,75))
		for mana in range(total_full_mana):
			self.display_surface.blit(pg.transform.scale(pg.image.load(FULL_MANA),(32,32)),(mana*75+30,75))
		
		


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

	def weapon_draw(self,player):
		"""Displays the player's weapon

		:param player: the player object
		:type player: Player
		"""
		icon_sprite = pg.image.load("../graphics/HUD/NinePathRect/DialogueBubble.png")
		icon_sprite = pg.transform.scale(icon_sprite, (int(1.25*HEIGTH/10),int(1.25*HEIGTH/10)))
		weapon_sprite=weapon_data[player.weapon]["graphic"]
		weapon_sprite=pg.transform.scale(pg.image.load(weapon_sprite),(int(18*RATIO),int(42*RATIO)))
		weapon_sprite=pg.transform.rotate(weapon_sprite,-45)
		self.display_surface.blit(icon_sprite,(9*(WIDTH/10),(HEIGTH/40)))
		self.display_surface.blit(weapon_sprite,(int(9.18*(WIDTH/10)),int(2.3*(HEIGTH/40))))
		if player.weapon_standby:
			cooldown=pg.image.load("../graphics/HUD/NinePathRect/cooldown_mask.png")
			cooldown=pg.transform.scale(cooldown,(int(1.25*(HEIGTH/10)),int(1.25*(HEIGTH/10))))
			cooldown.set_alpha(150)		
			self.display_surface.blit(cooldown,(9*(WIDTH/10),(HEIGTH/40)))

	def magic_draw(self,player):
		"""Displays the player's magic

		:param player: the player object
		:type player: Player
		"""		
		if self.player.magic_standby:
			cooldown=pg.image.load("../graphics/HUD/NinePathRect/cooldown_mask.png")
			cooldown=pg.transform.scale(cooldown,(100,100))
			cooldown.set_alpha(150)		
			self.display_surface.blit(cooldown,(9*(WIDTH/10),(HEIGTH/40)))