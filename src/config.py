# Window and rendering settings
CELL_SIZE = 30
WALL_THICKNESS = 2
FPS = 60

# Color palette
class Colors:
    BACKGROUND = (15, 15, 25)
    WALL = (220, 220, 230)
    UNVISITED = (30, 30, 45)
    VISITED = (45, 55, 85)
    WALK_PATH = (255, 200, 50)
    CURRENT_CELL = (255, 100, 100)
    TEXT = (200, 200, 210)
    TEXT_BG = (20, 20, 30)

# Maze generation settings
MIN_MAZE_SIZE = 5
MAX_MAZE_SIZE = 50
DEFAULT_GENERATION_SPEED = 1
MAX_GENERATION_SPEED = 10
