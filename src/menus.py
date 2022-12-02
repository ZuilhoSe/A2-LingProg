import pygame as pg
from settings import *
import sys
from buttons import Button

class Menus:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGTH))
		self.volume=VOLUME

	def get_font(self, size):
		return pg.font.Font("../graphics/HUD/Font/NormalFont.ttf", size)

	def main_menu(self):
		while True:
			main_menu_screen = self.screen

			main_menu_screen.fill("Black")

			menu_mouse_position = pg.mouse.get_pos()
			menu_text = self.get_font(MENU_FONT_SIZE).render("MAIN MENU", True, "#b68f40")
			menu_rect = menu_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.1)))

			
			play_button = Button(image=None, pos=(int(WIDTH/2), int(HEIGTH*0.35)), 
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
						return "play"
					if options_button.checkForInput(menu_mouse_position):
						return self.options_menu()
					if credits_button.checkForInput(menu_mouse_position):
						return self.credits_menu()
					if quit_button.checkForInput(menu_mouse_position):
						pg.quit()
						sys.exit()

			pg.display.update()
			
	def options_menu(self):
		while True:
			options_menu_screen = self.screen

			options_menu_screen.fill("Black")

			options_menu_mouse_position = pg.mouse.get_pos()
			options_text = self.get_font(MENU_FONT_SIZE).render("OPTIONS", True, "#b68f40")
			options_rect = options_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.05)))

			options_menu_screen.blit(options_text, options_rect)
			options_menu_screen.blit(pg.transform.scale(pg.image.load("../graphics/HUD/Dialog/ChoiceBox.png"),
									(768,144)), (int(WIDTH/5), int(HEIGTH*0.4)))

			music_button_up = Button(image=pg.transform.scale(pg.transform.rotate(
							pg.image.load("../graphics/HUD/arrow.png"),180),(64,64)), 
							pos=(int(8.5*(WIDTH/10)), int(HEIGTH*0.5)),
							text_input=None, font=self.get_font(int(MENU_FONT_SIZE/5)),
							base_color="#d7fcd4", hovering_color="White")
			music_button_down = Button(image=pg.transform.scale(pg.image.load("../graphics/HUD/arrow.png"),(64,64)), 
							pos=(int(1.5*(WIDTH/10)), int(HEIGTH*0.5)),
							text_input=None, font=self.get_font(int(MENU_FONT_SIZE/5)),
							base_color="#d7fcd4", hovering_color="White")
			back_button = Button(image=None, pos=(int(WIDTH/2), int(HEIGTH*0.9)), 
							text_input="BACK", font=self.get_font(MENU_FONT_SIZE), 
							base_color="#d7fcd4", hovering_color="White")

			for volume in range(0, self.volume):
				options_menu_screen.blit(pg.transform.scale(pg.image.load("../graphics/HUD/audio_icon/high_audio.png"),
									(70,70)), (int(2.28*(WIDTH/10)+volume*67)+10, int(HEIGTH*0.45)))


			for button in [music_button_up, music_button_down, back_button]:
				button.changeColor(options_menu_mouse_position)
				button.update(options_menu_screen)

			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()
				if event.type == pg.MOUSEBUTTONDOWN:
					if music_button_up.checkForInput(options_menu_mouse_position):
						if self.volume<10:
							self.volume+=1
							print(self.volume/10)
							pg.mixer.music.set_volume(self.volume/10)
					if music_button_down.checkForInput(options_menu_mouse_position):
						if self.volume>0:	
							self.volume-=1
							print(self.volume/10)
							pg.mixer.music.set_volume(self.volume/10)
					if back_button.checkForInput(options_menu_mouse_position):
						return self.main_menu()
				
			pg.display.update()
	   
	def pause_menu(self):
		pause_menu_screen = self.screen
		pause_menu_screen.fill("Black")
				
		pause_text = self.get_font(MENU_FONT_SIZE).render("PAUSE", True, "#b68f40")
		pause_rect = pause_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.1)))
		resume_text = self.get_font(int(MENU_FONT_SIZE/2)).render("Press    ENTER   to  resume", True, "#b68f40")
		resume_rect = resume_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.6)))
		
		pause_menu_screen.blit(pause_text, pause_rect)
		pause_menu_screen.blit(resume_text, resume_rect)
		pg.display.update()

	def credits_menu(self):
		while True:
			credits_menu_screen = self.screen
			credits_menu_screen.fill("Black")

			credits_text = self.get_font(MENU_FONT_SIZE).render("CREDITS", True, "#b68f40")
			credits_rect = credits_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.1)))
			credits_text1 = self.get_font(int(MENU_FONT_SIZE/2)).render("Made by:  ", True, "#b68f40")
			credits_rect1 = credits_text1.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.3)))
			credits_text2 = self.get_font(int(MENU_FONT_SIZE/2)).render("Bruno Lunardon", True, "#b68f40")
			credits_rect2 = credits_text2.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.4)))
			credits_text3 = self.get_font(int(MENU_FONT_SIZE/2)).render("George", True, "#b68f40")
			credits_rect3 = credits_text3.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.5)))
			credits_text4 = self.get_font(int(MENU_FONT_SIZE/2)).render("Zuilho", True, "#b68f40")
			credits_rect4 = credits_text4.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.6)))
			credits_text5 = self.get_font(int(MENU_FONT_SIZE/2)).render("Vini", True, "#b68f40")
			credits_rect5 = credits_text5.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.8)))

			credits_menu_screen.blit(credits_text, credits_rect)
			credits_menu_screen.blit(credits_text1, credits_rect1)
			credits_menu_screen.blit(credits_text2, credits_rect2)
			credits_menu_screen.blit(credits_text3, credits_rect3)
			credits_menu_screen.blit(credits_text4, credits_rect4)
			credits_menu_screen.blit(credits_text5, credits_rect5)

			back_button = Button(image=None, pos=(int(WIDTH/2), int(HEIGTH*0.9)),
							text_input="BACK", font=self.get_font(MENU_FONT_SIZE),
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