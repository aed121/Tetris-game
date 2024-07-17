import pygame
import os


FONT_PATH = pygame.font.get_default_font()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GAME_WIDTH = 300
GAME_HEIGHT = 570
CELL_SIZE = 30
PADDING = 20
LINE_COLOR = (255, 255, 255)
PURPLE_D = (75, 0, 130)
COLUMNS = GAME_WIDTH // CELL_SIZE
ROWS = GAME_HEIGHT // CELL_SIZE
TETROMINOS = {
    'I': {'shape': [(0, 0), (1, 0), (2, 0), (3, 0)], 'color': (0, 255, 255), 'color_f': (0, 128, 128)},
    'J': {'shape': [(0, 0), (1, 0), (2, 0), (2, 1)], 'color': (0, 0, 255), 'color_f': (0, 0, 128)},
    'L': {'shape': [(0, 0), (1, 0), (2, 0), (0, 1)], 'color': (255, 165, 0), 'color_f': (128, 83, 0)},
    'O': {'shape': [(0, 0), (1, 0), (0, 1), (1, 1)], 'color': (255, 255, 0), 'color_f': (128, 128, 0)},
    'S': {'shape': [(1, 0), (2, 0), (0, 1), (1, 1)], 'color': (0, 255, 0), 'color_f': (0, 128, 0)},
    'T': {'shape': [(1, 0), (0, 1), (1, 1), (2, 1)], 'color': (128, 0, 128), 'color_f': (64, 0, 64)},
    'Z': {'shape': [(0, 0), (1, 0), (1, 1), (2, 1)], 'color': (255, 0, 0), 'color_f': (128, 0, 0)}
}
UPDATE_START_SPEED = 1000
MOVE_WAIT_TIME = 200
ROTATE_WAIT_TIME = 200
SCORE_DATA = {1: 100, 2: 300, 3: 500, 4: 800}
BLOCK_OFFSET = pygame.Vector2(3, -2)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROTATE_SOUND_PATH = os.path.join(BASE_DIR, 'sound', 'rotate.wav')
LOSE_SOUND_PATH = os.path.join(BASE_DIR, 'sound', 'lose.wav')


print(f"ROTATE_SOUND_PATH: {ROTATE_SOUND_PATH}")
print(f"LOSE_SOUND_PATH: {LOSE_SOUND_PATH}")


if not os.path.exists(ROTATE_SOUND_PATH):
    print(f"Error: {ROTATE_SOUND_PATH} does not exist.")
else:
    print(f"Success: {ROTATE_SOUND_PATH} exists.")

if not os.path.exists(LOSE_SOUND_PATH):
    print(f"Error: {LOSE_SOUND_PATH} does not exist.")
else:
    print(f"Success: {LOSE_SOUND_PATH} exists.")


class Tetromino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.color_f = tuple(c // 2 for c in color)


class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color, color_f):
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(2, 2))
        pygame.draw.rect(self.image, color_f, self.rect, 2, 2)

        self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
        self.rect = self.image.get_rect(topleft=self.pos * CELL_SIZE)

    def rotate(self, pivot_pos):
        return pivot_pos + (self.pos - pivot_pos).rotate(90)

    def horizontal_collide(self, x, field_data):
        if not 0 <= x < COLUMNS:
            return True
        if field_data[int(self.pos.y)][x]:
            return True

    def vertical_collide(self, y, field_data):
        if y >= ROWS:
            return True
        if y >= 0 and field_data[y][int(self.pos.x)]:
            return True

    def update(self):
        self.rect.topleft = self.pos * CELL_SIZE
