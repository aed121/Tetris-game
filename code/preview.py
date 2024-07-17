import pygame
from settings import PADDING, CELL_SIZE, COLUMNS, TETROMINOS

class Preview:
    def __init__(self):
        self.surface = pygame.Surface((4 * CELL_SIZE, 12 * CELL_SIZE))
        self.rect = self.surface.get_rect(topleft=(2 * PADDING + COLUMNS * CELL_SIZE, PADDING))

    def run(self, next_shapes):
        self.surface.fill((0, 0, 0))
        for index, shape_key in enumerate(next_shapes):
            shape = TETROMINOS[shape_key]
            for pos in shape['shape']:
                pygame.draw.rect(
                    self.surface, shape['color'],
                    pygame.Rect(pos[0] * CELL_SIZE, pos[1] * CELL_SIZE + index * 4 * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )
        display_surface = pygame.display.get_surface()
        display_surface.blit(self.surface, self.rect)
