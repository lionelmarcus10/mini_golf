import sys
from Classes.Level import Level
from Const.ScreenConst import levels
import pygame
from Classes.Button import Button
from Classes.Sound import Sound
from Classes.Box import Box

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
        self.background3 = pygame.image.load("Assets/golf_2.png")
        self.solo = pygame.image.load("Assets/Solo.png")
        self.multijoueur = pygame.image.load("Assets/Multijoueur.png")
        self.Logo1 = pygame.image.load("Assets/LogoLevel1.png")
        self.Logo2 = pygame.image.load("Assets/LogoLevel2.png")
        self.Logo3 = pygame.image.load("Assets/LogoLevel3.png")

        # FONT

        self.font_export = pygame.font.Font("Fonts/Melinda Rosalie.ttf",90)
        self.game_welcome = self.font_export.render(self.menu_text, True, (255, 255, 255))

        # building of UI
        self.current_menu = 1
        self.menu_screen = pygame.display.get_surface()

        # button start/exit
        self.exit_image = pygame.image.load('Assets/Bouton_exit.png').convert_alpha()
        self.start_image = pygame.image.load('Assets/Bouton_start.png').convert_alpha()
     # differents menu   

    def menu2(self):
        self.menu_screen.blit(pygame.transform.scale(self.background2, (int(800), int(600))), (0, 0))
        self.menu_screen.blit(self.logo, (self.WIDTH / 2.2, self.HEIGHT / 10))
        self.menu_screen.blit(self.game_welcome, (self.WIDTH / 2.5, self.HEIGHT / 4))
        self.solo_button = Button(300,350,self.solo,1)
        self.multijoueur_button = Button(450, 350, self.multijoueur, 1)
        self.exit_button = Button(720, 530, self.exit_image, 1)

        if self.exit_button.draw() == True:
            sortie=pygame.mixer.Sound("Son/sortir.wav")
            sortie.set_volume(0.15)
            sortie.play()
            self.current_menu-=1
            self.menu_run()

        if self.solo_button.draw() == True:
            select=pygame.mixer.Sound("Son/select.wav")
            select.set_volume(0.15)
            select.play()
            self.current_menu+=1
            self.menu_run()

        elif self.multijoueur_button.draw() == True:
            select=pygame.mixer.Sound("Son/select.wav")
            select.set_volume(0.15)
            select.play()
            print("multijoueur")

    def menu1(self):
        self.menu_screen.blit(self.background, (0, 0))
        self.menu_screen.blit(self.logo, (self.WIDTH / 2.2, self.HEIGHT / 10))
        self.menu_screen.blit(self.game_welcome, (self.WIDTH / 2.5, self.HEIGHT / 4))
        self.start_button = Button(370, 420, self.start_image, 1)
        self.exit_button = Button(700, 530, self.exit_image, 1)
        if self.start_button.draw() == True:
            select=pygame.mixer.Sound("Son/select.wav")
            select.set_volume(0.15)
            select.play()
            self.current_menu+=1
            self.menu_run()

        if self.exit_button.draw() == True:
            sortie=pygame.mixer.Sound("Son/sortir.wav")
            sortie.set_volume(0.15)
            sortie.play()
            pygame.quit()
            sys.exit()

    def menu3(self):
        self.menu_screen.blit(pygame.transform.scale(self.background3, (int(800), int(600))), (0, 0))
        self.exit_button = Button(10, 530, self.exit_image, 1)
        self.Logo1_button = Button(160, 20, self.Logo1, 0.10)
        self.Logo2_button = Button(20, 130, self.Logo2, 0.10)
        self.Logo3_button = Button(160, 240, self.Logo3, 0.10)


        if self.Logo1_button.draw()==True:
            select=pygame.mixer.Sound("Son/select.wav")
            select.set_volume(0.15)
            select.play()
            self.current_menu = 4
            self.menu_run()

        if self.Logo2_button.draw()==True:
            select=pygame.mixer.Sound("Son/select.wav")
            select.set_volume(0.15)
            select.play()
            self.current_menu = 5
            self.menu_run()


        if self.Logo3_button.draw()==True:
            select=pygame.mixer.Sound("Son/select.wav")
            select.set_volume(0.15)
            select.play()
            self.current_menu = 6
            self.menu_run()


        if self.exit_button.draw() == True:
            select=pygame.mixer.Sound("Son/select.wav")
            select.set_volume(0.15)
            select.play()
            self.current_menu-=1
            self.menu_run()

    # menu regroupant tous les menus
    def menu_run(self):
        if self.current_menu==1:
            self.menu1()
        elif self.current_menu ==2:
            self.menu2()
        elif self.current_menu == 3:
            self.menu3()
        else:
            self.run()
    
    # boucle jouant le level en fonction du menu choisi

    def run(self):
            current_level = self.current_menu - 4
            Level(levels[current_level]["init_pos"],levels[current_level]["background"],levels[current_level]["border"],levels[current_level]["hole"], self.WIDTH, self.HEIGHT,levels[current_level]["hole_pos"],levels[current_level]["bsize"]).run()
            self.current_menu+=1
            Level(levels[current_level]["init_pos"],levels[current_level]["background"],levels[current_level]["border"],levels[current_level]["hole"], self.WIDTH, self.HEIGHT,levels[current_level]["hole_pos"],levels[current_level]["bsize"]).run()
