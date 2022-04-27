import  pygame
from math import *
import time
import numpy as np
# create levels

# integrer le paramètre du boutton
class Level:

    def __init__(self, init_pos, background, border, hole, width, height, hole_pos = [350, 240]):
        self.w, self.h = (width, height)

        self.hole_pos = hole_pos
        self.ball_size = 10

        hole_image = pygame.image.load(hole).convert_alpha()
        self.hole_size = hole_image.get_width()
        
        self.hole = pygame.Surface((self.w, self.h), flags=pygame.SRCALPHA)
        self.hole.blit(hole_image, hole_pos)

        self.hole_center = (hole_pos[0] + self.hole_size / 2, hole_pos[1] + self.hole_size / 2)

        #load images
        self.background = pygame.image.load(background).convert_alpha()
        self.border = pygame.image.load(border).convert_alpha()
        #init const

        self.x, self.y = init_pos

        # create masks
        self.border_mask = pygame.mask.from_surface(self.border)
        self.hole_mask = pygame.mask.from_surface(self.hole)
        self.screen = pygame.display.get_surface()

        self.ball = pygame.Surface((self.w, self.h), flags=pygame.SRCALPHA)
        pygame.draw.circle(self.ball, (255, 255, 255), (self.x, self.y), self.ball_size)
        self.ball_mask = pygame.mask.from_surface(self.ball)
        self.draw_background()
        self.screen.blit(self.ball, (0, 0))
        #self.update_player()

    # Intègre les images dans la fenetre
    def draw_background(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.border, (0, 0))
        self.screen.blit(self.hole, (0, 0))
        pygame.draw.lines(self.screen, (200, 150, 150), 1, self.hole_mask.outline())

    def update_pos(self, dx, dy):
        previous_pos = self.x, self.y

        self.x += dx
        self.y += dy

        if not self.update_player():
            self.x, self.y = previous_pos

    # Dessine le backgound, et le ballon avec les nouvelles ou positions de bases
    def update_player(self):

        next_ball = pygame.Surface((self.w, self.h), flags=pygame.SRCALPHA)
        pygame.draw.circle(next_ball, (255, 255, 255), (self.x, self.y), self.ball_size)
        next_ball_mask = pygame.mask.from_surface(next_ball)

        collision_border = self.border_mask.overlap(next_ball_mask, (0,0))
        if collision_border:
            return False

        collision_hole = self.hole_mask.overlap(next_ball_mask, (0, 0))
        if collision_hole:
            pygame.mixer.music.pause()
            pygame.mixer.Sound("Son/Trou.wav").play()

            n_steps = 300

            height = self.hole_center[1] - self.y
            hyp = sqrt((self.hole_center[0] - self.x)**2 + height**2)
            angle = asin(height/hyp) - 0.2

            theta = np.radians(np.linspace(0, 1000, n_steps))
            r = theta / 2
            x_2 = r*np.cos(theta)
            y_2 = r*np.sin(theta)

            x_final = ((np.cos(angle)*x_2 - np.sin(angle)*y_2) + self.hole_center[0])[::-1]
            y_final = ((np.sin(angle)*x_2 + np.cos(angle)*y_2) + self.hole_center[1])[::-1]

            print('SPIRAL', x_final, y_final)

            for i in range(n_steps):
                next_ball = pygame.Surface((self.w, self.h), flags=pygame.SRCALPHA)
                pygame.draw.circle(next_ball, (255, 255, 255), (x_final[i], y_final[i]), self.ball_size * 0.999**(i+1))
                self.draw_background()
                self.screen.blit(next_ball, (0, 0))
                pygame.display.update()
                print(f'pos {i} {(x_final[i] - self.ball_size / 2, y_final[i] - self.ball_size / 2)}')
                pygame.time.wait(10)

            return False


            # 
            # hyp = 

            # height = self.hole.y - next_ball.y
            # hyp = sqrt(height ^ 2 + (self.hole.x - next_ball.x) ^ 2)
            # angle = asin(height/hyp)

            # for i in range(1, 9):
            #     image = pygame.transform.rotate(pygame.image.load(f"Assets/image-{i}.png"),angle)
            #     self.screen.blit(image,(0,0))
            #     time.sleep(0.05)

        self.draw_background()

        self.ball = next_ball
        self.screen.blit(self.ball, (0, 0))

        pygame.display.update()
        return True
