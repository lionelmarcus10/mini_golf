import  pygame

# create levels

# integrer le paramètre du boutton
class Level:

    def __init__(self, init_pos ,background, border, hole, width, height):

        #load images
        self.background = pygame.image.load(background).convert_alpha()
        self.border = pygame.image.load(border).convert_alpha()
        self.hole = pygame.image.load(hole).convert_alpha()

        #init const
        self.w, self.h = (width, height)
        self.x, self.y = init_pos

        # create masks
        self.border_mask = pygame.mask.from_surface(self.border)
        self.hole_mask = pygame.mask.from_surface(self.hole)
        self.screen = pygame.display.get_surface()

        self.ball = pygame.Surface((self.w, self.h), flags=pygame.SRCALPHA)
        pygame.draw.circle(self.ball, (255, 255, 255), (self.x, self.y), 10)
        self.ball_mask = pygame.mask.from_surface(self.ball)
        self.draw_background()
        self.screen.blit(self.ball, (0, 0))
        #self.update_player()

    # Intègre les images dans la fenetre
    def draw_background(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.border, (0, 0))
        self.screen.blit(self.hole, (0, 0))

    def update_pos(self, dx, dy):
        previous_pos = self.x, self.y

        self.x += dx
        self.y += dy

        if not self.update_player():
            self.x, self.y = previous_pos

    # Dessine le backgound, et le ballon avec les nouvelles ou positions de bases
    def update_player(self):

        next_ball = pygame.Surface((self.w, self.h), flags=pygame.SRCALPHA)
        pygame.draw.circle(next_ball, (255, 255, 255), (self.x, self.y), 10)
        next_ball_mask = pygame.mask.from_surface(next_ball)

        collision = self.border_mask.overlap(next_ball_mask, (0,0))
        collision2 = self.hole_mask.overlap(next_ball_mask, (0, 0))
        if collision:
            return False
        if collision2:
            pygame.mixer.music.pause()
            pygame.mixer.Sound("Son/Trou.wav").play()

        self.draw_background()

        self.ball = next_ball
        self.screen.blit(self.ball, (0, 0))

        pygame.display.update()
        return True
