import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

class Menu:
    def __init__(self):
        self.options = ['Start Game', 'High Score', 'Exit']
        self.selected_index = 0
        self.font = pygame.font.Font(None, 40)
        self.display_surface = pygame.display.get_surface()

    def navigate_menu(self, direction):
        self.selected_index = (self.selected_index + direction) % len(self.options)

    def select_option(self):
        return self.options[self.selected_index]

    def display_menu(self):
        self.display_surface.fill((0, 0, 0))
        for index, option in enumerate(self.options):
            color = (255, 255, 255) if index == self.selected_index else (100, 100, 100)
            text_surface = self.font.render(option, True, color)
            text_rect = text_surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + index * 50))
            self.display_surface.blit(text_surface, text_rect)
