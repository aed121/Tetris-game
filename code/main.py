from settings import *
from sys import exit

from game import Game
from score import Score
from preview import Preview
from menu import Menu

from random import choice

class Main:
    def __init__(self):

        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tetris')


        self.next_shapes = [choice(list(TETROMINOS.keys())) for shape in range(3)]


        self.game = Game(self.get_next_shape, self.update_score)
        self.score = Score()
        self.preview = Preview()
        self.menu = Menu()


        self.state = 'menu'

    def update_score(self, lines, score, level):
        self.score.lines = lines
        self.score.score = score
        self.score.level = level

    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))
        return next_shape

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif self.state == 'menu':
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.menu.navigate_menu(-1)
                        elif event.key == pygame.K_DOWN:
                            self.menu.navigate_menu(1)
                        elif event.key == pygame.K_RETURN:
                            option = self.menu.select_option()
                            if option == 'Start Game':
                                self.state = 'game'
                            elif option == 'High Score':
                                print("Display high score")
                            elif option == 'Exit':
                                pygame.quit()
                                exit()

            if self.state == 'menu':
                self.menu.display_menu()
            elif self.state == 'game':
                self.display_surface.fill(PURPLE_D)

                self.game.run()
                self.score.run()
                self.preview.run(self.next_shapes)

            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    main = Main()
    main.run()
