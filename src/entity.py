import pygame as pg
from math import sin

class Entity(pg.sprite.Sprite):
    """This class carries the methods and properties that are common to all entities spawned in the game. It inherits from pygame.sprite.Sprite class.
    """

    def __init__(self, groups):
        """The Entity is an abstract class, and will never be called in the game. The init method has some important properties for entitie's movements.

        :param groups: List of tile groups the Entity will belong
        :type groups: list
        """

        super().__init__(groups)

        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pg.math.Vector2() # This is a vector representing the sprite's movement direction

    def move(self, speed):
        """This defines how changes in the movement vector combines with entities speed to create movement.

        :param speed: Entity's speed of movement.
        :type speed: int
        """

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize() # Here we normalize the vector, so if you go in two simultaneous directions, you don't become The Flash

        self.hitbox.x += self.direction.x * speed
        self.collision("x")

        self.hitbox.y += self.direction.y * speed
        self.collision("y")

        self.rect.center = self.hitbox.center   

    def collision(self, direction):
        """The collision method defines the entitie's behaviour when they touch each other.

        :param direction: "x" if the collision is happening in the horizontal. "y" if a collision is happening in the vertical.
        :type direction: str
        """

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

    def variable_value(self):
        """This method works simply to return a variable value as time passes.

        :return: Varies between returning 0 or 255 as time passes.
        :rtype: int
        """

        value = sin(pg.time.get_ticks())
        if value >= 0:
            return 255
        else:
            return 0