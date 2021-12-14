import pygame

class FruitName(pygame.sprite.Sprite):

    def __init__(self,game , name):
        super().__init__()
        self.name = name
        self.game = game
        self.croissance = 0