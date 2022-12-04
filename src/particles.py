"""The particles module has most of the important classes and methods to create and animate particles."""

import pygame as pg
from support import import_folder
from random import choice

class AnimationPlayer:
    """ This class is the player that calls the ParticleEffect class everytime it is triggered through one of it's 'create' methods.

    The class AnimationPlayer is created this way so it can be created only once and called inside the Level class. 
    Since it loads all the particles at once and stores them inside itself, this class prevent the game from reloading every single
    particle everytime it needs them, wich would unnecessarily use too much memory power.    
    """

    def __init__(self):
        """This class do not need any specification to be created, since it is unique and is only called once. The init method simply loads all the used particles.
        """

        self.frames = {
            # player attack
            "attack_x": import_folder('../graphics/particles/attack_x', rescale=2),
            "flip_attack_x": self.reflect_images(import_folder('../graphics/particles/attack_x', rescale=2)),
            "attack_y": self.reflect_images(import_folder('../graphics/particles/attack_y', rescale=2)),
            "flip_attack_y": self.reflect_images(import_folder('../graphics/particles/attack_y', rescale=2), y=True),

            # magic
            'fireball_die': import_folder('../graphics/particles/nova', rescale=0.5),
            'heal': import_folder('../graphics/particles/heal/frames', rescale=1),
            # 'aura': import_folder('../graphics/particles/aura', rescale=1),
            
            # monster attacks 
            # 'claw': import_folder('../graphics/particles/claw', rescale=1),
            'slash': import_folder('../graphics/particles/slash', rescale=1),
            'fire': import_folder('../graphics/particles/fire', rescale=2),
            'nova': import_folder('../graphics/particles/nova', rescale=0.5),
            # 'sparkle': import_folder('../graphics/particles/sparkle', rescale=1),
            # 'leaf_attack': import_folder('../graphics/particles/leaf_attack', rescale=1),
            # 'thunder': import_folder('../graphics/particles/thunder', rescale=1),
 
            # monster deaths
            'snake': import_folder('../graphics/particles/smoke', rescale=1),
            'squid': import_folder('../graphics/particles/smoke_orange', rescale=1),
            'raccoon': import_folder('../graphics/particles/smoke', rescale=1),
            'flam': import_folder('../graphics/particles/sparkle', rescale=1),
            'giant_flam': import_folder('../graphics/particles/sparkle', rescale=4),
            # 'bamboo': import_folder('../graphics/particles/bamboo', rescale=1),
            
            # leafs 
            'leaf': (
                import_folder('../graphics/particles/leaf1', rescale=1),
                import_folder('../graphics/particles/leaf2', rescale=1),
                import_folder('../graphics/particles/leaf3', rescale=1),
                import_folder('../graphics/particles/leaf4', rescale=1),
                import_folder('../graphics/particles/leaf5', rescale=1),
                import_folder('../graphics/particles/leaf6', rescale=1),
                self.reflect_images(import_folder('../graphics/particles/leaf1', rescale=1)),
                self.reflect_images(import_folder('../graphics/particles/leaf2', rescale=1)),
                self.reflect_images(import_folder('../graphics/particles/leaf3', rescale=1)),
                self.reflect_images(import_folder('../graphics/particles/leaf4', rescale=1)),
                self.reflect_images(import_folder('../graphics/particles/leaf5', rescale=1)),
                self.reflect_images(import_folder('../graphics/particles/leaf6', rescale=1))
                )
            }

    def reflect_images(self, frames, x = True, y = False):
        """This extra method flips the frames so we can easily manipulate animations without editting them outside the program.

        :param frames: List with each frame to be flipped.
        :type frames: list
        :param x: Flips the frames in the horizontal, defaults to True
        :type x: bool, optional
        :param y: Flips the frames in the vertical, defaults to False
        :type y: bool, optional
        :return: List with all the frames flipped.
        :rtype: list
        """

        new_frames = []
        for frame in frames:
            flipped_frame = pg.transform.flip(frame, x, y)
            new_frames.append(flipped_frame)
        
        return new_frames

    def create_grass_particles(self, pos, groups):
        """ Generates random grass particles whenever its called.

        :param pos: Position where the particles will be created
        :type pos: tuple
        :param groups: Sprite groups to wich the particles belong 
        :type groups: list
        """

        animation_frames = choice(self.frames["leaf"])
        ParticleEffect(pos, animation_frames, groups)

    def create_default_particles(self, particle_type, pos, groups):
        """ Triggers a particle animation through it's name.

        :param particle_type: The name of the particle's animation as specified in self.frames
        :type particle_type: str
        :param pos: Position where the particles will be created
        :type pos: tuple
        :param groups: Sprite groups to wich the particles belong
        :type groups: list
        """

        animation_frames = self.frames[particle_type]
        ParticleEffect(pos, animation_frames, groups)

class ParticleEffect(pg.sprite.Sprite):
    """ This class creates an animated particle sprite whenever it's called. It inherits from pygame.sprite.Sprite class.
    """

    def __init__(self, pos, animation_frames, groups):
        """Creates a temporary sprite that changes it's image through a list until the list is over, giving the impression of an animation.

        :param pos: Position where the animation will be shown
        :type pos: tuple
        :param animation_frames: List of frames that will be shown during the animation
        :type animation_frames: list
        :param groups: Sprite groups to wich the particles belong
        :type groups: list
        """

        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        """Uses the animation_speed attribute to gradually increase the frame_index, wich is used to iterate over the frames list. Once the list is over, the sprite is killed.
        """

        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        """This method sets what will be called everytime the game completes a main loop. Basically, it says what will be "updated" in each frame. 
        """

        self.animate()