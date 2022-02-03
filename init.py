import pygame

WIDTH = 800
HEIGHT = 600

class Game:
    def __init__(self):

        #initiation de pygame
        pygame.init()
        pygame.display.set_caption("Golf A109")
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: exit()

