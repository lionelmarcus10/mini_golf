import sys

import pygame
from Classes.Button import Button
from Classes.Sound import Sound

class MainMenu:
    def __init__(self):
        #screen dimensions
        self.WIDTH=800
        self.HEIGHT = 600

        # Texte
        self.game_name = "Golf A109"
        self.menu_text = "Bienvenu"

        # options

        self.choice1 = "SOLO"
        self.choice2 = "MULTIJOUER"

        # IMAGES

        self.background = pygame.image.load("Assets/Start_menu_back.png")
        self.logo = pygame.image.load("Assets/LOGO.png")
        self.background2 = pygame.image.load("Assets/Background2.jpg")
        self.solo = pygame.image.load("Assets/Solo.png")
        self.multijoueur = pygame.image.load("Assets/Multijoueur.png")

        # FONT

        self.font_export = pygame.font.Font("Fonts/Melinda Rosalie.ttf",90)
        self.game_welcome = self.font_export.render(self.menu_text, True, (255, 255, 255))

        # building of UI
        self.current_menu = 1
        self.menu_screen = pygame.display.get_surface()

        # button start/exit
        self.exit_image = pygame.image.load('Assets/Bouton_exit.png').convert_alpha()
        self.start_image = pygame.image.load('Assets/Bouton_start.png').convert_alpha()


    def menu2(self):
        self.menu_screen.blit(pygame.transform.scale(self.background2, (int(800), int(600))), (0, 0))
        self.menu_screen.blit(self.logo, (self.WIDTH / 2.2, self.HEIGHT / 10))
        self.menu_screen.blit(self.game_welcome, (self.WIDTH / 2.5, self.HEIGHT / 4))
        self.solo_button = Button(300,350,self.solo,1)
        self.multijoueur_button = Button(450, 350, self.multijoueur, 1)
        self.exit_button = Button(720, 530, self.exit_image, 1)

        if self.exit_button.draw() == True:
            self.current_menu-=1
            self.menu_run()

        if self.solo_button.draw() == True:
            print("soloooooo")
        elif self.multijoueur_button.draw() == True:
            print("multijoueur")

    def menu1(self):
        self.menu_screen.blit(self.background, (0, 0))
        self.menu_screen.blit(self.logo, (self.WIDTH / 2.2, self.HEIGHT / 10))
        self.menu_screen.blit(self.game_welcome, (self.WIDTH / 2.5, self.HEIGHT / 4))
        self.start_button = Button(370, 420, self.start_image, 1)
        self.exit_button = Button(700, 530, self.exit_image, 1)
        if self.start_button.draw() == True:
            self.current_menu+=1
            self.menu_run()

        if self.exit_button.draw() == True:
            pygame.quit()
            sys.exit()

    def menu_run(self):
        if self.current_menu==1:
            self.menu1()
        elif self.current_menu ==2:
            self.menu2()


