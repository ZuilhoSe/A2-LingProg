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
            menu_text = self.get_font(MENU_FONT_SIZE).render("MAIN MENU", True, "#b68f40")
            menu_rect = menu_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.1)))

            
            play_button = Button(image=None, pos=(int(WIDTH/2), int(HEIGTH*0.35)), 
                            text_input="PLAY", font=self.get_font(MENU_FONT_SIZE), 
                            base_color="#d7fcd4", hovering_color="White")
            options_button = Button(image=None, pos=(int(WIDTH/2), int(HEIGTH*0.55)), 
                            text_input="OPTIONS", font=self.get_font(MENU_FONT_SIZE), 
                            base_color="#d7fcd4", hovering_color="White")
            quit_button = Button(image=None, pos=(int(WIDTH/2), int(HEIGTH*0.75)), 
                            text_input="QUIT", font=self.get_font(MENU_FONT_SIZE), 
                            base_color="#d7fcd4", hovering_color="White")

            main_menu_screen.blit(menu_text, menu_rect)

            

            for button in [play_button, options_button, quit_button]:
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
            options_rect = options_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.2)))

            options_menu_screen.blit(options_text, options_rect)

            back_button = Button(image=None, pos=(int(WIDTH/2), int(HEIGTH*0.8)), 
                            text_input="BACK", font=self.get_font(MENU_FONT_SIZE), 
                            base_color="#d7fcd4", hovering_color="White")

            for button in [back_button]:
                button.changeColor(options_menu_mouse_position)
                button.update(options_menu_screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if back_button.checkForInput(options_menu_mouse_position):
                        return self.main_menu()
                
            pg.display.update()
       
    def pause_menu(self):
        pause_menu_screen = self.screen

        pause_menu_screen.fill("Black")

        pause_text = self.get_font(MENU_FONT_SIZE).render("PAUSE", True, "#b68f40")
        pause_rect = pause_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.5)))
        resume_text = self.get_font(int(MENU_FONT_SIZE/2)).render("Press    ENTER   to  resume", True, "#b68f40")
        resume_rect = resume_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.6)))

        pause_menu_screen.blit(pause_text, pause_rect)
        pause_menu_screen.blit(resume_text, resume_rect)

        pg.display.update()
        




            