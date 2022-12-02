import pygame as pg
from settings import *
from entity import Entity
from support import import_folder

class MagicPlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player

    def fireball(self, player, cost, groups, obstacle_sprites):
        if player.mana >= cost:
            player.mana -= cost
        
        type = player.magic
        facing = player.status.split("_")[0]
        caster_rect = player.rect
        Projectile(type, facing, caster_rect, groups, 6, obstacle_sprites)

class Projectile(Entity):
    def __init__(self, type, facing, caster_rect, groups, speed, obstacle_sprites):
        
        super().__init__(groups)

        self.sprite_type = type
        self.facing = facing
        self.speed = speed
        self.obstacle_sprites = obstacle_sprites
        self.image = pg.image.load(f"../graphics/particles/fireball/{self.facing}/0.png")

        path = magic_data[self.sprite_type]["frames"]
        full_path =  path + self.facing
        self.animation = import_folder(full_path, rescale=1)

        # Defining the projectile direction
        if self.facing == "right": 
            direction = pg.math.Vector2(1,0)
            self.rect = self.image.get_rect(midleft = caster_rect.midright)

        elif self.facing == "left": 
            direction = pg.math.Vector2(-1,0)
            self.rect = self.image.get_rect(midright = caster_rect.midleft)

        elif self.facing == "up":
            direction = pg.math.Vector2(0,-1)
            self.rect = self.image.get_rect(midbottom = caster_rect.midtop) 
        
        elif self.facing == "down": 
            direction = pg.math.Vector2(0,1)
            self.rect = self.image.get_rect(midtop = caster_rect.midbottom)

        self.hitbox = self.rect.inflate(10, 10)

    def animate(self):
        # Loops over the frames
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animation):
            self.frame_index = 0

        # Set the image
        self.image = self.animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        self.move(self.speed)
        self.animate()