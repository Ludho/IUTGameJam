import pygame

class Grille:

    def __init__(self, game):
        self.game = game
        self.grille = [[0 for _ in range(32)] for _ in range(42)]

    def occupate(self, rec):
        self.grille[rec.x][rec.y] = 1

    def getCoord(self, x, y) -> int:
        return pygame.Vector2(x*48-480,y*48+ 384)

    def getCase(self, rec):
        return int(((rec.x + 1008)/48, (rec.y - 48)/48))