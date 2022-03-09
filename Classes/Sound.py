import pygame

class Sound:
    def __init__(self):
        self.music= pygame.mixer_music.load("Son/boo classic.mp3")# musique du menu
        self.music_volume = pygame.mixer.music.set_volume(0.25)
        self.music_play = pygame.mixer.music.play(loops=-1)
        self.trou_sound = pygame.mixer.Sound("Son/Trou.wav") # music lorsque la balle tombe dans le trou
        self.coup_sound = pygame.mixer.Sound("Son/coup.wav")# musique lorsque on frappe la balle
        self.victoire_sound=pygame.mixer.Sound("Son/Victoire.wav")# musique lorsque le joueur a réussi un niveau
        self.Boutons_sound=pygame.mixer.Sound("Son/Boutons.wav")# musique lorsque le joueur clique sur un des 2 boutons
        self.sound_volume()

    def sound_volume(self):
        self.trou_sound.set_volume(0.05)
        self.coup_sound.set_volume(0.05)
        self.victoire_sound.set_volume(0.15)
        self.Boutons_sound.set_volume(0.15)
