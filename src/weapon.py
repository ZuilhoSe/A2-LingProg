import pygame as pg

class Weapon(pg.sprite.Sprite):
    """This class carries the assets to correctly create a weapon in the player's hand during an attack. It inherits from pygame.sprite.Sprite class.
    """

    def __init__(self, player, groups, attack_particles):
        """A Weapon is created every time the player cast a basic attack, and is soon deleted when the attack is over.

        :param player: The class must receive the Player object to know it's position and direction
        :type player: Player
        :param groups: List of tile groups the Weapon will belong
        :type groups: list
        """

        super().__init__(groups)
        self.sprite_type = 'weapon'

        # Getting the player's direction
        self.direction = player.status.split("_")[0]
    
        # Weapon graphics
        full_path = f"../graphics/weapons/{player.weapon}/{self.direction}.png"
        not_image = pg.image.load(full_path).convert_alpha()
        not_width, not_height = not_image.get_width(), not_image.get_height()
        self.image = pg.transform.scale(not_image, (not_width*4, not_height*4))
        self.attack_particles = attack_particles
        
        # Setting the direction and the particle animation of the attack
        if self.direction == "right":
            self.rect = self.image.get_rect(midleft = player.rect.midright + pg.math.Vector2(0, 16))
            if player.weapon_index == 1:
                self.attack_particles("attack_x", self.rect.center)

        elif self.direction == "left":
            self.rect = self.image.get_rect(midright = player.rect.midleft + pg.math.Vector2(0, 16))
            if player.weapon_index == 1:
                self.attack_particles("flip_attack_x", self.rect.center)

        elif self.direction == "up":
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + pg.math.Vector2(-12, 0))
            if player.weapon_index == 1:    
                self.attack_particles("attack_y", self.rect.center)

        elif self.direction == "down":
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pg.math.Vector2(-10, 0))
            if player.weapon_index == 1:
               self.attack_particles("flip_attack_y", self.rect.center)