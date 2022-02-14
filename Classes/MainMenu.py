import pygame

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
        self.choice3 = "INFOS"

        # IMAGES

        self.background = pygame.image.load("Assets/Start_menu_back.png")
        self.logo = pygame.image.load("Assets/LOGO.png")

        # FONT

        self.font_export = pygame.font.Font("Fonts/Melinda Rosalie.ttf",90)
        self.game_welcome = self.font_export.render(self.menu_text, True, (255, 255, 255))

        # building of UI

        self.menu_screen = pygame.display.get_surface()
        self.menu_screen.blit(self.background, (0, 0))
        self.menu_screen.blit(self.logo, (self.WIDTH / 2.2, self.HEIGHT / 10))
        self.menu_screen.blit(self.game_welcome, (self.WIDTH / 2.5, self.HEIGHT / 4))


    def display(self):
        pass

    def update(self):
        pass

    def choice(self):
        pass


