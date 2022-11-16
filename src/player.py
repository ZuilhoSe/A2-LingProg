import pygame as pg
from settings import *
from support import import_folder

class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pg.image.load("../graphics/test/player.png").convert_alpha() #Path de TESTE, não está pronto
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)

        # Here we have a few important variables for our player's proper function

        self.player_assets() # Import player graphic assets

        self.direction = pg.math.Vector2() # This is a vector representing the sprite's movement direction
        self.speed = 5 # This will be used to define the speed movement in pixels/frame

        self.status = "down"
        self.frame_index = 0
        self.animation_speed = 0.15

        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
    
        # IMPORTANT: This defines wich group of sprites is going to collide against the player, and will be passed as an argument at __init__
        self.obstacle_sprites = obstacle_sprites

    # Gets the assets to animate the player
    def player_assets(self):
        character_path = "../graphics/player/"
        self.animations = { 
            "up": [], "down": [], "left": [], "right": [], 
            "up_idle": [], "down_idle": [], "left_idle": [], "right_idle": [], 
            "up_attack": [], "down_attack": [], "left_attack": [], "right_attack": [] 
        }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    # Defining how our inputs afect the characters movement vector
    def input(self):
        keys = pg.key.get_pressed()

        if not self.attacking:
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
        if keys[pg.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pg.time.get_ticks()
            print("Attack!")

        # And now the magic input
        if keys[pg.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pg.time.get_ticks()
            print("Magic!")

    # Defining how the vector and the speed interact to create movement
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize() # Here we normalize the vector, so if you go in two simultaneous directions, you don't become The Flash

        self.hitbox.x += self.direction.x * speed
        self.collision("x")

        self.hitbox.y += self.direction.y * speed
        self.collision("y")

        self.rect.center = self.hitbox.center   

    # Defining the collision behaviour
    def collision(self, direction):
        if direction == "x":
            for obstacle in self.obstacle_sprites:
                if obstacle.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # The player is moving right, so we have a collision to the right
                        self.hitbox.right = obstacle.hitbox.left
                    if self.direction.x < 0: # The player is moving left, so we have a collision to the left
                        self.hitbox.left = obstacle.hitbox.right

        if direction == "y":
            for obstacle in self.obstacle_sprites:
                if obstacle.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # The player is moving down, so we have a collision at the bottom
                        self.hitbox.bottom = obstacle.hitbox.top
                    if self.direction.y < 0: # The player is moving up, so we have a collision to the top
                        self.hitbox.top = obstacle.hitbox.bottom

    #Defining some action's cooldowns
    def cooldowns(self):
        current_time = pg.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

     # Gets the player status to apply the correct animation
    def get_status(self):

        # Idle
        if self.direction.x == 0 and self.direction.y == 0 and not "idle" in self.status:
            if "attack" in self.status:
                self.status = self.status.replace("_attack","_idle")
            elif not self.attacking:
                self.status = self.status + "_idle"

        # Attacking
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not "attack" in self.status:
                if "idle" in self.status:
                    self.status = self.status.replace("_idle","_attack")
                else:
                    self.status = self.status + "_attack"

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

    def update(self):
        self.input()
        self.move(self.speed)
        self.get_status()
        self.animate()
        self.cooldowns()