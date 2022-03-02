import sys, pygame
from Classes.MainMenu import MainMenu
from Classes.Level import Level
from Const.ScreenConst import WIDTH,HEIGHT,levels
from Classes.Button import Button


class Game:
    def __init__(self):

        # initiation de pygame
        pygame.init()

        self.window_name = "Golf A109"
        pygame.display.set_caption(self.window_name)

        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.FPS = 60
        self.clock = pygame.time.Clock()

        #menu principal
        self.main_menu = MainMenu()
        #Level 1
        current_level = 0
        #self.level= Level(levels[current_level]["init_pos"],levels[current_level]["background"],levels[current_level]["border"],levels[current_level]["hole"], self.WIDTH, self.HEIGHT)



    def run(self):
        speed = (10, 10)
        move = {
            pygame.K_LEFT: (-1*speed[0], 0),
            pygame.K_RIGHT: (1*speed[0], 0),
            pygame.K_UP: (0, -1*speed[1]),
            pygame.K_DOWN: (0, 1*speed[1])
        }
        while True:

            keys = pygame.key.get_pressed()
            for key in move:
                if keys[key]:
                    self.level.update_pos(*move[key])


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.main_menu.menu_run()

            #update screen
            pygame.display.update()
            self.clock.tick(self.FPS)
