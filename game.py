from lib.numpy_api import getCopy, getSum, getArray
from lib.json_api import JSON
from lib.pygame_api import Game, pygame
from lib.constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLUMNS, ROWS, COLORS_BLACK, COLORS_GRAY, COLORS_GREEN, COLORS_WHITE, CELL_WIDTH, CELL_HEIGHT, BTN_HEIGHT, BTN_WIDTH, BTN_X, BTN_Y, LOAD_BTN_X, LOAD_BTN_Y, NEXT_GEN_BTN_HEIGHT, NEXT_GEN_BTN_WIDTH, PAUSE_BTN_X, PAUSE_BTN_Y, SAVE_BTN_X, SAVE_BTN_Y, SAVE_LOAD_BTN_HEIGHT, SAVE_LOAD_BTN_WIDTH


# Pygame initialization
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, COLUMNS, ROWS)
game.start()


# initializing json manager
json = JSON("game_persisted_state.json")

# Function that draws the "Next Generation" button


def draw_text(text: str):
    return pygame.font.Font(None, 36).render(text, True, COLORS_BLACK)


def draw_button():
    pygame.draw.rect(game.surface, COLORS_GREEN, (BTN_X, BTN_Y,
                                                  NEXT_GEN_BTN_WIDTH, NEXT_GEN_BTN_HEIGHT))
    text = draw_text("Next Generation")
    text_rect = text.get_rect(center=(
        BTN_X + NEXT_GEN_BTN_WIDTH // 2, BTN_Y + NEXT_GEN_BTN_HEIGHT // 2))
    game.surface.blit(text, text_rect)

# A function that draws a pause/resume button


def draw_pause_button():
    pygame.draw.rect(game.surface, COLORS_GREEN, (PAUSE_BTN_X,
                     PAUSE_BTN_Y, BTN_WIDTH, BTN_HEIGHT))
    pause_text = "Pause" if not game.isPaused else "Resume"
    text = draw_text(pause_text)
    text_rect = text.get_rect(center=(
        PAUSE_BTN_X + BTN_WIDTH // 2, PAUSE_BTN_Y + BTN_HEIGHT // 2))
    game.surface.blit(text, text_rect)

# Function that draws save and load buttons


def draw_save_load_buttons():
    pygame.draw.rect(game.surface, COLORS_GREEN, (SAVE_BTN_X, SAVE_BTN_Y,
                                                  SAVE_LOAD_BTN_WIDTH, SAVE_LOAD_BTN_HEIGHT))
    game.surface.blit(draw_text("Save"), (SAVE_BTN_X + 20, SAVE_BTN_Y + 10))

    pygame.draw.rect(game.surface, COLORS_GREEN, (LOAD_BTN_X, LOAD_BTN_Y,
                                                  SAVE_LOAD_BTN_WIDTH, SAVE_LOAD_BTN_HEIGHT))
    game.surface.blit(draw_text("Load"), (LOAD_BTN_X + 20, LOAD_BTN_Y + 10))

# A function that draws a mesh


def draw_grid():
    for y in range(0, SCREEN_HEIGHT, CELL_HEIGHT):
        for x in range(0, SCREEN_WIDTH, CELL_WIDTH):
            cell = pygame.Rect(x, y, CELL_WIDTH, CELL_HEIGHT)
            pygame.draw.rect(game.surface, COLORS_GRAY, cell, 1)

# Function that draws living cells


def draw_cells():
    for y in range(ROWS):
        for x in range(COLUMNS):
            if game.state[x, y] == 1:
                pygame.draw.rect(game.surface, COLORS_BLACK, (x * CELL_WIDTH,
                                 y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

# A function that generates the next generation


def next_generation():
    updates_state = getCopy(game.state)
    for row in range(ROWS):
        for column in range(COLUMNS):
            n_neighbors = getSum(
                game.state[(column - 1):(column + 2), (row - 1):(row + 2)]) - game.state[column, row]

            if game.state[column, row] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                updates_state[column, row] = 0
            elif game.state[column, row] == 0 and n_neighbors == 3:
                updates_state[column, row] = 1

    game.state = updates_state

# Pause toggle function


def toggle_pause() -> bool:
    game.isPaused = not game.isPaused
    if game.isPaused:
        pygame.time.set_timer(timer_event, 0)
    else:
        pygame.time.set_timer(timer_event, update_interval)


# A function that saves the game state to a file


def save_game_state():
    json.write(game.state.tolist())

# A function that loads the game state from a file


def persist_game_state():
    results = json.load()
    persist_game_state = getArray(results)
    if persist_game_state.shape == (COLUMNS, ROWS):
        game.state = persist_game_state
    else:
        print("Invalid game state size.")


timer_event = pygame.USEREVENT + 1
update_interval = 100
pygame.time.set_timer(timer_event, update_interval)

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == timer_event and not game.isPaused:
            next_generation()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if BTN_X <= mouse_x <= BTN_X + NEXT_GEN_BTN_WIDTH and BTN_Y <= mouse_y <= BTN_Y + NEXT_GEN_BTN_HEIGHT:
                next_generation()
            elif PAUSE_BTN_X <= mouse_x <= PAUSE_BTN_X + BTN_WIDTH and PAUSE_BTN_Y <= mouse_y <= PAUSE_BTN_Y + BTN_HEIGHT:
                toggle_pause()
            elif SAVE_BTN_X <= mouse_x <= SAVE_BTN_X + SAVE_LOAD_BTN_WIDTH and SAVE_BTN_Y <= mouse_y <= SAVE_BTN_Y + SAVE_LOAD_BTN_HEIGHT:
                save_game_state()
            elif LOAD_BTN_X <= mouse_x <= LOAD_BTN_X + SAVE_LOAD_BTN_WIDTH and LOAD_BTN_Y <= mouse_y <= LOAD_BTN_Y + SAVE_LOAD_BTN_HEIGHT:
                persist_game_state()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save_game_state()
            elif event.key == pygame.K_l:
                persist_game_state()

    # Screen update
    game.surface.fill(COLORS_WHITE)
    draw_grid()
    draw_cells()
    draw_button()
    draw_pause_button()
    draw_save_load_buttons()
    pygame.display.flip()

# Close Pygame when the program ends
game.quit()
