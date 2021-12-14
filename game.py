import pygame, random
from player import Player
from arrosoir import Arrosoir
from composte import Composte
from grille import Grille
from fruit import Fruit
from fruitName import FruitName
from porte import Porte
from boite import Boite

class Game:

    def __init__(self, screen):
        # definir si notre jeu a commencé
        self.is_playing = False
        self.is_over = False
        self.is_ended = False
        #################################
        self.pressed = {}  # dictionnaire = agrégat de clés associés à des valeurs
        self.screen = screen
        self.score = 0
        self.grille = Grille(self)
        self.camera = pygame.Vector2(0, 0)
        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.fraise = FruitName(self, "fraise")
        self.carotte = FruitName(self, "carotte")
        self.poire = FruitName(self, "poire")
        self.arrosoir = Arrosoir(pygame.Vector2(0, 0), self)
        self.composte_fraise = Composte("composte_fraise", pygame.Vector2(4, 4), self)
        self.composte_carotte = Composte("composte_carotte", pygame.Vector2(3, 3), self)
        self.composte_poire = Composte("composte_poire", pygame.Vector2(6, 6), self)
        self.objects = [self.arrosoir, self.composte_fraise, self.composte_carotte, self.composte_poire]
        self.objects.append(Porte(self))
        self.objects.append(Boite(pygame.Vector2(20, 1), self))
        self.key_f = pygame.image.load("Asset/Image/key_f.png")
        self.key_p = pygame.image.load("Asset/Image/key_p.png")
        self.key_g = pygame.image.load("Asset/Image/key_g.png")
        self.background = pygame.Vector2(-1044, -22)
        # self.fruit = Fruit(self, "fraise")
        self.all_fruits = pygame.sprite.Group()
        self.spawn_fruit(pygame.Vector2(11, 6))
        self.spawn_fruit(pygame.Vector2(14, 7))
        self.spawn_fruit(pygame.Vector2(12, 4))
        # self.all_fruits.add(self.fruit)
        self.objects.append(Fruit(self, "vide", pygame.Vector2(19, 3)))
        self.listAff = [self.player]
        self.listAff.extend(self.objects)
        self.sleep = False
        self.sleepJauge = 0
        self.zzz = pygame.image.load("Asset/Image/zzz.png")

    def is_moving(self):
        if self.pressed.get(pygame.K_RIGHT) or self.pressed.get(pygame.K_LEFT) or self.pressed.get(pygame.K_UP) or self.pressed.get(pygame.K_DOWN):
            return True
        else:
            return False

    def fin_fruits(self):
        if self.player.hold == ():
            for obj in self.objects:
                if obj.name in ["fraise", "carotte", "poire"]:
                    return False
            return True
    def game_over(self):
        self.is_over = True
        self.is_playing = False

    def attempt_end(self):
        if self.fin_fruits():
            self.is_ended = True
            self.is_playing = False

    def interract(self):
        for obj in self.objects:
            if obj.name == "porte":
                if self.player.dir == "up":
                    if obj.rect.x + self.camera.x + 48 <= self.player.rectEcran.x + 36 <= obj.rect.x + self.camera.x + 96:
                        if obj.rect.y + self.camera.y + 48 <= self.player.rectEcran.y + 50 <= obj.rect.y + self.camera.y + 96:
                            obj.actionPorte()
            elif not obj.hold:
                if self.player.dir == "right":
                    if obj.rect.x + self.camera.x + 48 <= self.player.rectEcran.x + 72 <= obj.rect.x + self.camera.x + 96:
                        if obj.rect.y + self.camera.y + 48 <= self.player.rectEcran.y + 72 <= obj.rect.y + self.camera.y + 96:
                            if obj.name in ["fraise", "carotte", "poire", "vide"]:
                                obj.actionFruit()
                            elif obj.name == "boite":
                                obj.actionBoite()
                            elif self.player.hold != obj:
                                self.screen.blit(self.key_f, (self.player.rectEcran.x + 4, self.player.rectEcran.y - 80))
                                if self.pressed.get(pygame.K_f):
                                    self.player.prendre(obj)
                if self.player.dir == "left":
                    if obj.rect.x + self.camera.x + 48 <= self.player.rectEcran.x <= obj.rect.x + self.camera.x + 96:
                        if obj.rect.y + self.camera.y + 48 <= self.player.rectEcran.y + 72 <= obj.rect.y + self.camera.y + 96:
                            if obj.name in ["fraise", "carotte", "poire", "vide"]:
                                obj.actionFruit()
                            elif obj.name == "boite":
                                obj.actionBoite()
                            elif self.player.hold != obj:
                                self.screen.blit(self.key_f, (self.player.rectEcran.x + 4, self.player.rectEcran.y - 80))
                                if self.pressed.get(pygame.K_f):
                                    self.player.prendre(obj)
                if self.player.dir == "up":
                    if obj.rect.x + self.camera.x + 48 <= self.player.rectEcran.x + 36 <= obj.rect.x + self.camera.x + 96:
                        if obj.rect.y + self.camera.y + 48 <= self.player.rectEcran.y + 68 <= obj.rect.y + self.camera.y + 96:
                            if obj.name in ["fraise", "carotte", "poire", "vide"]:
                                obj.actionFruit()
                            elif obj.name == "boite":
                                obj.actionBoite()
                            elif self.player.hold != obj:
                                self.screen.blit(self.key_f, (self.player.rectEcran.x + 4, self.player.rectEcran.y - 80))
                                if self.pressed.get(pygame.K_f):
                                    self.player.prendre(obj)
                if self.player.dir == "down":
                    if obj.rect.x + self.camera.x + 48 <= self.player.rectEcran.x + 36 <= obj.rect.x + self.camera.x + 96:
                        if obj.rect.y + self.camera.y + 48 <= self.player.rectEcran.y + 96 <= obj.rect.y + self.camera.y + 96:
                            if obj.name in ["fraise", "carotte", "poire", "vide"]:
                                obj.actionFruit()
                            elif obj.name == "boite":
                                obj.actionBoite()
                            elif self.player.hold != obj:
                                self.screen.blit(self.key_f, (self.player.rectEcran.x + 4, self.player.rectEcran.y - 80))
                                if self.pressed.get(pygame.K_f):
                                    self.player.prendre(obj)

    def block(self, key):
        for i in range(len(self.grille.grille)):
            for j in range(len(self.grille.grille[i])):
                coor = self.grille.getCoord(i, j)
                if self.grille.grille[i][j] == 1:
                    coor.x += 480
                    coor.y -= 384
                    if key == "right":
                        if coor.x == (-self.camera.x + 1000):
                            if coor.y <= (-self.camera.y + 20) <= coor.y + 40 or \
                                    coor.y <= (-self.camera.y + 45) <= coor.y + 48:
                                return False
                    if key == "left":
                        if coor.x + 48 == (-self.camera.x + 960):
                            if coor.y <= (-self.camera.y + 20) <= coor.y + 40 or \
                                    coor.y <= (-self.camera.y + 45) <= coor.y + 48:
                                return False
                    if key == "up":
                        if coor.y + 24 == (-self.camera.y):
                            if coor.x <= (-self.camera.x + 965) <= coor.x + 48 or \
                                    coor.x <= (-self.camera.x + 995) <= coor.x + 48:
                                return False
                    if key == "down":
                        if coor.y == (-self.camera.y + 48):
                            if coor.x <= (-self.camera.x + 965) <= coor.x + 48 or \
                                    coor.x <= (-self.camera.x + 995) <= coor.x + 48:
                                return False
        return True

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_fruit(self, coord):
        self.objects.append(Fruit(self, random.choice(["fraise", "carotte", "poire"]), coord))

    def affiche(self):
        self.listAff.sort(key=lambda x: float(x.y))
        for obj in self.listAff:
            obj.affiche()

    def update(self, screen):
        # vérifier déplacements
        if self.sleep and self.sleepJauge <= 100:
            self.sleepJauge += 0.5
            if self.sleepJauge == 100:
                self.sleep = False
                self.sleepJauge = 0
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.zzz, (1024 / 2 - 50, 768 / 2 - 270))
        else:
            if self.pressed.get(pygame.K_RIGHT) :
                if self.block("right") and self.camera.x >= (-2016 / 2):
                    self.player.move_right()
                self.player.dir = "right"
            if self.pressed.get(pygame.K_LEFT) :
                if self.block("left") and self.camera.x <= (2016 / 2) - 48:
                    self.player.move_left()
                self.player.dir = "left"
            if self.pressed.get(pygame.K_UP) :
                if self.block("up") and self.camera.y <= 0:
                    self.player.move_up()
                self.player.dir = "up"
            if self.pressed.get(pygame.K_DOWN):
                if self.block("down") and self.camera.y >= (-1536) + 72:
                    self.player.move_down()
                self.player.dir = "down"
            if self.pressed.get(pygame.K_p):
                self.player.place()
            if self.pressed.get(pygame.K_b):
                self.is_playing = False
            self.all_fruits.draw(screen)
            self.affiche()
            self.player.holding()
            self.interract()
            self.player.vision()
            for obj in self.objects:
                if obj.name in ["fraise", "carotte", "poire"]:
                    obj.murir()
            #print(self.score)
            self.attempt_end()
