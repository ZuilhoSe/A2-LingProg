import pygame as pg
from support import import_folder
from random import choice

class AnimationPlayer:
    def __init__(self):
        self.frames = {
            # magic
            'flame': import_folder('../graphics/particles/flame/frames', rescale=False),
            'aura': import_folder('../graphics/particles/aura', rescale=False),
            'heal': import_folder('../graphics/particles/heal/frames', rescale=False),
            
            # attacks 
            'claw': import_folder('../graphics/particles/claw', rescale=False),
            'slash': import_folder('../graphics/particles/slash', rescale=False),
            'sparkle': import_folder('../graphics/particles/sparkle', rescale=False),
            'leaf_attack': import_folder('../graphics/particles/leaf_attack', rescale=False),
            'thunder': import_folder('../graphics/particles/thunder', rescale=False),
 
            # monster deaths
            'squid': import_folder('../graphics/particles/smoke_orange', rescale=False),
            'raccoon': import_folder('../graphics/particles/raccoon', rescale=False),
            'spirit': import_folder('../graphics/particles/nova', rescale=False),
            'bamboo': import_folder('../graphics/particles/bamboo', rescale=False),
            
            # leafs 
            'leaf': (
                import_folder('../graphics/particles/leaf1', rescale=False),
                import_folder('../graphics/particles/leaf2', rescale=False),
                import_folder('../graphics/particles/leaf3', rescale=False),
                import_folder('../graphics/particles/leaf4', rescale=False),
                import_folder('../graphics/particles/leaf5', rescale=False),
                import_folder('../graphics/particles/leaf6', rescale=False),
                self.reflect_images(import_folder('../graphics/particles/leaf1', rescale=False)),
                self.reflect_images(import_folder('../graphics/particles/leaf2', rescale=False)),
                self.reflect_images(import_folder('../graphics/particles/leaf3', rescale=False)),
                self.reflect_images(import_folder('../graphics/particles/leaf4', rescale=False)),
                self.reflect_images(import_folder('../graphics/particles/leaf5', rescale=False)),
                self.reflect_images(import_folder('../graphics/particles/leaf6', rescale=False))
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