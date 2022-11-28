import pygame as pg
from settings import *
from support import import_folder
from entity import Entity

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, create_attack, end_attack):
        super().__init__(groups)
        self.image = pg.image.load("../graphics/test/player.png").convert_alpha() #Path de TESTE, não está pronto
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)

        # Here we have a few important variables for our player's proper function

        self.player_assets() # Import player graphic assets

        self.status = "down"

        self.create_attack = create_attack
        self.end_attack = end_attack
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

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

        self.stats = {"health": 100, "energy": 60, "attack": 10, "magic": 4, "speed": 6}
        self.health = self.stats["health"]
        self.health = 7
        self.max_health=12
        self.energy = self.stats["energy"]
        self.speed = self.stats["speed"] # This will be used to define the speed movement in pixels/frame
        # IMPORTANT: This defines wich group of sprites is going to collide against the player, and will be passed as an argument at __init__
        self.obstacle_sprites = obstacle_sprites
        
        #damage timer
        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_duration = 500

    # Gets the assets to animate the player
    def player_assets(self):
        character_path = "../graphics/player/"
        self.animations = { 
            "up": [], "down": [], "left": [], "right": [], 
            "up_idle": [], "down_idle": [], "left_idle": [], "right_idle": [], 
            "up_attack": [], "down_attack": [], "left_attack": [], "right_attack": [],
            "up_dash": [], "down_dash": [], "left_dash": [], "right_dash": []
        }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    # Defining how our inputs afect the characters movement vector
    def input(self):
        keys = pg.key.get_pressed()

        if not self.attacking and not self.dashing:
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
        if keys[pg.K_SPACE] and not self.attacking and not self.weapon_standby:
            self.attacking = True
            self.weapon_standby = True
            self.attack_time = pg.time.get_ticks()
            self.weapon_time = pg.time.get_ticks()
            self.create_attack()

        # And the magic input
        # if keys[pg.K_LCTRL] and not self.attacking:
        #     self.attacking = True
        #     self.attack_time = pg.time.get_ticks()

        # Defining the dash input
        if keys[pg.K_LSHIFT] and not self.attacking and not self.dash_wait and not "idle" in self.status:
            self.dashing = True
            self.dash_wait = True
            self.speed += self.dash_speed          
            self.dash_time = pg.time.get_ticks()
 
    #Defining some action's cooldowns
    def cooldowns(self):
        current_time = pg.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.end_attack()

        if self.weapon_standby:
            if current_time - self.weapon_time >= weapon_data[self.weapon]["cooldown"]:
                self.weapon_standby = False
                
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

     # Gets the player status to apply the correct animation
    def get_status(self):

        # Idle
        if self.direction.x == 0 and self.direction.y == 0 and not "idle" in self.status:
            if "attack" in self.status:
                self.status = self.status.replace("_attack","_idle")
            elif "dash" in self.status:
                    self.status = self.status.replace("_dash","_idle")
            elif not self.attacking and not self.dashing:
                self.status = self.status + "_idle"

        # Attacking
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not "attack" in self.status:
                if "idle" in self.status:
                    self.status = self.status.replace("_idle","_attack")
                elif "dash" in self.status:
                    self.status = self.status.replace("_dash","_attack")
                else:
                    self.status = self.status + "_attack"

        # Dash
        if self.dashing and not "dash" in self.status:
            if "attack" in self.status:
                self.status = self.status.replace("_attack","_dash")
            elif "idle" in self.status:
                self.status = self.status.replace("_idle","_dash")
            else:
                self.status = self.status + "_dash"

    # Animates the player according to it's status
    def animate(self):
        animation = self.animations[self.status]

        # Loops over the frames
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # Set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)


    #this method should be called when the player is hit by an enemy
    def get_damage(self,dmg):
        """This method should be called when the player is hit by an enemy

        :param dmg: the damage the player will take
        :type dmg: int
        """        

        if self.health>0:
            self.health-=dmg


    def update(self):
        self.input()
        self.move(self.speed)
        self.get_status()
        self.animate()
        self.cooldowns()