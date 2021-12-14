import pygame

class Boite:

    def __init__(self, coord, game):
        self.name = "boite"
        self.game = game
        self.image = pygame.image.load("Asset/Image/Coffre_V2.png")
        self.coo = self.game.grille.getCoord(coord.x, coord.y)
        self.rect = self.image.get_rect()
        self.rect.x = self.coo.x
        self.rect.y = self.coo.y
        self.y = self.coo.y + 96
        self.cases = coord
        self.hold = False
        self.game.grille.grille[int(coord.x)][int(coord.y)] = int(1)
        self.game.grille.grille[int(coord.x)+1][int(coord.y)] = int(1)

    def affiche(self):
        self.game.screen.blit(self.image, (self.rect.x + self.game.camera.x - 36, self.rect.y + self.game.camera.y - 70))

    def actionBoite(self):
        if self.game.player.hold != ():
            if self.game.player.hold.name in ["fraise", "carotte", "poire"] and self.game.player.hold.croissance >= 100:
                self.game.screen.blit(self.game.key_f, (self.game.player.rectEcran.x + 40, self.game.player.rectEcran.y - 10))
                if self.game.pressed.get(pygame.K_f):
                    self.game.player.hold = ()
                    self.game.score += 100

    def affiche(self):
        if not self.hold:
            self.game.screen.blit(self.image, (self.rect.x + self.game.camera.x-36, self.rect.y + self.game.camera.y-70))

