import  pygame
from math import *
from Classes.Score import Score
from Classes.Box import Box
import numpy as np

# create levels

# integrer le paramètre du boutton
class Level:

    def __init__(self, init_pos, background, border, hole, width, height, hole_pos,bsize):
        self.w, self.h = (width, height)

        self.hole_pos = hole_pos
        self.ball_size = bsize
        self.box = Box(100, 100, 140, 32)
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
        self.col = 0
        self.score = 0
        self.Score = Score()

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
        self.update_score(self.screen)
        #pygame.draw.lines(self.screen, (200, 150, 150), 1, self.hole_mask.outline())

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
        # effets après collision avec le bord
        if collision_border:
            return False

        collision_hole = self.hole_mask.overlap(next_ball_mask, (0, 0))
        # effets apres collision avec le trou
        if collision_hole:
            trou=pygame.mixer.Sound("Son/Fall.wav")
            trou.set_volume(0.15)
            trou.play()
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

                

            #------------------------------------------------------
            self.tester_score()
            if self.besoin_nom:
                self.Score.ancien_score[-1] = (self.Score.nom, self.Score.nouveau_score)
                self.Score.trier_score()
                self.Score.sauvegarder_score()

            for i in range(0, len(self.Score.ancien_score)+1):
                self.screen.blit(self.Score.afficher_score(i), self.Score.score_corriger)
            
            self.col = 1
            pygame.time.wait(1000)
            return False, False
            #------------------------------------------------------

        self.draw_background()

        self.ball = next_ball
        self.screen.blit(self.ball, (0, 0))

        pygame.display.update()
        return True
    

    def update_score(self, screen):
    # afficher le score
        self.score = round(self.score)
        font = pygame.font.SysFont("monospace", 16)
        score_text = font.render(f"Score : {self.score}", True, (255, 0, 0))
        screen.blit(score_text, (10, 10))
    
    def tester_score(self):
    #permet de vérifier si les scores sont bien à jour
        self.Score.nouveau_score = self.score
        self.Score.verif_update()
        if self.Score.besoin_nom:
            self.besoin_nom = True
    
    def entrer_nom(self, screen):
        # permet d'entrer le nom du joueur dans le classement
        while not self.box.nom_saisi:
            for event in pygame.event.get():
                self.box.gestion_text(event)
                pygame.display.flip()
            self.draw_background()
            self.box.maj()
            self.box.ecrire(screen)
            pygame.display.flip()
        self.Score.nom = self.box.text
        self.besoin_nom = False
        self.update_player()

    def run(self):
        speed = (10, 10)
        move = {
            pygame.K_LEFT: (-1*speed[0], 0),
            pygame.K_RIGHT: (1*speed[0], 0),
            pygame.K_UP: (0, -1*speed[1]),
            pygame.K_DOWN: (0, 1*speed[1])
        }
        # Saisie du pseudo de l'utilisateur
        self.entrer_nom(self.screen)
        self.boucle = True
        while self.boucle == True:
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
              if event.type == pygame.MOUSEBUTTONUP:
                x1 = pos[0]
                y1 = pos[1]

                #conditions
                xspeed = 0
                yspeed = 0
                #gauche 
                if x1 < self.x:
                    xspeed = -40
                # droite
                else:
                    #x1 > self.level.x
                    xspeed = 40
                # haut
                if y1 < self.y:
                    yspeed = -40
                #bas
                else:
                    # y1 > self.level.x
                    yspeed = 40
        
                self.update_pos(xspeed, yspeed)

            keys = pygame.key.get_pressed()
            for key in move:
                if keys[key]:
                    self.score+= 0.5
                    self.update_pos(*move[key])
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            
            if self.col == 1:
               self.boucle = False
               return True

            #update screen
            pygame.display.update()
            
            
