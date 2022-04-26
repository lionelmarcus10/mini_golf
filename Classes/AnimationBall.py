import pygame
import sys
import time


class Anim(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__()
            self.sprites = []
            self.animeting = False
            for i in range(1,9):
                self.sprites.append(pygame.image.load(f"Assets/image-{i}.png"))
                time.sleep(2)
                #break

            self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]

            self.rect = self.image.get_rect()
            self.rect.topleft = [pos_x, pos_y]

        def animet(self):
            self.animeting = True

        def update(self,speed):
            if self.animeting == True:
                self.current_sprite += speed

                if self.current_sprite >= len(self.sprites):
                    self.current_sprite = 0
                    self.animeting = False

                self.image = self.sprites[int(self.current_sprite)]


moving_sprites = pygame.sprite.Group()
player = Anim(5,5)
moving_sprites.add(player)



while True:

    if event.type == pygame.KEYDOWN:
            player.animet()


    moving_sprites.draw(screen)
    moving_sprites.update(0.25)


