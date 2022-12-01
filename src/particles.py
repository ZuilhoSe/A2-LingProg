import pygame as pg
from support import import_folder
from random import choice

class AnimationPlayer:
    def __init__(self):
        self.frames = {
            # player attack
            # "attack": import_folder('../graphics/particles/attack', rescale=1),

            # magic
            # 'flame': import_folder('../graphics/particles/flame/frames', rescale=1),
            # 'aura': import_folder('../graphics/particles/aura', rescale=1),
            # 'heal': import_folder('../graphics/particles/heal/frames', rescale=1),
            
            # monster attacks 
            # 'claw': import_folder('../graphics/particles/claw', rescale=1),
            'slash': import_folder('../graphics/particles/slash', rescale=1),
            'fire': import_folder('../graphics/particles/fire', rescale=2),
            # 'sparkle': import_folder('../graphics/particles/sparkle', rescale=1),
            # 'leaf_attack': import_folder('../graphics/particles/leaf_attack', rescale=1),
            # 'thunder': import_folder('../graphics/particles/thunder', rescale=1),
 
            # monster deaths
            'snake': import_folder('../graphics/particles/smoke', rescale=1),
            'squid': import_folder('../graphics/particles/smoke_orange', rescale=1),
            'raccoon': import_folder('../graphics/particles/smoke', rescale=1),
            'flam': import_folder('../graphics/particles/sparkle', rescale=1),
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

    def reflect_images(self, frames):
        new_frames = []
        for frame in frames:
            flipped_frame = pg.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        
        return new_frames

    def create_grass_particles(self, pos, groups):
        animation_frames = choice(self.frames["leaf"])
        ParticleEffect(pos, animation_frames, groups)

    def create_default_particles(self, particle_type, pos, groups):
        animation_frames = self.frames[particle_type]
        ParticleEffect(pos, animation_frames, groups)

class ParticleEffect(pg.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()