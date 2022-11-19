# game setup
WIDTH    = 1280	
HEIGTH   = 720
FPS      = 60
TILESIZE = 64


"""Not sure if all this variables will stay till the end of project"""

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
# ui hearts
# FULL_HEART = pg.image.load('../graphics/HUD/fullheart.png').convert_alpha()
# HALF_HEART = pg.image.load('../graphics/HUD/half_heart.png').convert_alpha()
# EMPTY_HEART = pg.image.load('../graphics/HUD/empty_heart.png').convert_alpha()
# QUARTER_HEART = pg.image.load('../graphics/HUD/quarter_heart.png').convert_alpha()
# QUARTER_3_HEART = pg.image.load('../graphics/HUD/quarter_3_heart.png').convert_alpha()


FULL_HEART='../graphics/HUD/fullheart.png'
HALF_HEART='../graphics/HUD/half_heart.png'
EMPTY_HEART='../graphics/HUD/empty_heart.png'
QUARTER_HEART='../graphics/HUD/quarter_heart.png'
QUARTER_3_HEART='../graphics/HUD/quarter_3_heart.png'
EMPTY_MANA='../graphics/HUD/empty_mana.png'
FULL_MANA='../graphics/HUD/full_mana.png'

WORLD_MAP = [
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
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
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]

# Weapon Data:
weapon_data = {
    "Stick": {"cooldown": 100, "damage": 8, "graphic": "..graphics/weapons/Stick/SpriteInHand.png"},
    "Katana": {"cooldown": 80, "damage": 15, "graphic": "..graphics/weapons/Katana/SpriteInHand.png"}
}