"""Module that creates the villagers."""

import pygame as pg
from settings import *
from support import import_folder
from entity import Entity
from ui import UI

class Villager(Entity):
    def __init__(self, pos, groups, image, player, speech):
        """Initializes the villager

        :param pos: Beginning position
        :type pos: tuple
        :param groups: Grups to add the villager to
        :type groups: list
        :param image: Image of the villager
        :type image: Surface
        :param player: Player object
        :type player: Player
        :param speech: Speech of the villager
        :type speech: List
        """
        super().__init__(groups)
        #Player
        self.player = player
        
        #Images
        self.image = image 
        self.image = pg.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)
        self.hitbox.center = self.rect.center
        
        #Type
        self.sprite_type = "villager"
        
        #UI and dialogue
        self.ui=UI(self.player)
        self.speech = speech

        #Importing Sounds
        self.voice = pg.mixer.Sound("../audio/voice.wav")
        self.voice.set_volume(0.1)

    def check_talk(self):
        """Checks if the player is close enough to talk to the villager"""
        if self.player.rect.colliderect(self.hitbox):
            self.ui.display_dialogue(self.speech)
            self.voice.play()
    
    def update(self):
        """Updates the villager"""
        self.check_talk()
    