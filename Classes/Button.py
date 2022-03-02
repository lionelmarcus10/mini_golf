# button class
import pygame.display


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.cliked = False

    def draw(self):
        action = False
        # get mouse position
        position = pygame.mouse.get_pos()


        # check mouseover and conditions
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.cliked == False:
                self.cliked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.cliked = False

        # draw button on screen
        self.screen = pygame.display.get_surface()
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

        return action