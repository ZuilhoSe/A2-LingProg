"""This module is dedicated to the class and methods involving the player and it's interactions."""

import pygame as pg
from settings import *
from support import import_folder
from entity import Entity

class Player(Entity):
    """This class carries most of the important properties and methods to the player's controls and functionalities. It inherits from the class Entity, in the entity module.
    """

    def __init__(self, pos, groups, obstacle_sprites, create_attack, end_attack, create_magic):
        """The class Player is created inside the class Level, and most of it's interactions come from it. The init method carries most of player's important varaiables, such as stats and cooldown values.

        :param pos: Receives coordinates where the player's tile will be spawned in the map, in the format: (x,y)
        :type pos: tuple
        :param groups: List of tile groups the Player will belong
        :type groups: list
        :param obstacle_sprites: Group of sprites the player will interact through collision
        :type obstacle_sprites: pg.sprite.Group
        :param create_attack: Method the Level uses to create a Weapon in the player's hand. The Player must know this method to call it through the Level class.
        :type create_attack: method
        :param end_attack: Method the Level uses to delete the Weapon sprite once an attack is over. The Player must know this method to call it through the Level class.
        :type end_attack: method
        :param create_magic: Method the Level uses to create the magic's sprites. The Player must know this method to call it through the Level class.
        :type create_magic: method
        """

        super().__init__(groups)
        self.image = pg.image.load("../graphics/test/player.png").convert_alpha() #Path de TESTE, não está pronto
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)

        # Here we have a few important variables for our player's proper function

        self.player_assets() # Import player graphic assets

        self.status = "down"

        self.create_attack = create_attack
        self.end_attack = end_attack
        self.create_magic = create_magic
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        self.special = False
        self.special_cooldown = 300

        self.dashing = False
        self.dash_wait = False
        self.dash_time = None
        self.dash_cooldown = 1000
        self.dash_duration = 200
        self.dash_speed = 12

        self.weapon_index = 1 #IMPORTANT to change the weapon
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.weapon_time = None
        self.weapon_standby = False

        self.magic_index = 0 #IMPORTANT to change the magic equipped
        self.magic_list = list(magic_data.keys())
        self.magic = self.magic_list[0]
        self.magic_time = None
        self.magic_standby = False
        
        self.magic_can_switch = True
        self.magic_switch_cooldown = 300
        self.magic_switch_time = None

        self.stats = {"health": 12, "mana": 10, "speed": 6}
        self.health = self.stats["health"]
        self.max_health = self.stats["health"]
        self.mana = self.stats["mana"]
        self.speed = self.stats["speed"] # This will be used to define the speed movement in pixels/frame
        
        # IMPORTANT: This defines wich group of sprites is going to collide against the player, and will be passed as an argument at __init__
        self.obstacle_sprites = obstacle_sprites
        
        #damage timer
        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_duration = 500

        #Importing Sounds
        self.sword_attack = pg.mixer.Sound("../audio/sword.wav")
        self.stick_attack = pg.mixer.Sound("../audio/stick.wav")
        self.sword_attack.set_volume(0.2)
        self.stick_attack.set_volume(0.2)

    def player_assets(self):
        """Import the assets to animate the player, such as walking and attacking sprites.
        """

        character_path = "../graphics/player/"
        self.animations = { 
            "up": [], "down": [], "left": [], "right": [], 
            "up_idle": [], "down_idle": [], "left_idle": [], "right_idle": [], 
            "up_attack": [], "down_attack": [], "left_attack": [], "right_attack": [],
            "up_dash": [], "down_dash": [], "left_dash": [], "right_dash": [],
            "special": []
        }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        """Defines how player's keyboard inputs affects the character, with movement and attack comands.
        """

        keys = pg.key.get_pressed()

        if not self.attacking and not self.dashing and not self.special:
            # First for up and down movement
            if keys[pg.K_UP]:
                self.direction.y = -1
                self.status = "up"
            elif keys[pg.K_DOWN]:
                self.direction.y = 1
                self.status = "down"
            else:
                self.direction.y = 0
            
            # Then for left and right movement
            if keys[pg.K_RIGHT]:
                self.direction.x = 1
                self.status = "right"
            elif keys[pg.K_LEFT]:
                self.direction.x = -1
                self.status = "left"
            else:
                self.direction.x = 0

        # Now defining the attack input
        if keys[pg.K_SPACE] and not self.attacking and not self.weapon_standby and not self.special:
            self.attacking = True
            self.weapon_standby = True
            self.attack_time = pg.time.get_ticks()
            self.weapon_time = pg.time.get_ticks()

            self.create_attack()

            if self.weapon_index == 0:
                self.stick_attack.play()
            elif self.weapon_index == 1:
                self.sword_attack.play()

        # And the magic input
        if keys[pg.K_LCTRL] and self.magic and not self.attacking and not self.magic_standby and not self.special:
            
            if self.magic == "heal":
                self.special = True
            else:
                self.attacking = True
                self.attack_time = pg.time.get_ticks()
    
            self.magic_standby = True
            self.magic_time = pg.time.get_ticks()

            strength = magic_data[self.magic]["strength"]
            cost = magic_data[self.magic]["cost"]
            self.create_magic(strength, cost)

        # For switching magics:
        if keys[pg.K_e] and self.magic and self.magic_can_switch and not self.attacking and not self.special:
            
            self.magic_switch_time = pg.time.get_ticks()
            self.magic_can_switch = False
            
            self.magic_index += 1
            if self.magic_index >= len(self.magic_list):
                self.magic_index = 0
            self.magic = self.magic_list[self.magic_index]

        # Defining the dash input
        if keys[pg.K_LSHIFT] and not self.attacking and not self.dash_wait and not "idle" in self.status and not self.special:
            self.dashing = True
            self.dash_wait = True
            self.speed += self.dash_speed          
            self.dash_time = pg.time.get_ticks()
 
    def cooldowns(self):
        """Defines the player's cooldowns behaviour, such as attack, dash and vulnerability cooldowns.
        """

        current_time = pg.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.end_attack()

        if self.weapon_standby:
            if current_time - self.weapon_time >= weapon_data[self.weapon]["cooldown"]:
                self.weapon_standby = False
                
        if self.magic_standby:
            if current_time - self.magic_time >= magic_data[self.magic]["cooldown"]:
                self.magic_standby = False
                
        if not self.magic_can_switch:
            if current_time - self.magic_switch_time >= self.magic_switch_cooldown:
                self.magic_can_switch = True

        if self.special:
            if current_time - self.magic_time >= self.special_cooldown:
                self.special = False

        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invulnerability_duration:
                self.vulnerable = True
        
        if self.dashing:
            if current_time - self.dash_time >= self.dash_duration:
                self.speed = self.stats["speed"]
                self.dashing = False

        if self.dash_wait:
            if current_time - self.dash_time >= self.dash_cooldown:
                self.dash_wait = False

    def get_status(self):
        """This method sets the character self.status property according to the action in course.
        """

        # Idle
        if self.direction.x == 0 and self.direction.y == 0 and not "idle" in self.status and not self.special:
            if "attack" in self.status:
                self.status = self.status.replace("_attack","_idle")
            elif "dash" in self.status:
                    self.status = self.status.replace("_dash","_idle")
            elif self.status == "special":
                self.status = "down_idle"
            elif not self.attacking and not self.dashing:
                self.status = self.status + "_idle"

        # Attacking
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not "attack" in self.status and self.status != "special":
                if "idle" in self.status:
                    self.status = self.status.replace("_idle","_attack")
                elif "dash" in self.status:
                    self.status = self.status.replace("_dash","_attack")
                else:
                    self.status = self.status + "_attack"

        # Special
        if self.special:
            self.direction.x = 0
            self.direction.y = 0
            if self.status != "special":
                self.status = "special"

        # Dash
        if self.dashing and not "dash" in self.status:
            if "attack" in self.status:
                self.status = self.status.replace("_attack","_dash")
            elif "idle" in self.status:
                self.status = self.status.replace("_idle","_dash")
            else:
                self.status = self.status + "_dash"

    def animate(self):
        """Uses the self.status property to correctly set the character's animation sprites. 
        """

        animation = self.animations[self.status]

        # Loops over the frames
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # Set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def get_damage(self, dmg):
        """ This method should be called when the player is hit by an enemy.

        :param dmg: the damage the player will take
        :type dmg: int
        """  

        if self.health > 0:
            self.health -= dmg

    def mana_regen(self):
        """ Defines a passive mana regeneation for the player.
        """

        if self.mana < self.stats["mana"]:
            self.mana += 0.005
        else:
            self.mana = self.stats["mana"]

    def level_up(self, level):
        """This level gives the player new magics after certain events.

        :param level: This parameter defines wich level the player is going to level up, and wich magic he will gain.
        :type level: int
        """
        
        if level == 0:
            self.weapon_index = 1
        
        new_magic = list(magic_data.keys)[level]
        if new_magic not in self.magic_list:
            self.magic_list.append(new_magic)

        self.magic = self.magic_list[0]

    def update(self):
        """This method sets what will be called everytime the game completes a main loop. Basically, it says what will be "updated" in each frame. 
        """

        self.cooldowns()
        self.get_status()
        self.input()
        self.move(self.speed)
        self.animate()
        self.mana_regen()