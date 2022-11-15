import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pg.image.load("../graphics/test/player.png").convert_alpha() #Path de TESTE, não está pronto
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pg.math.Vector2() # This is a vector representing the sprite's movement direction
        self.speed = 5 # This will be used to define the speed movement in pixels/frame
    
        # IMPORTANT: This defines wich group of sprites is going to collide against the player, and will be passed as an argument at __init__
        self.obstacle_sprites = obstacle_sprites

    # Defining how our inputs afect the characters movement vector
    def input(self):
        keys = pg.key.get_pressed()

        # First for up and down movement
        if keys[pg.K_UP]:
            self.direction.y = -1
        elif keys[pg.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        # Then for left and right movement
        if keys[pg.K_RIGHT]:
            self.direction.x = 1
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    # Defining how the vector and the speed interact to create movement
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize() # Here we normalize the vector, so if you go in two simultaneous directions, you don't become The Flash

        self.rect.x += self.direction.x * speed
        self.collision("x")

        self.rect.y += self.direction.y * speed
        self.collision("y")

    # Defining the collision behaviour
    def collision(self, direction):
        if direction == "x":
            for obstacle in self.obstacle_sprites:
                if obstacle.rect.colliderect(self.rect):
                    if self.direction.x > 0: # The player is moving right, so we have a collision to the right
                        self.rect.right = obstacle.rect.left
                    if self.direction.x < 0: # The player is moving left, so we have a collision to the left
                        self.rect.left = obstacle.rect.right

        if direction == "y":
            for obstacle in self.obstacle_sprites:
                if obstacle.rect.colliderect(self.rect):
                    if self.direction.y > 0: # The player is moving down, so we have a collision at the bottom
                        self.rect.bottom = obstacle.rect.top
                    if self.direction.y < 0: # The player is moving up, so we have a collision to the top
                        self.rect.top = obstacle.rect.bottom

    def update(self):
        self.input()
        self.move(self.speed)