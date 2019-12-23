HEIGHT = 720
WIDTH = 1080
BIT_SPEED = 5
screen = "lul"
clock = "w o w"
ENEMY_AMOUNT = 30
FRIENDLY_AMOUNT = ENEMY_AMOUNT - 10
HARDMODE_ON = False
GAMEMODE = "elimination"
# need these as placeholders to stop Pycharm from erroring

# Game State Variables
QUIT = False
GAMEMODES = ("capture", "elimination", "2 player duel")
TEAMS = ("enemy", "friendly")

# Menu Variables
INTRO_FPS = 360
MENU_FPS = 90
FB_AMOUNT = 101
FB_SPEED = 5
MIN_SPEED_PERCENT = 75
MAX_SPEED_PERCENT = 200
FB_WAIT = 2000    # time delay in ms between falling blocks

# Game Variables
LIST_OF_CLASSES = ("Grunt", "Shotgunner", "Autogunner", "Tank", "Terror", "Boss")   # didn't have time to implement terror
FPS = 60
SCREENSHAKE_SIZE = 8

PLAYER_SIZE = 20
PLAYER_SPEED = 3 * FPS / 60
PLAYER_FIRE_DELAY = 100
PLAYER_HP = 4
PLAYER_SHOTGUN_DELAY = 900
SHOTGUN_SPREAD = .2    # in radians, must be > .01
SHOTGUN_AMOUNT = 12

UNIT_SPEED = 2 * FPS / 60
UNIT_SIZE = 20 * HEIGHT / 720

UNIT_FIRE_DELAY = 1000
BIT_SIZE = 5
BIT_THICKNESS = 2

SHIELD_SIZE = 30
SHIELD_THICKNESS = 8

WALL_SIZE = WIDTH * 1.25
WALL_THICKNESS = 10

BARRICADE_AMOUNT = 15
BARRICADE_SIZE = 200
BARRICADE_THICKNESS = 15
BARRICADE_STEP = BARRICADE_SIZE

# Play Area Vars
LEFT = -WALL_SIZE / 2 + WIDTH / 2
RIGHT = WALL_SIZE / 2 + WIDTH / 2
BOTTOM = WALL_SIZE / 2
TOP = -WALL_SIZE / 2

PLAY_AREA_LEFT = LEFT + WALL_THICKNESS
PLAY_AREA_RIGHT = RIGHT
PLAY_AREA_TOP = TOP + WALL_THICKNESS
PLAY_AREA_BOTTOM = BOTTOM - WALL_THICKNESS

# Two Player Vars
AIM_SIZE = 5
PLAYER_FIRE_DELAY_2P = 400
BIT_SIZE_2P = 4

# Game Over Variables
GO_AMOUNT = 100
GO_WAIT = 250
GO_SPEED = 5

# RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
DGRAY = (112, 128, 144)
DDGRAY = (105, 105, 105)
RED = (255, 0, 0)
LGREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
PURPLE = (148, 0, 211)
LPURPLE = (255, 0, 255)
ORANGE = (255, 140, 0)
