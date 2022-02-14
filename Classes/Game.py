import sys, pygame
from Classes.MainMenu import MainMenu

class Game:
    def __init__(self):

        #initiation de pygame
        pygame.init()
        self.WIDTH = 800
        self.HEIGHT = 600
        pygame.display.set_caption("Golf A109")
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.time.Clock().tick(60)

        #---------------------------------------------

        #font = pygame.font.SysFont(None,50,False,True)
        #img = font.render('Golf A109', True, (255,255,255))
        #self.screen.blit(img, (20, 20))

        #pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(30, 30, 60, 60))

        #----------------------------------------------
        self.main_menu = MainMenu()
        # ----------------------------------------------

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.main_menu.display()

            #update screen
            pygame.display.update()

