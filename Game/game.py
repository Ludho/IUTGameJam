import pygame, random
from player import Player
from arrosoir import Arrosoir
from composte import Composte
from grille import Grille
from fruit import Fruit
from fruitName import FruitName
from porte import Porte
from boite import Boite
from obstacle import Obstacle

class Game:

    def __init__(self, screen, music):
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
        self.fraise = FruitName(self, "fraise")
        self.carotte = FruitName(self, "carotte")
        self.poire = FruitName(self, "poire")
        self.arrosoir = None
        self.composte_fraise = None
        self.composte_carotte = None
        self.composte_poire = None
        self.objects = []
        self.key_f = pygame.image.load("Asset/Image/key_f.png")
        self.key_p = pygame.image.load("Asset/Image/key_p.png")
        self.key_g = pygame.image.load("Asset/Image/key_g.png")
        self.zzz = pygame.image.load("Asset/Image/zzz.png")
        self.bg = None
        self.background = pygame.Vector2(-1044, -22)
        self.listAff = []
        self.sleep = False
        self.voisinJauge = 0
        self.x = 0
        self.y = 0
        self.music = music

    def init(self, level):
        if level == 1:
            self.bg = pygame.image.load("Asset/Image/Fond_Level_1.png")
            self.x = 7
            self.y = 13
            self.arrosoir = Arrosoir(pygame.Vector2(8 + self.x, 0), self)
            self.composte_fraise = Composte("composte_fraise", pygame.Vector2(2 + self.x, 0), self)
            self.composte_carotte = Composte("composte_carotte", pygame.Vector2(4 + self.x, 0), self)
            self.composte_poire = Composte("composte_poire", pygame.Vector2(6 + self.x, 0), self)
            self.objects.append(self.arrosoir)
            self.objects.append(self.composte_fraise)
            self.objects.append(self.composte_carotte)
            self.objects.append(self.composte_poire)
            self.objects.append(Boite(pygame.Vector2(17 + self.x, 0), self))
            self.objects.append(Porte(self))

            for x in range(7):
                for y in range(6):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + self.x + 5, y + 6), self))
            for x in range(3):
                for y in range(3):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + self.x + 12, y + 9), self))
            self.spawn_fruit(pygame.Vector2(29, 3))
            self.spawn_fruit(pygame.Vector2(30, 14))
            self.spawn_fruit(pygame.Vector2(12, 13))
            self.objects.append(Obstacle("buisson", pygame.Vector2(30, 7), self))
            self.objects.append(Obstacle("buisson", pygame.Vector2(23, 5), self))
            self.objects.append(Obstacle("rocher_1", pygame.Vector2(26, 7), self))
            self.objects.append(Obstacle("rocher_2", pygame.Vector2(8, 15), self))
            self.objects.append(Obstacle("rocher_2", pygame.Vector2(20, 16), self))
            self.objects.append(Obstacle("rocher_3", pygame.Vector2(12, 4), self))
            self.objects.append(Fruit(self, "vide", pygame.Vector2(19, 4)))
            self.listAff = [self.player]
            self.listAff.extend(self.objects)
        elif level ==2:
            self.bg = pygame.image.load("Asset/Image/Fond_Level_2.png")
            self.x = 7
            self.y = 13
            self.arrosoir = Arrosoir(pygame.Vector2(8 + self.x, 0), self)
            self.composte_fraise = Composte("composte_fraise", pygame.Vector2(2 + self.x, 0), self)
            self.composte_carotte = Composte("composte_carotte", pygame.Vector2(4 + self.x, 0), self)
            self.composte_poire = Composte("composte_poire", pygame.Vector2(6 + self.x, 0), self)
            self.objects.append(self.arrosoir)
            self.objects.append(self.composte_fraise)
            self.objects.append(self.composte_carotte)
            self.objects.append(self.composte_poire)
            self.objects.append(Boite(pygame.Vector2(17 + self.x, 0), self))
            self.objects.append(Porte(self))

            for x in range(4):
                for y in range(5):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + self.x + 3, y + 5), self))
            self.objects.append(Obstacle("block", pygame.Vector2(13, 10), self))
            self.objects.append(Obstacle("block", pygame.Vector2(13, 11), self))
            for x in range(3):
                for y in range(5):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + 14, y + 7), self))
            for x in range(5):
                for y in range(6):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + 25, y + 4), self))
            self.objects.append(Obstacle("block", pygame.Vector2(30, 4), self))
            self.objects.append(Obstacle("block", pygame.Vector2(30, 5), self))
            self.objects.append(Obstacle("block", pygame.Vector2(24, 7), self))
            self.objects.append(Obstacle("block", pygame.Vector2(24, 8), self))
            self.objects.append(Obstacle("block", pygame.Vector2(24, 9), self))
            for x in range(7):
                for y in range(3):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + 21, y + 10), self))
            for x in range(4):
                for y in range(2):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + 21, y + 13), self))
            self.spawn_fruit(pygame.Vector2(29, 11))
            self.spawn_fruit(pygame.Vector2(26, 14))
            self.spawn_fruit(pygame.Vector2(10, 15))
            self.spawn_fruit(pygame.Vector2(14, 16))
            self.spawn_fruit(pygame.Vector2(21, 8))
            self.objects.append(Obstacle("buisson", pygame.Vector2(16, 14), self))
            self.objects.append(Obstacle("buisson", pygame.Vector2(10, 11), self))
            self.objects.append(Obstacle("rocher_1", pygame.Vector2(13, 3), self))
            self.objects.append(Obstacle("rocher_2", pygame.Vector2(32, 1), self))
            self.objects.append(Obstacle("rocher_2", pygame.Vector2(32, 16), self))
            self.objects.append(Obstacle("rocher_3", pygame.Vector2(19, 14), self))
            self.objects.append(Fruit(self, "vide", pygame.Vector2(21, 6)))
            self.objects.append(Fruit(self, "vide", pygame.Vector2(23, 4)))
            self.listAff = [self.player]
            self.listAff.extend(self.objects)
        elif level ==3:
            self.bg = pygame.image.load("Asset/Image/Fond_Level_3.png")
            self.x = 7
            self.y = 13
            self.arrosoir = Arrosoir(pygame.Vector2(21 + self.x, 0), self)
            self.composte_fraise = Composte("composte_fraise", pygame.Vector2(2 + self.x, 0), self)
            self.composte_carotte = Composte("composte_carotte", pygame.Vector2(4 + self.x, 0), self)
            self.composte_poire = Composte("composte_poire", pygame.Vector2(23 + self.x, 0), self)
            self.objects.append(self.arrosoir)
            self.objects.append(self.composte_fraise)
            self.objects.append(self.composte_carotte)
            self.objects.append(self.composte_poire)
            self.objects.append(Boite(pygame.Vector2(17 + self.x, 0), self))
            self.objects.append(Porte(self))

            for x in range(3):
                for y in range(3):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + 12, y + 1), self))
            for x in range(6):
                for y in range(2):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + 12, y + 4), self))
            for x in range(6):
                for y in range(2):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + 16, y + 6), self))
            self.objects.append(Obstacle("block", pygame.Vector2(11, 1), self))
            self.objects.append(Obstacle("block", pygame.Vector2(11, 2), self))
            for x in range(6):
                for y in range(2):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + 24, y + 9), self))
            for x in range(3):
                for y in range(4):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + 24, y + 11), self))
            for x in range(2):
                for y in range(3):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + 28, y + 6), self))
            for x in range(3):
                for y in range(3):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + 30, y + 5), self))
            self.objects.append(Obstacle("block", pygame.Vector2(33, 5), self))
            self.objects.append(Obstacle("block", pygame.Vector2(33, 6), self))
            for x in range(2):
                for y in range(5):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + 10, y + 8), self))
            for x in range(4):
                for y in range(2):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + 11, y + 11), self))
            self.objects.append(Obstacle("block", pygame.Vector2(13, 13), self))
            self.objects.append(Obstacle("block", pygame.Vector2(14, 13), self))
            self.objects.append(Obstacle("block", pygame.Vector2(13, 14), self))
            for x in range(3):
                for y in range(4):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + 14, y + 14), self))
            for x in range(2):
                for y in range(2):
                    self.objects.append(Obstacle("block", pygame.Vector2(x + 12, y + 16), self))
            self.spawn_fruit(pygame.Vector2(29, 11))
            self.spawn_fruit(pygame.Vector2(32, 14))
            self.spawn_fruit(pygame.Vector2(11, 14))
            self.spawn_fruit(pygame.Vector2(8, 16))
            self.spawn_fruit(pygame.Vector2(9, 3))
            self.spawn_fruit(pygame.Vector2(27, 3))
            self.spawn_fruit(pygame.Vector2(32, 1))
            self.objects.append(Fruit(self, "vide", pygame.Vector2(18, 10)))
            self.objects.append(Fruit(self, "vide", pygame.Vector2(22, 11)))
            self.objects.append(Obstacle("buisson", pygame.Vector2(16, 1), self))
            self.objects.append(Obstacle("buisson", pygame.Vector2(19, 16), self))
            self.objects.append(Obstacle("rocher_1", pygame.Vector2(34, 7), self))
            self.objects.append(Obstacle("rocher_2", pygame.Vector2(15, 9), self))
            self.objects.append(Obstacle("rocher_2", pygame.Vector2(28, 13), self))
            self.objects.append(Obstacle("rocher_3", pygame.Vector2(24, 4), self))
            self.listAff = [self.player]
            self.listAff.extend(self.objects)

    def is_moving(self):
        if self.pressed.get(pygame.K_RIGHT) or self.pressed.get(pygame.K_LEFT) or self.pressed.get(pygame.K_UP) or self.pressed.get(pygame.K_DOWN):
            # if not self.music.channel_back_noise.get_busy():
            #     self.music.noise = 'Asset/musique/bruitage/marche.mp3'
            #     self.music.back_noise = pygame.mixer.Sound(self.music.noise)
            #     self.music.channel_back_noise.play(self.music.back_noise)
            return True
        else:
            # self.music.channel_back_noise.stop()
            return False

    def fin_fruits(self):
        if self.player.hold == ():
            for obj in self.objects:
                if obj.name in ["fraise", "carotte", "poire"]:
                    return False
            return True

    def bar(self):
        # bar fatigue
        pygame.draw.rect(self.screen, (255, 255, 255),
                         [40, 100 + 508 - self.player.fatigue , 20, self.player.fatigue], 0)
        pygame.draw.rect(self.screen, (255, 255, 255), [40, 100, 20, 508], 1)
        # bar voisin
        pygame.draw.rect(self.screen, (255, 255, 255),
                         [200, 40, self.voisinJauge * 7, 20], 0)
        pygame.draw.rect(self.screen, (255, 255, 255), [200, 40, 700, 20], 1)

    def game_over(self):
        self.music.channel_back_music.stop()
        self.music.back_music = pygame.mixer.Sound('Asset/musique/défaite.mp3')
        self.music.channel_back_music.play(self.music.back_music)
        self.is_over = True
        self.is_playing = False

    def random_placement(self, x, y):
        tuile = 1
        for obj in self.objects:
            if obj.name in ["composte_fraise", "composte_carotte", "composte_poire", "arrosoir"]:
                while tuile != 0:
                    i = random.randint(2+x, 40-x)
                    j = random.randint(2, 30-y)
                    tuile = self.grille.grille[i][j]
                obj.move(pygame.Vector2(i, j))
                tuile = 1

    def attempt_end(self):
        if self.fin_fruits():
            # Musique de victoire
            self.music.channel_back_music.stop()
            self.music.back_music = pygame.mixer.Sound('Asset/musique/victoire.mp3')
            self.music.channel_back_music.play(self.music.back_music)
            ###
            self.is_ended = True
            self.is_playing = False

    def pleure(self):
        for obj in self.objects:
            if obj.name in ["fraise", "carotte", "poire"]:
                if obj.event.need != "nothing":
                    if not self.music.channel_pleure.get_busy():
                        self.music.channel_pleure.play(self.music.pleure)
                    self.voisinJauge +=0.02
        else:
            return False

    def voisin(self):
        if self.pleure():
            self.voisinJauge += 0.01
        if self.voisinJauge > 100:
            self.game_over()

    def interract(self):
        for obj in self.objects:
            if obj.name in ["block","barriere","buisson","rocher_1","rocher_2", "rocher_3"]:
                pass
            elif obj.name == "porte":
                if self.player.dir == "up":
                    if obj.rect.x + self.camera.x + 48 <= self.player.rectEcran.x + 36 <= obj.rect.x + self.camera.x + 96:
                        if obj.rect.y + self.camera.y + 48 <= self.player.rectEcran.y + 50 <= obj.rect.y + self.camera.y + 96:
                            obj.actionPorte()
            elif obj.name == "boite":
                if self.player.dir == "right":
                    if obj.rect.x + self.camera.x + 48 <= self.player.rectEcran.x + 72 <= obj.rect.x + self.camera.x + 144:
                        if obj.rect.y + self.camera.y + 48 <= self.player.rectEcran.y + 72 <= obj.rect.y + self.camera.y + 96:
                            obj.actionBoite()
                if self.player.dir == "left":
                    if obj.rect.x + self.camera.x + 48 <= self.player.rectEcran.x <= obj.rect.x + self.camera.x + 148:
                        if obj.rect.y + self.camera.y + 48 <= self.player.rectEcran.y + 72 <= obj.rect.y + self.camera.y + 96:
                            obj.actionBoite()
                if self.player.dir == "up":
                    if obj.rect.x + self.camera.x + 48 <= self.player.rectEcran.x + 36 <= obj.rect.x + self.camera.x + 148:
                        if obj.rect.y + self.camera.y + 48 <= self.player.rectEcran.y + 68 <= obj.rect.y + self.camera.y + 96:
                            obj.actionBoite()
                if self.player.dir == "down":
                    if obj.rect.x + self.camera.x + 48 <= self.player.rectEcran.x + 36 <= obj.rect.x + self.camera.x + 148:
                        if obj.rect.y + self.camera.y + 48 <= self.player.rectEcran.y + 96 <= obj.rect.y + self.camera.y + 96:
                            obj.actionBoite()
            elif not obj.hold:
                if self.player.dir == "right":
                    if obj.rect.x + self.camera.x + 48 <= self.player.rectEcran.x + 72 <= obj.rect.x + self.camera.x + 96:
                        if obj.rect.y + self.camera.y + 48 <= self.player.rectEcran.y + 72 <= obj.rect.y + self.camera.y + 96:
                            if obj.name in ["fraise", "carotte", "poire", "vide"]:
                                obj.actionFruit()
                            elif self.player.hold != obj:
                                if self.player.hold != ():
                                    if self.player.hold.name not in ["fraise", "carotte", "poire"]:
                                        self.screen.blit(self.key_f,
                                                         (self.player.rectEcran.x + 4, self.player.rectEcran.y - 80))
                                        if self.pressed.get(pygame.K_f):
                                            self.player.prendre(obj)
                                else:
                                    self.screen.blit(self.key_f,
                                                     (self.player.rectEcran.x + 4, self.player.rectEcran.y - 80))
                                    if self.pressed.get(pygame.K_f):
                                        self.player.prendre(obj)
                if self.player.dir == "left":
                    if obj.rect.x + self.camera.x + 48 <= self.player.rectEcran.x <= obj.rect.x + self.camera.x + 96:
                        if obj.rect.y + self.camera.y + 48 <= self.player.rectEcran.y + 72 <= obj.rect.y + self.camera.y + 96:
                            if obj.name in ["fraise", "carotte", "poire", "vide"]:
                                obj.actionFruit()
                            elif self.player.hold != obj:
                                if self.player.hold != ():
                                    if self.player.hold.name not in ["fraise", "carotte", "poire"]:
                                        self.screen.blit(self.key_f,
                                                         (self.player.rectEcran.x + 4, self.player.rectEcran.y - 80))
                                        if self.pressed.get(pygame.K_f):
                                            self.player.prendre(obj)
                                else:
                                    self.screen.blit(self.key_f,
                                                     (self.player.rectEcran.x + 4, self.player.rectEcran.y - 80))
                                    if self.pressed.get(pygame.K_f):
                                        self.player.prendre(obj)
                if self.player.dir == "up":
                    if obj.rect.x + self.camera.x + 48 <= self.player.rectEcran.x + 36 <= obj.rect.x + self.camera.x + 96:
                        if obj.rect.y + self.camera.y + 48 <= self.player.rectEcran.y + 68 <= obj.rect.y + self.camera.y + 96:
                            if obj.name in ["fraise", "carotte", "poire", "vide"]:
                                obj.actionFruit()
                            elif self.player.hold != obj:
                                if self.player.hold != ():
                                    if self.player.hold.name not in ["fraise", "carotte", "poire"]:
                                        self.screen.blit(self.key_f,
                                                         (self.player.rectEcran.x + 4, self.player.rectEcran.y - 80))
                                        if self.pressed.get(pygame.K_f):
                                            self.player.prendre(obj)
                                else:
                                    self.screen.blit(self.key_f,
                                                     (self.player.rectEcran.x + 4, self.player.rectEcran.y - 80))
                                    if self.pressed.get(pygame.K_f):
                                        self.player.prendre(obj)
                if self.player.dir == "down":
                    if obj.rect.x + self.camera.x + 48 <= self.player.rectEcran.x + 36 <= obj.rect.x + self.camera.x + 96:
                        if obj.rect.y + self.camera.y + 48 <= self.player.rectEcran.y + 96 <= obj.rect.y + self.camera.y + 96:
                            if obj.name in ["fraise", "carotte", "poire", "vide"]:
                                obj.actionFruit()
                            elif self.player.hold != obj:
                                if self.player.hold != ():
                                    if self.player.hold.name not in ["fraise", "carotte", "poire"]:
                                        self.screen.blit(self.key_f,
                                                         (self.player.rectEcran.x + 4, self.player.rectEcran.y - 80))
                                        if self.pressed.get(pygame.K_f):
                                            self.player.prendre(obj)
                                else:
                                    self.screen.blit(self.key_f,
                                                     (self.player.rectEcran.x + 4, self.player.rectEcran.y - 80))
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
        self.screen.blit(self.bg, (self.background.x + self.camera.x, self.background.y + self.camera.y))
        self.listAff.sort(key=lambda x: float(x.y))
        for obj in self.listAff:
            obj.affiche()

    def update(self, screen):
        # vérifier déplacements
        if self.sleep:
            if self.player.fatigue > 0:
                self.player.fatigue -= 0.5
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.zzz, (1024 / 2 - 50, 768 / 2 - 270))
            if self.pressed.get(pygame.K_g):
                # sort de la maison
                self.music.noise = 'Asset/musique/bruitage/Porte_maison.mp3'
                self.music.channel_back_noise.play(self.music.back_noise)
                self.music.channel_back_music.stop()
                self.music.back_music = pygame.mixer.Sound('Asset/musique/Musique de fond.mp3')
                self.music.channel_back_music.play(self.music.back_music, 50)
                ##
                self.sleep = False
        else:
            if self.pressed.get(pygame.K_RIGHT):
                if self.block("right") and self.camera.x >= (-2016 / 2) + 336:
                    self.player.move_right()
                self.player.dir = "right"
            if self.pressed.get(pygame.K_LEFT):
                if self.block("left") and self.camera.x <= (2016 / 2) - 48 - 336:
                    self.player.move_left()
                self.player.dir = "left"
            if self.pressed.get(pygame.K_UP):
                if self.block("up") and self.camera.y <= 0:
                    self.player.move_up()
                self.player.dir = "up"
            if self.pressed.get(pygame.K_DOWN):
                if self.block("down") and self.camera.y >= (-1536) + 72 + 650:
                    self.player.move_down()
                self.player.dir = "down"
            if self.pressed.get(pygame.K_r):
                self.player.place()
            if self.pressed.get(pygame.K_b):
                self.is_ended = True
                self.is_playing = False
            self.affiche()
            self.player.holding()
            self.interract()
            self.player.vision()
        for obj in self.objects:
            if obj.name in ["fraise", "carotte", "poire"]:
                obj.murir()
        self.attempt_end()
        self.voisin()
        self.bar()
