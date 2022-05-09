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
        self.box = Box(100, 100, 140, 32)
        #menu principal
        self.main_menu = MainMenu()
        #Level 1
        current_level = 0
        #self.level= Level(levels[current_level]["init_pos"],levels[current_level]["background"],levels[current_level]["border"],levels[current_level]["hole"], self.WIDTH, self.HEIGHT)
        # initiation son arrière-plan
        self.music = Sound()

    def entrer_nom(self, screen):
        # permet d'entrer le nom du joueur dans le classement
        while not self.box.nom_saisi:
            for event in pygame.event.get():
                self.box.gestion_text(event)
                pygame.display.flip()
            self.level.draw_background()
            self.box.maj()
            self.box.ecrire(screen)
            pygame.display.flip()
        self.level.Score.nom = self.box.text
        self.level.besoin_nom = False
        self.level.update_player()

    def run(self):
        speed = (10, 10)
        move = {
            pygame.K_LEFT: (-1*speed[0], 0),
            pygame.K_RIGHT: (1*speed[0], 0),
            pygame.K_UP: (0, -1*speed[1]),
            pygame.K_DOWN: (0, 1*speed[1])
        }
        # Saisie du pseudo de l'utilisateur
        #self.entrer_nom(self.screen)
        while True:

            keys = pygame.key.get_pressed()
            for key in move:
                if keys[key]:
                    self.level.score+= 0.5
                    self.level.update_pos(*move[key])

            self.main_menu.menu3()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            

            #update screen
            pygame.display.update()
            self.clock.tick(self.FPS)
