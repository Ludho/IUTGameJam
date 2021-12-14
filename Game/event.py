import pygame
import random

class Event:

    def __init__(self, game, fruit):
        self.fruit = fruit
        self.fillspeed = 1/random.randint(1,15)
        self.percent = [0,self.fillspeed]
        self.all_needs = ["poo","thirst","love"]
        self.need = "nothing"
        self.game = game
        self.image1 = pygame.image.load("Asset/Image/Bulle_Engrais.png")
        self.image2 = pygame.image.load("Asset/Image/Bulle_Arrosoir.png")
        self.image3 = pygame.image.load("Asset/Image/Bulle_Bisou.png")
        self.rect = self.image1.get_rect()
        self.rect.x = fruit.rect.x
        self.rect.y = fruit.rect.y

    def add_percent(self):
        self.percent[0] += self.percent[1]

    def isLoaded(self):
        return self.percent[0] >= 100

    def attemp_event(self):
        if self.fruit.name != "vide":
            if self.isLoaded():
                if (self.need == "nothing"):
                        self.need = random.choice(self.all_needs)
                if (self.need == "poo"):
                    self.game.screen.blit(self.image1, (self.fruit.rect.x + self.game.camera.x - 36, self.fruit.rect.y + self.game.camera.y - 70))
                if (self.need == "thirst"):
                    self.game.screen.blit(self.image2, (self.fruit.rect.x + self.game.camera.x - 36, self.fruit.rect.y + self.game.camera.y - 70))
                if (self.need == "love"):
                    self.game.screen.blit(self.image3, (self.fruit.rect.x + self.game.camera.x - 36, self.fruit.rect.y + self.game.camera.y - 70))
            elif not self.fruit.mure:
                self.add_percent()

    def reset_event(self):
        self.percent = [0,self.fillspeed]
        self.need = "nothing"

