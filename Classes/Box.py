import pygame as pg

class Box:
    #classe qui permet d'entrer le pseudo du joueur dans une boite avant de lancer un niveau
    def __init__(self, x, y, w, h, text="ENTREZ VOTRE NOM"):
        self.ecran = pg.Rect(x, y, w, h)
        self.couleur = pg.Color('white')
        self.text = text
        self.font = pg.font.SysFont('Verdana', 18, 0)
        self.txt_surface = self.font.render(text, True, self.couleur)
        self.activation = False
        self.nom_saisi = False

    def gestion_text(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.ecran.collidepoint(event.pos):
                self.activation = not self.activation
                self.text = ""
                self.txt_surface = self.font.render(self.text, True, self.couleur)
            else:
                self.activation = False
        if event.type == pg.KEYDOWN:
            if self.activation and event.key == pg.K_RETURN:
                self.nom_saisi = True
            elif event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.txt_surface = self.font.render(self.text, True, self.couleur)

    def maj(self):
        wi = max(180, self.txt_surface.get_width()+10)
        self.ecran.w = wi

    def ecrire(self, screen):
        screen.blit(self.txt_surface, (self.ecran.x+5, self.ecran.y+5))
        pg.draw.rect(screen, self.couleur, self.ecran, 2)