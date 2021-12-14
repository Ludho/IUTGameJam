import pygame

class Arrosoir(pygame.sprite.Sprite):

    def __init__(self, coord, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("Asset/Image/arrosoir.png")
        self.name = "arrosoir"
        self.coo = self.game.grille.getCoord(coord.x, coord.y)
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = self.coo.x
        self.rect.y = self.coo.y
        self.y = self.coo.y + 96
        self.cases = coord
        self.hold = False
        self.game.grille.grille[int(coord.x)][int(coord.y)] = int(1)

    def move(self, coord):
        self.game.grille.grille[int(self.cases.x)][int(self.cases.y)] = int(0)
        self.coo = self.game.grille.getCoord(coord.x, coord.y)
        self.rect = self.image.get_rect()
        self.rect.x = self.coo.x
        self.rect.y = self.coo.y
        self.y = self.coo.y + 96
        self.cases = coord
        self.game.grille.grille[int(coord.x)][int(coord.y)] = int(1)

    def affiche(self):
        if not self.hold:
            self.game.screen.blit(self.image, (self.rect.x + self.game.camera.x-36, self.rect.y + self.game.camera.y-70))
