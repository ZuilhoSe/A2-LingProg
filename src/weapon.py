import pygame as pg

class Weapon(pg.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)

        # Getting the player's direction
        direction = player.status.split("_")[0]
    
        # Weapon graphics
        full_path = f"../graphics/weapons/{player.weapon}/{direction}.png"
        not_image = pg.image.load(full_path).convert_alpha()
        not_width, not_height = not_image.get_width(), not_image.get_height()
        self.image = pg.transform.scale(not_image, (not_width*4, not_height*4))
        
        # Setting the direction of the attack
        if direction == "right":
            self.rect = self.image.get_rect(midleft = player.rect.midright + pg.math.Vector2(0, 16))
        elif direction == "left":
            self.rect = self.image.get_rect(midright = player.rect.midleft + pg.math.Vector2(0, 16))
        elif direction == "up":
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + pg.math.Vector2(-12, 0))
        elif direction == "down":
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pg.math.Vector2(-10, 0))