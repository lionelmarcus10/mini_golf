import pygame

class Sound:
    def __init__(self):
        self.music= pygame.mixer_music.load("Son/Son_ap.mp3")# musique du menu
        self.music_volume = pygame.mixer.music.set_volume(0.25)#réglage du volume sonore du son principal
        self.music_play = pygame.mixer.music.play(loops=-1)#musique qui va tourner en boucle
        self.trou_sound = pygame.mixer.Sound("Son/Fall.wav") # music lorsque la balle tombe dans le trou
        self.victoire_sound=pygame.mixer.Sound("Son/Victoire.wav")# musique lorsque le joueur a réussi un niveau
        self.Boutons_sound=pygame.mixer.Sound("Son/select.wav")# musique lorsque le joueur clique sur un des 2 boutons
