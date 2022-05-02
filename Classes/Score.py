import os
import json
import pygame
class Score:
    def __init__(self,score=0, pseudo ='dingding'):
        self.besoin_nom = False
        self.nom = pseudo
        self.ancien_score = []
        self.nouveau_score = score
        self.fichier_exist = False
        self.verif_fichier()
        self.load_ancien_score()
        self.score_corriger = (100, 400)

    def afficher_score(self, nombre):
        police1 = pygame.font.SysFont('Verdana', 20, 0)
        police2 = pygame.font.SysFont('Verdana', 30, 1)
        if nombre == 0:
            score_txt = police2.render("MEILLEURS SCORES", True, (250, 0, 0))
            
        else:
            score_txt = police1.render(f"{nombre}: {self.ancien_score[nombre-1][1]} points pour {self.ancien_score[nombre-1][0]}", True, (250, 0, 0))
            self.score_corriger = (100, 450 + (28*(nombre-1)))
        return score_txt
    def verif_fichier(self):
        if os.path.exists("score.txt"):
            self.fichier_exist = True
        else:
            self.creer_pardefault()

    def creer_pardefault(self):
        if not self.fichier_exist:
            default = open("score.txt", "w")
            json.dump(["Admin", 5,"beta_tester_1", 6,"beta_tester_2", 10,"beta_testeur_3", 150,"first_player", 100], default)
            default.close()
            self.fichier_exist = True

    def load_ancien_score(self):
        if self.fichier_exist:
            self.ancien_score = []
            op = open("score.txt", "r")
            list_score = json.load(op)
            for i in range(len(list_score)):
                if i % 2 == 0:
                    self.ancien_score.append((list_score[i], list_score[i+1]))
            op.close()

    def verif_update(self):
        if self.nouveau_score <= self.ancien_score[-1][1]:
            self.besoin_nom = True

    def trier_score(self):
        self.ancien_score = sorted(self.ancien_score, key=lambda score: score[1])

    def sauvegarder_score(self):
        default = open("score.txt", "w")
        list_score = []
        for i in range(len(self.ancien_score)):
            list_score.append(self.ancien_score[i][0])
            list_score.append(self.ancien_score[i][1])
        json.dump(list_score, default)
        default.close()
