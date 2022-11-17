import pygame as pg

class Entity(pg.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pg.math.Vector2() # This is a vector representing the sprite's movement direction

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