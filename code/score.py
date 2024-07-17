import pygame
from settings import WINDOW_WIDTH, PADDING


class Score:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.display_surface = pygame.display.get_surface()
        self.lines = 0
        self.score = 0
        self.level = 1

    def run(self):
        score_surface = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        lines_surface = self.font.render(f'Lines: {self.lines}', True, (255, 255, 255))
        level_surface = self.font.render(f'Level: {self.level}', True, (255, 255, 255))

        self.display_surface.blit(score_surface, (WINDOW_WIDTH - score_surface.get_width() - PADDING, PADDING))
        self.display_surface.blit(lines_surface, (WINDOW_WIDTH - lines_surface.get_width() - PADDING, PADDING + 40))
        self.display_surface.blit(level_surface, (WINDOW_WIDTH - level_surface.get_width() - PADDING, PADDING + 80))
