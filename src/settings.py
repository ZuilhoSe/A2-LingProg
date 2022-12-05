# game setup
STANDARD_WIDTH=1280
STANDARD_HEIGTH=720
STANDARD_FONT_SIZE=100
WIDTH    = 1280	
HEIGTH   = 720
MENU_FONT_SIZE=STANDARD_FONT_SIZE*(int(WIDTH/STANDARD_WIDTH))
FPS      = 60
TILESIZE = 64


######################################################
###########Not sure if I will keep this###############
#ui 
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/HUD/Font/NormalFont.ttf'
UI_FONT_SIZE = 18
# gererall colors
WATER_COLOR='#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR ='#EEEEEE'
# ui colors
HEALTH_COLOR ='red'
ENERGY_COLOR ="blue"
UI_BORDER_COLOR_ACTIVE = 'gold'
######################################################

#hearts
FULL_HEART='../graphics/HUD/fullheart.png'
HALF_HEART='../graphics/HUD/half_heart.png'
EMPTY_HEART='../graphics/HUD/empty_heart.png'
QUARTER_HEART='../graphics/HUD/quarter_heart.png'
QUARTER_3_HEART='../graphics/HUD/quarter_3_heart.png'


WORLD_MAP = [
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',' ','',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ','e',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' '],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' '],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' '],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','p','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]

# Weapon Data:
weapon_data = {
    "Stick": {"cooldown": 1000, "damage": 1, "graphic": "../graphics/weapons/Stick/Sprite.png"},
    "Katana": {"cooldown": 800, "damage": 2, "graphic": "../graphics/weapons/Katana/Sprite.png"}
}

# Magic Data:
magic_data = {
    "fireball": {"strength": 3, "cost": 2, "cooldown": 1200, "graphic": "../graphics/particles/fireball/fire.png"},
    "heal": {"strength": 2, "cost": 1, "cooldown": 800, "graphic": "../graphics/particles/fireball/fire.png"}
}

monsters_data = {
    'squid': {'health': 3,'exp':100,'damage':1,'attack_type': 'slash', 'attack_sound':'../audio/monster_hit.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'flam': {'health': 2,'exp':100,'damage':1,'attack_type': 'fire', 'attack_sound':'../audio/flame_attack.wav', 'speed': 5, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 4,'exp':100,'damage':1,'attack_type': 'slash', 'attack_sound':'../audio/monster_hit.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'snake': {'health': 2,'exp':100,'damage':1,'attack_type': 'slash', 'attack_sound':'../audio/monster_hit.wav', 'speed': 2, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'beast': {'health': 5,'exp':100,'damage':1,'attack_type': 'slash', 'attack_sound':'../audio/monster_hit.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'blue_octopus': {'health': 3,'exp':100,'damage':1,'attack_type': 'slash', 'attack_sound':'../audio/monster_hit.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'skull': {'health': 3,'exp':100,'damage':1,'attack_type': 'fire', 'attack_sound':'../audio/flame_attack.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'blue_skull': {'health': 3,'exp':100,'damage':1,'attack_type': 'fire', 'attack_sound':'../audio/flame_attack.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'giant_flam': {'health': 10,'exp':100,'damage':1,'attack_type': 'fire', 'attack_sound':'../audio/flame_attack.wav', 'speed': 2, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360,'magic_radius':250,'magic_type':'fireball','magic_damage':1, 'magic_speed': 6},
}