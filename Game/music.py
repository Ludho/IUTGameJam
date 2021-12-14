import pygame

class Music:

    def __init__(self):
        self.noise = 'Asset/musique/bruitage/Porte_maison.mp3'
        self.back_music = pygame.mixer.Sound('Asset/musique/Musique de fond.mp3')
        self.back_noise = pygame.mixer.Sound(self.noise)
        self.pleure = pygame.mixer.Sound('Asset/musique/bruitage/pleure.mp3')
        self.channel_back_music = pygame.mixer.Channel(0)
        self.channel_back_noise = pygame.mixer.Channel(1)
        self.channel_pleure = pygame.mixer.Channel(3)
