import pygame as pg
from settings import *
from support import import_folder
from entity import Entity
import menus

class Villager(Entity):
    def __init__(self, pos, groups, image, player):

        super().__init__(groups)
        self.image = image #Path de TESTE, não está pronto
        self.image = pg.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)
        self.hitbox.center = self.rect.center
        self.sprite_type = "villager"
        self.player = player

    