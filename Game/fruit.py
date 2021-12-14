import pygame, random

from event import Event

class Fruit(pygame.sprite.Sprite):

    def __init__(self, game, name, coord):
        super().__init__()
        self.name = name
        self.game = game
        self.hold = False
        self.coo = game.grille.getCoord(coord.x, coord.y)
        self.cases = coord
        self.rect = self.coo
        self.rect.x = self.coo.x
        self.rect.y = self.coo.y
        self.y = self.coo.y + 96
        self.game.grille.grille[int(coord.x)][int(coord.y)] = int(1)
        self.event = Event(self.game, self)
        self.croissance = 0
        self.mure = False
        if name == "fraise":
            if self.event.need == "poo" or self.event.need == "thirst" or self.event.need == "love":
                self.image = pygame.image.load("Asset/Image/Panier/Panier_BBFraise_Pleure_V2.png")
            else:
                self.image = pygame.image.load("Asset/Image/Panier/Panier_BBFraise_V2.png")
        elif name == "poire":
            if self.event.need == "poo" or self.event.need == "thirst" or self.event.need == "love":
                self.image = pygame.image.load("Asset/Image/Panier/Panier_BBPoire_Pleure_V2.png")
            else:
                self.image = pygame.image.load("Asset/Image/Panier/Panier_BBPoire_V2.png")
        elif name == "carotte":
            if self.event.need == "poo" or self.event.need == "thirst" or self.event.need == "love":
                self.image = pygame.image.load("Asset/Image/Panier/Panier_BBCarotte_Pleure_V2.png")
            else:
                self.image = pygame.image.load("Asset/Image/Panier/Panier_BBCarotte_V2.png")
        elif name == "vide":
            self.image = pygame.image.load("Asset/Image/Panier/Panier_V2.png")
        self.test = pygame.image.load("Asset/Image/Icon.png")
        self.chargement_image = 0
        self.current_image = 0
        self.Fraise = animations.get("BBFraise_")
        self.FraiseP = animations.get("BBFraise_Pleure_")
        self.Poire = animations.get("BBPoire_")
        self.PoireP = animations.get("BBPoire_Pleure_")
        self.Carotte = animations.get("BBCarotte_")
        self.CarotteP = animations.get("BBCarotte_Pleure_")

    def murir(self):
        if self.event.need == "nothing" and self.croissance < 100:
            self.croissance += 5/60
        if self.croissance >= 100:
            self.mure = True

    def move(self, coord):
        self.game.grille.grille[int(self.cases.x)][int(self.cases.y)] = int(0)
        self.coo = self.game.grille.getCoord(coord.x, coord.y)
        self.rect = self.image.get_rect()
        self.rect.x = self.coo.x
        self.rect.y = self.coo.y
        self.y = self.coo.y + 96
        self.cases = coord
        self.game.grille.grille[int(coord.x)][int(coord.y)] = int(1)

    def actionFruit(self):
        # if self.game.player.hold != ():
        #     print(self.game.player.hold.name)
        # print(self.name)
        if self.name != "vide":
            if self.game.player.hold == self.game.composte_fraise and self.event.need == "poo" and self.name == "fraise":
                self.game.screen.blit(self.game.key_f, (self.game.player.rectEcran.x + 4, self.game.player.rectEcran.y - 80))
                if self.game.pressed.get(pygame.K_f):
                    self.event.reset_event()
            if self.game.player.hold == self.game.composte_poire and self.event.need == "poo" and self.name == "poire":
                self.game.screen.blit(self.game.key_f, (self.game.player.rectEcran.x + 4, self.game.player.rectEcran.y - 80))
                if self.game.pressed.get(pygame.K_f):
                    self.event.reset_event()
            if self.game.player.hold == self.game.composte_carotte and self.event.need == "poo" and self.name == "carotte":
                self.game.screen.blit(self.game.key_f, (self.game.player.rectEcran.x + 4, self.game.player.rectEcran.y - 80))
                if self.game.pressed.get(pygame.K_f):
                    self.event.reset_event()
            if self.game.player.hold == self.game.arrosoir and self.event.need == "thirst":
                self.game.screen.blit(self.game.key_f, (self.game.player.rectEcran.x + 4, self.game.player.rectEcran.y - 80))
                if self.game.pressed.get(pygame.K_f):
                    self.event.reset_event()
            if self.game.player.hold == () and self.event.need == "love":
                self.game.screen.blit(self.game.key_f,
                                      (self.game.player.rectEcran.x + 4, self.game.player.rectEcran.y - 80))
                if self.game.pressed.get(pygame.K_f):
                    self.event.reset_event()
            if self.game.player.hold == () and self.event.need == "nothing":
                self.game.screen.blit(self.game.key_f, (self.game.player.rectEcran.x + 4, self.game.player.rectEcran.y - 80))
                if self.game.pressed.get(pygame.K_f):
                    if self.name == "fraise":
                        self.game.player.hold = self.game.fraise
                        self.game.fraise.croissance = self.croissance
                        self.croissance = 0
                    elif self.name == "carotte":
                        self.game.player.hold = self.game.carotte
                        self.game.carotte.croissance = self.croissance
                        self.croissance = 0
                    elif self.name == "poire":
                        self.game.player.hold = self.game.poire
                        self.game.poire.croissance = self.croissance
                        self.croissance = 0
                    self.name = "vide"
        else:
            if self.game.player.hold != ():
                if self.game.player.hold.name in ["fraise", "carotte", "poire"]:
                    self.game.screen.blit(self.game.key_g,
                                          (self.game.player.rectEcran.x + 4, self.game.player.rectEcran.y - 80))
                    if self.game.pressed.get(pygame.K_g):
                        self.name = self.game.player.hold.name
                        self.croissance = self.game.player.hold.croissance
                        self.game.player.hold = ()


    def affiche(self):
        if self.name == "fraise":
            if self.event.need == "poo" or self.event.need == "thirst" or self.event.need == "love":
                self.animate(self.FraiseP)
            elif self.mure == True:
                self.image = pygame.image.load("Asset/Image/Panier/Panier_Fraise_V2.png")
            else:
                self.animate(self.Fraise)
        elif self.name == "poire":
            if self.event.need == "poo" or self.event.need == "thirst" or self.event.need == "love":
                self.animate(self.PoireP)
            elif self.mure == True:
                self.image = pygame.image.load("Asset/Image/Panier/Panier_Poire_V2.png")
            else:
                self.animate(self.Poire)
        elif self.name == "carotte":
            if self.event.need == "poo" or self.event.need == "thirst" or self.event.need == "love":
                self.animate(self.CarotteP)
            elif self.mure == True:
                self.image = pygame.image.load("Asset/Image/Panier/Panier_Carotte_V2.png")
            else:
                self.animate(self.Carotte)
        elif self.name == "vide":
            self.image = pygame.image.load("Asset/Image/Panier/Panier_V2.png")
        self.game.screen.blit(self.image,(self.rect.x + self.game.camera.x-36, self.rect.y + self.game.camera.y-70))
        self.event.attemp_event()

    def animate(self, dir):
        self.chargement_image += 2
        if self.chargement_image >= 10:
            self.current_image += 1
            if self.current_image >= len(dir):
                # remettre l'anim au depart
                self.current_image = 0
            self.image = dir[self.current_image]
            self.chargement_image = 0

def get_image1_path(sprite_name):
    path = f"Asset/animation/Fruits/{sprite_name}/{sprite_name}"
    return path + str(1) + '.png'


def load_animation_images(sprite_name):
    #charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    #recuperer le chemin du dossier pour ce sprite
    path = f"Asset/animation/Fruits/{sprite_name}/{sprite_name}"
    #boucler sur chaque image dans ce dossier
    for num in range(1,11): #1ere et dernière image
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    #renvoyer contenu de la liste d'images
    return images

#definir un dictionnaire qui va contenir les images chargées de chaque sprite
animations = {
    'BBCarotte_': load_animation_images('BBCarotte_'),
    'BBCarotte_Pleure_': load_animation_images('BBCarotte_Pleure_'),
    ########################
    'BBFraise_': load_animation_images('BBFraise_'),
    'BBFraise_Pleure_': load_animation_images('BBFraise_Pleure_'),
    #######################
    'BBPoire_': load_animation_images('BBPoire_'),
    'BBPoire_Pleure_': load_animation_images('BBPoire_Pleure_')
}