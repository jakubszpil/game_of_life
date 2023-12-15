# CONSTANTS
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
COLUMNS, ROWS = 40, 30
CELL_WIDTH = SCREEN_WIDTH // COLUMNS
CELL_HEIGHT = SCREEN_HEIGHT // ROWS

# COLORS
COLORS_WHITE = (255, 255, 255)
COLORS_BLACK = (0, 0, 0)
COLORS_GRAY = (128, 128, 128)
COLORS_GREEN = (0, 255, 0)


# BTN CONSTANTS
BTN_WIDTH, BTN_HEIGHT = 200, 50
BTN_X, BTN_Y = (
    SCREEN_WIDTH - BTN_WIDTH) // 2, SCREEN_HEIGHT - BTN_HEIGHT - 10

# Dimensions of the pause/resume button
PAUSE_BTN_X, PAUSE_BTN_Y = 10, SCREEN_HEIGHT - BTN_HEIGHT - 10

# Dimensions of save and load buttons
SAVE_LOAD_BTN_WIDTH, SAVE_LOAD_BTN_HEIGHT = 150, 40
SAVE_BTN_X, SAVE_BTN_Y = 10, 10
LOAD_BTN_X, LOAD_BTN_Y = 10, 70

# "Next Generation" button dimensions
NEXT_GEN_BTN_WIDTH, NEXT_GEN_BTN_HEIGHT = 200, 50