
import pygame
from .score import Score
from .boxrs import Box
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
        self.score = 0
        self.Score = Score()


        self.ball = pygame.Surface((self.w, self.h), flags=pygame.SRCALPHA)
        pygame.draw.circle(self.ball, (255, 255, 255), (self.x, self.y), 10)
        self.ball_mask = pygame.mask.from_surface(self.ball)
        self.draw_background()
        self.screen.blit(self.ball, (0, 0))
        self.besoin_nom = False
        self.update_player()

    # Intègre les images dans la fenetre
    def draw_background(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.border, (0, 0))
        self.screen.blit(self.hole, (0, 0))
        self.update_score(self.screen)

    def draw_initial_state(self):
        self.draw_background()
        self.screen.blit(self.ball, (0, 0))

    def update_pos(self, dx, dy):
        previous_pos = self.x, self.y
        self.x += dx
        self.y += dy
        should_continue, collision = self.update_player()
        if collision:
            self.x, self.y = previous_pos
        return should_continue

    # Dessine le backgound, et le ballon avec les nouvelles ou positions de bases
    def update_player(self):

        next_ball = pygame.Surface((self.w, self.h), flags=pygame.SRCALPHA)
        pygame.draw.circle(next_ball, (255, 255, 255), (self.x, self.y), 10)
        next_ball_mask = pygame.mask.from_surface(next_ball)

        collision = self.border_mask.overlap(next_ball_mask, (0,0))
        collision2 = self.hole_mask.overlap(next_ball_mask, (0, 0))
        self.draw_background()
        if collision:
            self.score += 1
            self.update_score(self.screen)
            return True, True
        if collision2:
            pygame.mixer.music.pause()
            pygame.mixer.Sound("Son/Trou.wav").play()
            self.draw_background()
            self.tester_score()
            if self.besoin_nom:
                self.Score.ancien_score[-1] = (self.Score.nom, self.Score.nouveau_score)
                self.Score.trier_score()
                self.Score.sauvegarder_score()

            for i in range(0, len(self.Score.ancien_score)+1):
                self.screen.blit(self.Score.afficher_score(i), self.Score.score_corriger)
            return False, False


        pygame.display.flip()
        self.ball = next_ball
        self.screen.blit(self.ball, (0, 0))

        pygame.display.update()
        return True, False

    def update_score(self, screen):
    # afficher le score
        font = pygame.font.SysFont("monospace", 16)
        score_text = font.render(f"Score : {self.score}", True, (255, 0, 0))
        screen.blit(score_text, (10, 10))

    def tester_score(self):
    #permet de vérifier si les scores sont bien à jour
        self.Score.nouveau_score = self.score
        self.Score.verif_update()
        if self.Score.besoin_nom:
            self.besoin_nom = True


