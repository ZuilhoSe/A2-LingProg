from multiprocessing.dummy import current_process
import pygame
import settings
from entity import Entity
import support

class Enemy(Entity):
    """Enemy class responsible for the enemy's behaviour

    :param Entity: Enemy class inherits from Entity class
    :type Entity: Entity
    """    
    def __init__(self, monster_name: str, pos: tuple[int], groups, obstacle_sprites: pygame.sprite.Group()):
        """
        :param monster_name: name of the enemy so that it's attributes can be searched
        :type monster_name: str
        :param pos: initial position of the enemy, measured in pixels
        :type pos: tuple[int]
        :param groups: _description_
        :type groups: _type_
        :param obstacle_sprites: _description_
        :type obstacle_sprites: pygame.sprite.Group
        """   
             
        #general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'
        
        #graphics setup
        self.status = 'idle'
        self.import_graphics(monster_name)
        self.image= self.animations[self.status][self.frame_index]
        
        # movement
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.obstacle_sprites = obstacle_sprites
        
        # stats
        self.monster_name = monster_name
        monster_info = settings.monsters_data[self.monster_name]
        self.health = monster_info['health']
        self.exp = monster_info['exp']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.resistance = monster_info['resistance']
        self.attack_radius = monster_info['attack_radius']
        self.notice_radius = monster_info['notice_radius']
        self.attack_type = monster_info['attack_type']
        
        #player interaction
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400
        
    def import_graphics(self, name: str):
        """Stores the animations of the enemy in a dictionay

        :param name: name of the enemy
        :type name: str
        """ 
               
        self.animations = {'idle':[],'move':[],'attack':[]}
        main_path =f'../graphics/monster/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = support.import_folder(main_path + animation)
    
    def get_player_distance_direction(self, player):
        """Gets the postion of the enemy relative to the player

        :param player: the player
        :type player: Player
        """     
        
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()
        
        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()
        return (distance, direction)
    
    def get_status(self, player):
        """Define the status of the enemy based on it's distance to the player

        :param player: the player
        :type player: Player
        """   
                
        distance = self.get_player_distance_direction(player)[0]
        
        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack':
                self.frame_index = 0
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'
            
    def actions(self,player):
        """Define what the enemy does based on it's status

        :param player: hte playable character
        :type player: Player
        """        
        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()
    
    def animate(self):
        """Draws the enemy animations
        """
                
        animation = self.animations[self.status]
        
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status == 'attack':
                self.can_attack = False
            self.frame_index = 0
            
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
        
    def cooldown(self):
        """Attack cooldown timer of the enemy
        """        
        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True
                
    def update(self):
        """Updates the enemy
        """        
        self.move(self.speed)
        self.animate()
        self.cooldown()
        
    def enemy_update(self,player):
        """updates the enemy

        :param player: the playable character
        :type player: Player
        """        
        self.get_status(player)
        self.actions(player)