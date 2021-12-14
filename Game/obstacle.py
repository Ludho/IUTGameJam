import pygame

class Obstacle:

    def __init__(self, name, coord, game):
        self.name = name
        self.game = game
        if name == "block":
            self.image = pygame.image.load("Asset/Image/Obstacle/block.png")
        elif name == "barriere":
            self.image = pygame.image.load("Asset/Image/Obstacle/barriere.png")
        elif name == "buisson":
            self.image = pygame.image.load("Asset/Image/Obstacle/Buisson.png")
        elif name == "rocher_1":
            self.image = pygame.image.load("Asset/Image/Obstacle/Rocher_1.png")
        elif name == "rocher_2":
            self.image = pygame.image.load("Asset/Image/Obstacle/Rocher_2.png")
        elif name == "rocher_3":
            self.image = pygame.image.load("Asset/Image/Obstacle/Rocher_3.png")

        self.coo = self.game.grille.getCoord(coord.x, coord.y)
        self.rect = self.image.get_rect()
        self.rect.x = self.coo.x
        self.rect.y = self.coo.y
        self.y = self.coo.y + 96
        self.cases = coord
        self.hold = False
        self.game.grille.grille[int(coord.x)][int(coord.y)] = int(1)

    def affiche(self):
        self.game.screen.blit(self.image, (self.rect.x + self.game.camera.x - 36, self.rect.y + self.game.camera.y - 70))