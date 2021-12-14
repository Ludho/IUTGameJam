import pygame

class Porte:

    def __init__(self, game):
        self.name = "porte"
        self.game = game
        self.image = pygame.image.load("Asset/Image/Obstacle/block.png")
        self.rect = self.image.get_rect()
        self.rect.x = 480
        self.rect.y = 336
        self.y = self.rect.y + 96
        self.hold = False

    def affiche(self):
        self.game.screen.blit(self.image, (self.rect.x + self.game.camera.x - 36, self.rect.y + self.game.camera.y - 70))

    def actionPorte(self):
        self.game.screen.blit(self.game.key_f, (self.game.player.rectEcran.x + 40, self.game.player.rectEcran.y - 10))
        if self.game.pressed.get(pygame.K_f):
            self.game.sleep = True
            self.game.random_placement(self.game.x, self.game.y)
            # entre dans la maison et dort
            self.game.music.noise = 'Asset/musique/bruitage/Porte_maison.mp3'
            self.game.music.channel_back_noise.play(self.game.music.back_noise)
            self.game.music.channel_back_music.stop()
            self.game.music.back_music = pygame.mixer.Sound('Asset/musique/Musique_de_dodo.mp3')
            self.game.music.channel_back_music.play(self.game.music.back_music, 50)
            ###