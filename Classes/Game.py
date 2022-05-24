import math
import sys, pygame
from Classes.MainMenu import MainMenu
from Classes.Level import Level
from Const.ScreenConst import WIDTH,HEIGHT,levels
from Classes.Button import Button
from Classes.Sound import Sound
from Classes.Box import Box

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
        #current_level = 0
        #self.level= Level(levels[current_level]["init_pos"],levels[current_level]["background"],levels[current_level]["border"],levels[current_level]["hole"], self.WIDTH, self.HEIGHT)
        # initiation son arrière-plan
        self.music = Sound()

   

    def run(self):
        # boucle principale du jeu
        while True:

            self.main_menu.menu_run()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            

            #update screen
            pygame.display.update()
            self.clock.tick(self.FPS)
