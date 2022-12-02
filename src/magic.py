import pygame as pg
from settings import *
from entity import Entity
from support import import_folder

class MagicPlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player

    def fireball(self, player, cost, groups, obstacle_sprites, attackable_sprites):
        if player.mana >= cost:
            player.mana -= cost
    
            type = player.magic
            facing = player.status.split("_")[0]
            caster_rect = player.rect
            Projectile(type, facing, caster_rect, groups, 6, obstacle_sprites, attackable_sprites, self.animation_player)

class Projectile(Entity):
    def __init__(self, type, facing, caster_rect, groups, speed, obstacle_sprites, attackable_sprites, animation_player):
        
        super().__init__(groups)
        self.creation_time = pg.time.get_ticks()
        self.life_expectancy = 1200
        self.visible_sprites = groups[0]
        self.sprite_type = type
        self.facing = facing
        self.speed = speed
        self.obstacle_sprites = obstacle_sprites
        self.attackable_sprites = attackable_sprites
        self.image = pg.image.load(f"../graphics/particles/fireball/{self.facing}/0.png")
        self.animation_player = animation_player

        path = magic_data[self.sprite_type]["frames"]
        full_path =  path + self.facing
        self.animation = import_folder(full_path, rescale=1)

        # Defining the projectile direction
        if self.facing == "right": 
            self.direction = pg.math.Vector2(1,0)
            self.rect = self.image.get_rect(midleft = caster_rect.midright)

        elif self.facing == "left": 
            self.direction = pg.math.Vector2(-1,0)
            self.rect = self.image.get_rect(midright = caster_rect.midleft)

        elif self.facing == "up":
            self.direction = pg.math.Vector2(0,-1)
            self.rect = self.image.get_rect(midbottom = caster_rect.midtop) 
        
        elif self.facing == "down": 
            self.direction = pg.math.Vector2(0,1)
            self.rect = self.image.get_rect(midtop = caster_rect.midbottom)

        self.hitbox = self.rect

    def animate(self):
        # Loops over the frames
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animation):
            self.frame_index = 1

        # Set the image
        self.image = self.animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def die(self):
        self.animation_player.create_default_particles(self.sprite_type + "_die", self.rect.center, [self.visible_sprites])
        self.kill()

    def timer(self):
        current_time = pg.time.get_ticks()
        if current_time - self.creation_time >= self.life_expectancy:
            self.die() 

    def update(self):
        self.move(self.speed)
        self.animate()
        self.timer()