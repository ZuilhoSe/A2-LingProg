"""This module stores the classes and methods needed to create magic sprites."""

import pygame as pg
from settings import *
from entity import Entity
from support import import_folder
class MagicPlayer:
    """The MagicPlayer class import all the magics assets at once and calls the Projectile class to create the magics.
    """

    def __init__(self, animation_player):
        """Since it is created only once, the MagicPlayer doesn't need any specifications to be created, but it needs to know the AnimationPlayer class.

        :param animation_player: Class used to animate basic particles for the magics
        :type animation_player: particles.AnimationPlayer
        """

        self.animation_player = animation_player
        self.frames = {
            "fireball": import_folder("../graphics/particles/fireball/frames", rescale=1),
            "stone_edge": import_folder("../graphics/particles/stone_edge/frames", rescale=2),
            "ice_spike": import_folder("../graphics/particles/ice_spike/frames", rescale=2),
            "spirit_wind": import_folder("../graphics/particles/spirit/frames", rescale=2)
        }

    def heal(self, player, strength, cost, groups):
        """Calls the animation player to create healing particles, and increases player's health.

        :param player: The player class, so the method can access health and know its position
        :type player: player.Player
        :param strength: How much health will be recovered
        :type strength: int
        :param cost: How much mana will be deducted from the player
        :type cost: int
        :param groups: Wich groups the magic particles belong
        :type groups: list
        """
        if player.health < player.max_health and player.mana >= cost:
            player.mana -= cost
            player.health += strength
            offset = pg.math.Vector2(0,6)
            pg.mixer.Sound("../audio/heal.wav").play()
            self.animation_player.create_default_particles(player.magic, player.rect.center + offset, groups)
            if player.health >= player.max_health:
                player.health = player.max_health

    def projectile(self, player, cost, groups, obstacle_sprites, attackable_sprites):
        """Calls the Projectile class to create a projectile magic.

        :param player: The Player object, so the method can know it's position and access it's mana
        :type player: player.Player
        :param cost: How much mana will be deducted from the player
        :type cost: int
        :param groups: Wich groups the magic particles belong
        :type groups: list
        :param obstacle_sprites: Sprite group that contains the obstacles in the scenery
        :type obstacle_sprites: pygame.sprite.Group
        :param attackable_sprites: Sprite group that contains the enemy's sprites
        :type attackable_sprites: pygame.sprite.Group
        """

        if player.mana >= cost:
            player.mana -= cost

            facing = player.status.split("_")[0]
            if facing == "right": direction = pg.math.Vector2(1,0)
            elif facing == "left": direction = pg.math.Vector2(-1,0)
            elif facing == "up": direction = pg.math.Vector2(0,-1)
            elif facing == "down": direction = pg.math.Vector2(0,1)
        
            type = player.magic
            caster_rect = player.rect
            speed = magic_data[player.magic]["speed"]
            Projectile(type, direction, caster_rect, self.frames, groups, speed, obstacle_sprites, attackable_sprites, self.animation_player, False)

class MagicBoss:
    """The MagicPlayer class import all the magics assets at once and calls the Projectile class to create the magics.
    """

    def __init__(self, animation):
        """Since it is created only once, the MagicPlayer doesn't need any specifications to be created, but it needs to know the AnimationPlayer class.

        :param animation_player: Class used to animate basic particles for the magics
        :type animation_player: particles.AnimationPlayer
        """

        self.animation = animation
        self.frames = {
            "fireball": import_folder("../graphics/particles/fireball/frames", rescale=1)
        }

    def fireball(self, boss, groups, obstacle_sprites, player):
        """Calls the Projectile class to create a fireball.
        :param player: The Player object, so the method can know it's position and access it's mana
        :type player: player.Player
        :param cost: How much mana will be deducted from the player
        :type cost: int
        :param groups: Wich groups the magic particles belong
        :type groups: list
        :param obstacle_sprites: Sprite group that contains the obstacles in the scenery
        :type obstacle_sprites: pygame.sprite.Group
        :param attackable_sprites: Sprite group that contains the enemy's sprites
        :type attackable_sprites: pygame.sprite.Group
        """

    
        type = boss.magic_type
        caster_rect = boss.rect
        speed = boss.magic_speed
        Projectile(type, boss.direction, caster_rect, self.frames, groups, speed, obstacle_sprites, player, self.animation, True)
        
class Projectile(Entity):
    """This class creates a sprite in a certain direction, that moves at constant speed in that direction. This class inherits from the Entity class.
    """

    def __init__(self, type, direction, caster_rect, frames, groups, speed, obstacle_sprites, attackable_sprites, animation_player, cast_from_center):
        """The creation of a Projectile is kinda complex, due to the fact that the class is used by both the player and the enemies.

        :param type: Type of the projectile. This is used to define the frames, the damage, among other things.
        :type type: str
        :param direction: This is the direction the projectile will move, and the rotation of the images
        :type direction: pygame.math.Vector2
        :param caster_rect: This is the rect property from the sprite where the projectile will be cast
        :type caster_rect: pygame.sprite.Sprite.rect
        :param frames: These are the frames used to animate the projectile. It must be a list with images pointing to the RIGHT.
        :type frames: list
        :param groups: Wich groups the magic particles belong
        :type groups: list
        :param speed: Movement speed of the projectile
        :type speed: int
        :param obstacle_sprites: Sprite group that contains the obstacles in the scenery, so the project explodes when it collides with them
        :type obstacle_sprites: pygame.sprite.Group
        :param attackable_sprites: Sprite group that contains the enemy's sprites, so the enemies get damaged when they collide with a Projectile
        :type attackable_sprites: pygame.sprite.Group
        :param animation_player: Class used to animate basic particles for the magics
        :type animation_player: particles.AnimationPlayer
        :param cast_from_center: If True the projectile will be cast from the center of the caster_rect
        :type cast_from_center: bool
        """

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

        # Rotating and defining animation frames
        if direction != pg.math.Vector2(0,0):
            self.direction = direction.normalize()
        self.animation = []

        rotation_angle = pg.math.Vector2(1,0).angle_to(self.direction)
        for frame in frames[self.sprite_type]:
    
            rotated_frame = pg.transform.rotate(frame, -rotation_angle)
            self.animation.append(rotated_frame)

        self.image = self.animation[0]

        # Defining movement direction
        if cast_from_center:
            self.rect = self.image.get_rect(center=caster_rect.center)
        elif abs(self.direction.x) >= abs(self.direction.y):
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
        """This method is called once per loop to animate the frames over the images in the self.animation list.
        """

        # Loops over the frames
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animation):
            self.frame_index = 1

        # Set the image
        self.image = self.animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def die(self):
        """This method is called when the Projectile must end.
        """

        self.animation_player.create_default_particles(self.sprite_type + "_die", self.rect.center, [self.visible_sprites])
        self.kill()

    def timer(self):
        """This method verifies how long the projectile lasts, and kills it once it reaches the limit time.
        """

        current_time = pg.time.get_ticks()
        if current_time - self.creation_time >= self.life_expectancy:
            self.die() 

    def update(self):
        """This method sets what will be called everytime the game completes a main loop. Basically, it says what will be "updated" in each frame. 
        """

        self.move(self.speed)
        self.animate()
        self.timer()