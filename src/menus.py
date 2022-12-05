import pygame as pg
import enemy
from settings import *
import sys

class Menus:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGTH))
        self.volume=VOLUME
        self.sfx_vol=1

    def get_font(self, size):
        return pg.font.Font("../graphics/HUD/Font/NormalFont.ttf", size)

    def main_menu(self):
        while True:
            main_menu_screen = self.screen

            main_menu_screen.fill("Black")

            menu_text = self.get_font(MENU_FONT_SIZE).render("THE  LEGEND  OF  OLIVIA", True, "#b68f40")
            menu_rect = menu_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.1)))

            play_text= self.get_font(int(MENU_FONT_SIZE/2)).render("\"P\"   -   PLAY", True, "#b68f40")
            play_rect = play_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.3)))
            options_text= self.get_font(int(MENU_FONT_SIZE/2)).render("\"O\"   -   OPTIONS", True, "#b68f40")
            options_rect = options_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.5)))
            credits_text= self.get_font(int(MENU_FONT_SIZE/2)).render("\"C\"   -   CREDITS", True, "#b68f40")
            credits_rect = credits_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.7)))
            quit_text= self.get_font(int(MENU_FONT_SIZE/2)).render("\"Q\"   -   QUIT", True, "#b68f40")
            quit_rect = quit_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.9)))
            

            main_menu_screen.blit(menu_text, menu_rect)
            main_menu_screen.blit(play_text, play_rect)
            main_menu_screen.blit(options_text, options_rect)
            main_menu_screen.blit(credits_text, credits_rect)
            main_menu_screen.blit(quit_text, quit_rect)


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        return True
                    if event.key == pg.K_o:
                        self.options_menu()
                    if event.key == pg.K_c:
                        self.credits_menu()
                    if event.key == pg.K_q:
                        pg.quit()
                        sys.exit()

            pg.display.update()
            
    def options_menu(self):
        while True:
            options_menu_screen = self.screen

            options_menu_screen.fill("Black")

            options_text = self.get_font(int(8*MENU_FONT_SIZE/10)).render("OPTIONS", True, "#b68f40")
            options_rect = options_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.05)))
            back_text = self.get_font(int(8*MENU_FONT_SIZE/10)).render("BACK", True, "#b68f40")
            back_rect = back_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.95)))
            volume_text = self.get_font(int(MENU_FONT_SIZE/2)).render(f"VOLUME:  {self.volume}", True, "#b68f40")
            volume_rect = volume_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.15)))
            control_text = self.get_font(int(MENU_FONT_SIZE/4)).render("\"CTRL+UP\"   OR   \"CTRL+DOWN\"   TO  CONTROL  VOLUME", True, "#b68f40")
            control_rect = control_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.45)))
            sfx_text = self.get_font(int(MENU_FONT_SIZE/2)).render(f"SFX:  {self.sfx_vol}", True, "#b68f40")
            sfx_rect = sfx_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.55)))
            sfx_control_text = self.get_font(int(MENU_FONT_SIZE/4)).render("\"SHIFT+UP\"   OR   \"SHIFT+DOWN\"   TO  CONTROL  SFX", True, "#b68f40")
            sfx_control_rect = sfx_control_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.85)))

            options_menu_screen.blit(options_text, options_rect)
            options_menu_screen.blit(back_text, back_rect)
            options_menu_screen.blit(volume_text, volume_rect)
            options_menu_screen.blit(control_text, control_rect)
            options_menu_screen.blit(sfx_text, sfx_rect)
            options_menu_screen.blit(sfx_control_text, sfx_control_rect)
            options_menu_screen.blit(pg.transform.scale(pg.image.load("../graphics/HUD/Dialog/ChoiceBox.png"),
                                    (6*(WIDTH/10),HEIGTH/5)), (int(WIDTH/5), int(HEIGTH*0.2)))
            options_menu_screen.blit(pg.transform.scale(pg.image.load("../graphics/HUD/Dialog/ChoiceBox.png"),
                                    (6*(WIDTH/10),HEIGTH/5)), (int(WIDTH/5), int(HEIGTH*0.6)))


            for volume in range(0, self.volume):
                options_menu_screen.blit(pg.transform.scale(pg.image.load("../graphics/HUD/audio_icon/volume_bar.png"),
                                    (1.15*(WIDTH/20),(HEIGTH/10))), (int(2.28*(WIDTH/10)+volume*(WIDTH/20))+(WIDTH/51), int(HEIGTH*0.25)))
            for sfx_vol in range(0, self.sfx_vol):
                options_menu_screen.blit(pg.transform.scale(pg.image.load("../graphics/HUD/audio_icon/volume_bar.png"),
                                    (1.15*(WIDTH/20),(HEIGTH/10))), (int(2.28*(WIDTH/10)+sfx_vol*(WIDTH/20))+(WIDTH/51), int(HEIGTH*0.65)))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_b:
                        return self.main_menu()
                    if event.key == pg.K_UP and pg.key.get_mods() & pg.KMOD_CTRL: 
                            if self.volume<10:
                                self.volume+=1
                                pg.mixer.music.set_volume(self.volume/10)
                    if event.key == pg.K_DOWN and pg.key.get_mods() & pg.KMOD_CTRL:
                            if self.volume>0:	
                                self.volume-=1
                                pg.mixer.music.set_volume(self.volume/10)
                    if event.key == pg.K_UP and pg.key.get_mods() & pg.KMOD_SHIFT:
                        if self.sfx_vol<10:
                            self.sfx_vol+=1
                    if event.key == pg.K_DOWN and pg.key.get_mods() & pg.KMOD_SHIFT:
                        if self.sfx_vol>0:
                            self.sfx_vol-=1
                
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
            back_text = self.get_font(int(MENU_FONT_SIZE/2)).render("\"B\"   -   BACK", True, "#b68f40")
            back_rect = back_text.get_rect(center=(int(WIDTH/2), int(HEIGTH*0.95)))


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
            credits_menu_screen.blit(back_text, back_rect)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_b:
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
menu=Menus()
SFX_VOLUME = menu.sfx_vol