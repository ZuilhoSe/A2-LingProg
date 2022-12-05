import pygame as pg
from settings import *
import sys
from buttons import Button

class Menus:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGTH))

	def get_font(self, size):
		return pg.font.Font("../graphics/HUD/Font/NormalFont.ttf", size)

	def main_menu(self):
		while True:
			main_menu_screen = self.screen

			main_menu_screen.fill("Black")

			menu_mouse_position = pg.mouse.get_pos()
			menu_text = self.get_font(MENU_FONT_SIZE).render("THE  LEGEND  OF  OPHELIA", True, "#b68f40")
			menu_rect = menu_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.1)))

			
			play_button = Button(image=None, pos=(int(WIDTH/2), int(HEIGTH*0.3)), 
							text_input="PLAY", font=self.get_font(MENU_FONT_SIZE), 
							base_color="#d7fcd4", hovering_color="White")
			options_button = Button(image=None, pos=(int(WIDTH/2), int(HEIGTH*0.5)),
							text_input="OPTIONS", font=self.get_font(MENU_FONT_SIZE),
							base_color="#d7fcd4", hovering_color="White")
			credits_button = Button(image=None, pos=(int(WIDTH/2), int(HEIGTH*0.7)), 
							text_input="CREDITS", font=self.get_font(MENU_FONT_SIZE), 
							base_color="#d7fcd4", hovering_color="White")
			quit_button = Button(image=None, pos=(int(WIDTH/2), int(HEIGTH*0.9)), 
							text_input="QUIT", font=self.get_font(MENU_FONT_SIZE), 
							base_color="#d7fcd4", hovering_color="White")

			main_menu_screen.blit(menu_text, menu_rect)

			

			for button in [play_button, options_button, credits_button, quit_button]:
				button.changeColor(menu_mouse_position)
				button.update(main_menu_screen)

			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()
				if event.type == pg.MOUSEBUTTONDOWN:
					if play_button.checkForInput(menu_mouse_position):
						return True
					if options_button.checkForInput(menu_mouse_position):
						return self.options_menu()
					if credits_button.checkForInput(menu_mouse_position):
						return self.credits_menu()
					if quit_button.checkForInput(menu_mouse_position):
						pg.quit()
						sys.exit()

			pg.display.update()
			
	def options_menu(self):
		global volum
		volum=VOLUME
		while True:
			options_menu_screen = self.screen

			options_menu_screen.fill("Black")

			options_menu_mouse_position = pg.mouse.get_pos()
			options_text = self.get_font(MENU_FONT_SIZE).render("OPTIONS", True, "#b68f40")
			options_rect = options_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.05)))

			options_menu_screen.blit(options_text, options_rect)
			options_menu_screen.blit(pg.transform.scale(pg.image.load("../graphics/HUD/Dialog/ChoiceBox.png"),
									(6*(WIDTH/10),HEIGTH/5)), (int(WIDTH/5), int(HEIGTH*0.4)))

			music_button_up = Button(image=pg.transform.scale(pg.transform.rotate(
							pg.image.load("../graphics/HUD/arrow.png"),180),(int(0.9*(HEIGTH/10)),int(0.9*(HEIGTH/10)))), 
							pos=(int(8.5*(WIDTH/10)), int(HEIGTH*0.5)),
							text_input=None, font=self.get_font(int(MENU_FONT_SIZE/5)),
							base_color="#d7fcd4", hovering_color="White")
			music_button_down = Button(image=pg.transform.scale(pg.image.load("../graphics/HUD/arrow.png"),(int(0.9*(HEIGTH/10)),int(0.9*(HEIGTH/10)))), 
							pos=(int(1.5*(WIDTH/10)), int(HEIGTH*0.5)),
							text_input=None, font=self.get_font(int(MENU_FONT_SIZE/5)),
							base_color="#d7fcd4", hovering_color="White")
			back_button = Button(image=None, pos=(int(WIDTH/2), int(HEIGTH*0.9)), 
							text_input="BACK", font=self.get_font(MENU_FONT_SIZE), 
							base_color="#d7fcd4", hovering_color="White")

			for volume in range(0, volum):
				options_menu_screen.blit(pg.transform.scale(pg.image.load("../graphics/HUD/audio_icon/volume_bar.png"),
									(1.15*(WIDTH/20),(HEIGTH/10))), (int(2.28*(WIDTH/10)+volume*(WIDTH/20))+(WIDTH/51), int(HEIGTH*0.45)))


			for button in [music_button_up, music_button_down, back_button]:
				button.changeColor(options_menu_mouse_position)
				button.update(options_menu_screen)

			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()
				if event.type == pg.MOUSEBUTTONDOWN:
					if music_button_up.checkForInput(options_menu_mouse_position):
						if volum<10:
							volum+=1
							pg.mixer.music.set_volume(volum/10)
					if music_button_down.checkForInput(options_menu_mouse_position):
						if volum>0:	
							volum-=1
							pg.mixer.music.set_volume(volum/10)
					if back_button.checkForInput(options_menu_mouse_position):
						return self.main_menu()
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_UP:
						if volum<10:
							volum+=1
							pg.mixer.music.set_volume(volum/10)	
					if event.key == pg.K_DOWN:
						if volum>0:	
							volum-=1
							pg.mixer.music.set_volume(volum/10)
				
			pg.display.update()
	   
	def pause_menu(self):
		pause_menu_screen = self.screen
		pause_menu_screen.fill("Black")
				
		pause_text = self.get_font(MENU_FONT_SIZE).render("PAUSE", True, "#b68f40")
		pause_rect = pause_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.1)))
		resume_text = self.get_font(int(MENU_FONT_SIZE/2)).render("Press    ENTER   to  resume", True, "#b68f40")
		resume_rect = resume_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.375)))
		main_menu_text = self.get_font(int(MENU_FONT_SIZE/2)).render("Press    ESC   to  main menu", True, "#b68f40")
		main_menu_rect = main_menu_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.5)))
		restar_text = self.get_font(int(MENU_FONT_SIZE/2)).render("Press    R   to  restart", True, "#b68f40")
		restar_rect = restar_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.625)))
		quit_text = self.get_font(int(MENU_FONT_SIZE/2)).render("Press    Q   to  quit", True, "#b68f40")
		quit_rect = quit_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.75)))

		pause_menu_screen.blit(pause_text, pause_rect)
		pause_menu_screen.blit(resume_text, resume_rect)
		pause_menu_screen.blit(main_menu_text, main_menu_rect)
		pause_menu_screen.blit(restar_text, restar_rect)
		pause_menu_screen.blit(quit_text, quit_rect)
		pg.display.update()

	def credits_menu(self):
		while True:
			credits_menu_screen = self.screen
			credits_menu_screen.fill("Black")

			credits_text = self.get_font(int(8*(MENU_FONT_SIZE/10))).render("CREDITS", True, "#b68f40")
			credits_rect = credits_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.05)))
			made_by_text = self.get_font(int(MENU_FONT_SIZE/3)).render("MADE  BY:  ", True, "#b68f40")
			made_by_rect = made_by_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.2)))
			author1 = self.get_font(int(MENU_FONT_SIZE/3)).render("LUNAS", True, "#b68f40")
			author1_rect = author1.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.25)))
			author2 = self.get_font(int(MENU_FONT_SIZE/3)).render("JOOJ", True, "#b68f40")
			author2_rect = author2.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.3)))
			author3 = self.get_font(int(MENU_FONT_SIZE/3)).render("VINI", True, "#b68f40")
			author3_rect = author3.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.35)))
			author4 = self.get_font(int(MENU_FONT_SIZE/3)).render("ZUZU", True, "#b68f40")
			author4_rect = author4.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.4)))
			thanks_text = self.get_font(int(MENU_FONT_SIZE/2)).render("THANKS  TO:  ", True, "#b68f40")
			thanks_rect = thanks_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.5)))
			thanks1 = self.get_font(int(MENU_FONT_SIZE/3)).render("PIXEL  ARCHIPEL  FOR  THE  MAJORITY  OF  SPRITES", True, "#b68f40")
			thanks1_rect = thanks1.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.575)))
			patreon = self.get_font(int(MENU_FONT_SIZE/3)).render("PATREON:", True, "#b68f40")
			patreon_rect = patreon.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.65)))
			patreon_link = self.get_font(int(MENU_FONT_SIZE/3)).render("https://www.patreon.com/pixelarchipel", True, "#b68f40")
			patreon_link_rect = patreon_link.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.725)))



			credits_menu_screen.blit(credits_text, credits_rect)
			credits_menu_screen.blit(made_by_text, made_by_rect)
			credits_menu_screen.blit(author1, author1_rect)
			credits_menu_screen.blit(author2, author2_rect)
			credits_menu_screen.blit(author3, author3_rect)
			credits_menu_screen.blit(author4, author4_rect)
			credits_menu_screen.blit(thanks_text, thanks_rect)
			credits_menu_screen.blit(thanks1, thanks1_rect)
			credits_menu_screen.blit(patreon, patreon_rect)
			credits_menu_screen.blit(patreon_link, patreon_link_rect)

			back_button = Button(image=None, pos=(int(WIDTH/2), int(HEIGTH*0.9)),
							text_input="BACK", font=self.get_font(int(7.5*(MENU_FONT_SIZE/10))),
							base_color="#d7fcd4", hovering_color="White")

			back_button.changeColor(pg.mouse.get_pos())
			back_button.update(credits_menu_screen)

			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()
				if event.type == pg.MOUSEBUTTONDOWN:
					if back_button.checkForInput(pg.mouse.get_pos()):
						return self.main_menu()

			pg.display.update()

	def game_over_menu(self):
			game_over_menu_screen = self.screen
			game_over_menu_screen.fill("Black")

			game_over_text = self.get_font(MENU_FONT_SIZE).render("GAME OVER", True, "#b68f40")
			game_over_rect = game_over_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.1)))
			game_over_text1 = self.get_font(int(MENU_FONT_SIZE/2)).render("Press    ENTER   to  restart", True, "#b68f40")
			game_over_rect1 = game_over_text1.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.375)))
			game_over_text2 = self.get_font(int(MENU_FONT_SIZE/2)).render("Press    ESC   to  main menu", True, "#b68f40")
			game_over_rect2 = game_over_text2.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.5)))
			game_over_text3 = self.get_font(int(MENU_FONT_SIZE/2)).render("Press    Q   to  quit", True, "#b68f40")
			game_over_rect3 = game_over_text3.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.625)))

			game_over_menu_screen.blit(game_over_text, game_over_rect)
			game_over_menu_screen.blit(game_over_text1, game_over_rect1)
			game_over_menu_screen.blit(game_over_text2, game_over_rect2)
			game_over_menu_screen.blit(game_over_text3, game_over_rect3)
			
			pg.display.update()

	def vol(self):
		return volum
