import pygame as pg
from settings import *
from entity import Entity
from support import import_folder

class MagicPlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player
        self.frames = {
            "fireball": import_folder("../graphics/particles/fireball/frames", rescale=1)
        }

    def heal(self, player, strength, cost, groups):
        if player.mana >= cost:
            player.mana -= cost
            player.health += strength
            offset = pg.math.Vector2(0,6)
            self.animation_player.create_default_particles("aura", player.rect.center + offset, groups)
            if player.health >= player.max_health:
                player.health = player.max_health

    def fireball(self, player, cost, groups, obstacle_sprites, attackable_sprites):
        if player.mana >= cost:
            player.mana -= cost

            facing = player.status.split("_")[0]
            if facing == "right": direction = pg.math.Vector2(1,0)
            elif facing == "left": direction = pg.math.Vector2(-1,0)
            elif facing == "up": direction = pg.math.Vector2(0,-1)
            elif facing == "down": direction = pg.math.Vector2(0,1)
        
            type = player.magic
            caster_rect = player.rect
            speed = 6
            Projectile(type, direction, caster_rect, self.frames, groups, speed, obstacle_sprites, attackable_sprites, self.animation_player)

class Projectile(Entity):
    def __init__(self, type, direction, caster_rect, frames, groups, speed, obstacle_sprites, attackable_sprites, animation_player):
        
        super().__init__(groups)
        self.sprite_type = type

        # How long the projectile lasts
        self.creation_time = pg.time.get_ticks()
        self.life_expectancy = 1200

        #Some important sprite groups
        self.visible_sprites = groups[0]
        self.obstacle_sprites = obstacle_sprites
        self.attackable_sprites = attackable_sprites
        
        #And an important method
        self.animation_player = animation_player

        # Defining animation frames
        self.direction = direction.normalize()
        self.animation = []

        rotation_angle = pg.math.Vector2(1,0).angle_to(self.direction)
        for frame in frames[self.sprite_type]:
            rotated_frame = pg.transform.rotate(frame, -rotation_angle)
            self.animation.append(rotated_frame)

        self.image = self.animation[0]

        # Defining movement direction
        if abs(self.direction.x) >= abs(self.direction.y):
            if self.direction.x > 0:
                self.rect = self.image.get_rect(midleft = caster_rect.midright)
            else:
                self.rect = self.image.get_rect(midright = caster_rect.midleft)
        else:
            if self.direction.y > 0:
                self.rect = self.image.get_rect(midtop = caster_rect.midbottom)
            else:
                self.rect = self.image.get_rect(midbottom = caster_rect.midtop) 

        self.hitbox = self.rect
        self.speed = speed

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