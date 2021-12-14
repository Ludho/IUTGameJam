import pygame



# Creation class du player
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.velocity = 8
        self.percent_max = 100
        self.fatigue = 1
        self.percent = 0
        self.image = pygame.image.load("Asset/Player/Idle/Player_Right_Front_Idle.png")
        self.rectEcran = self.image.get_rect()
        self.rectEcran.x = 1024 / 2
        self.rectEcran.y = 768 / 2
        self.hold = ()
        self.y = -self.game.camera.y -50
        self.case = pygame.Vector2((int((-self.game.camera.x + 984) / 48)), (int((-self.game.camera.y + 48) / 48)))
        self.dir = "down"
        self.left = False
        #images Pour Arrosoir
        self.RFPAimages = animations.get("Right_Front_PorteArrosoir_")
        self.LFPAimages = animations.get("Left_Front_PorteArrosoir_")
        #images Pour Composte Fraise
        self.LFPEFimages = animations.get("Left_Front_PorteEngraisFraise_")
        self.RFPEFimages = animations.get("Right_Front_PorteEngraisFraise_")
        #images Pour Composte Carotte
        self.LFPECimages = animations.get("Left_Front_PorteEngraisCarotte_")
        self.RFPECimages = animations.get("Right_Front_PorteEngraisCarotte_")
        #images Pour Composte Poire
        self.LFPEPimages = animations.get("Left_Front_PorteEngraisPoire_")
        self.RFPEPimages = animations.get("Right_Front_PorteEngraisPoire_")
        # images Pour BBB Fraise
        self.LFPBBFimages = animations.get("Left_Front_PorteBBFraise_")
        self.RFPBBFimages = animations.get("Right_Front_PorteBBFraise_")
        # images Pour BBB Carotte
        self.LFPBBCimages = animations.get("Left_Front_PorteBBCarotte_")
        self.RFPBBCimages = animations.get("Right_Front_PorteBBCarotte_")
        # images Pour BBB Poire
        self.LFPBBPimages = animations.get("Left_Front_PorteBBPoire_")
        self.RFPBBPimages = animations.get("Right_Front_PorteBBPoire_")
        # images Pour Fraise
        self.LFPFimages = animations.get("Left_Front_PorteFraise_")
        self.RFPFimages = animations.get("Right_Front_PorteFraise_")
        # images Pour Carotte
        self.LFPCimages = animations.get("Left_Front_PorteCarotte_")
        self.RFPCimages = animations.get("Right_Front_PorteCarotte_")
        # images Pour Poire
        self.LFPPimages = animations.get("Left_Front_PortePoire_")
        self.RFPPimages = animations.get("Right_Front_PortePoire_")
        #images déplacements
        self.RBimages = animations.get("Right_Back_Run_")
        self.LBimages = animations.get("Left_Back_Run_")
        self.RFimages = animations.get("Right_Front_Run_")
        self.LFimages = animations.get("Left_Front_Run_")


        self.RBPimages = animations.get("Right_Back_PorteQQC")
        self.LBPimages = animations.get("Left_Back_PorteQQC_")

        # self.LBimages = animations.get("Left_Back_Run_")
        # self.LFimages = animations.get("Left_Front_Run_")
        self.current_image = 0
        self.chargement_image = 0

    def vision(self):
        if self.percent < self.percent_max:
            self.percent +=10
        else:
                self.fatigue += 1   #if 400
                self.percent = 0
                if self.fatigue >= 508:
                    print("CHEH")
                    self.game.game_over()
        pygame.draw.circle(self.game.screen, (0, 0, 0), ((1024/2), (768/2)), 650, int(self.fatigue)+140)

    def move_right(self):
        self.game.camera.x -= self.velocity
        self.case = pygame.Vector2((int((-self.game.camera.x + 964) / 48)), (int((-self.game.camera.y + 28) / 48)))
        self.left = False

    def move_left(self):
        self.game.camera.x += self.velocity
        self.case = pygame.Vector2((int((-self.game.camera.x + 964) / 48)), (int((-self.game.camera.y + 28) / 48)))
        self.left = True

    def move_up(self):
        self.game.camera.y += self.velocity
        self.case = pygame.Vector2((int((-self.game.camera.x + 964) / 48)), (int((-self.game.camera.y + 28) / 48)))

    def move_down(self):
        self.game.camera.y -= self.velocity
        self.case = pygame.Vector2((int((-self.game.camera.x + 964) / 48)), (int((-self.game.camera.y + 28) / 48)))

    def prendre(self, obj):
        if obj.name == "arrosoir" and not self.game.music.channel_back_noise.get_busy():
            self.game.music.noise = 'Asset/musique/bruitage/arrosoire.mp3'
            self.game.music.back_noise = pygame.mixer.Sound(self.game.music.noise)
            self.game.music.channel_back_noise.play(self.game.music.back_noise)
        if self.hold != ():
            self.hold.hold = False
            self.hold.cases = obj.cases
            self.hold.rect = obj.rect
            self.hold = obj
            self.hold.cases = pygame.Vector2(-1, -1)
            self.hold.rect = pygame.Vector2(-10000, -10000)
        else:
            self.hold = obj
            self.game.grille.grille[int(self.hold.cases.x)][int(self.hold.cases.y)] = 0
            obj.hold = True
            self.hold.cases = pygame.Vector2(-1, -1)
            self.hold.rect = pygame.Vector2(-10000, -10000)


    def place(self):
        if self.hold != ():
            if self.hold.name in ["fraise", "carotte", "poire"]:
                pass
            elif self.game.grille.grille[int(self.case.x)][int(self.case.y)] == 0:
                self.hold.rect.x = self.game.grille.getCoord(self.case.x, self.case.y).x
                self.hold.rect.y = self.game.grille.getCoord(self.case.x, self.case.y).y
                self.hold.hold = False
                self.hold.cases = self.case
                self.game.grille.grille[int(self.case.x)][int(self.case.y)] = 1
                self.hold.y = self.case.y*48
                self.hold = ()

    def holding(self):
        # arrosoir
        if self.hold == self.game.arrosoir:
            if self.dir == "down":
                if self.left:
                    if self.game.is_moving():
                        self.animate(self.LFPAimages)
                    else :
                        self.image = pygame.image.load(get_image1_path("Left_Front_PorteArrosoir_"))
                else:
                    if self.game.is_moving():
                        self.animate(self.RFPAimages)
                    else :
                        self.image = pygame.image.load(get_image1_path("Right_Front_PorteArrosoir_"))
            if self.dir == "up":
                if self.left:
                    if self.game.is_moving():
                        self.animate(self.LBPimages)
                    else :
                        self.image = pygame.image.load(get_image1_path("Left_Back_PorteQQC_"))
                else:
                    if self.game.is_moving():
                        self.animate(self.RBPimages)
                    else :
                        self.image = pygame.image.load(get_image1_path("Right_Back_PorteQQC"))
            if self.dir == "right":
                if self.game.is_moving():
                    self.animate(self.RFPAimages)
                else:
                    self.image = pygame.image.load(get_image1_path("Right_Front_PorteArrosoir_"))
            if self.dir == "left":
                if self.game.is_moving():
                    self.animate(self.LFPAimages)
                else:
                    self.image = pygame.image.load(get_image1_path("Left_Front_PorteArrosoir_"))
        # composte fraise
        elif self.hold == self.game.composte_fraise:
            if self.dir == "down":
                if self.left:
                    if self.game.is_moving():
                        self.animate(self.LFPEFimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Left_Front_PorteEngraisFraise_"))
                else:
                    if self.game.is_moving():
                        self.animate(self.RFPEFimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Right_Front_PorteEngraisFraise_"))
            if self.dir == "up":
                if self.left:
                    if self.game.is_moving():
                        self.animate(self.LBPimages)
                    else :
                        self.image = pygame.image.load(get_image1_path("Left_Back_PorteQQC_"))
                else:
                    if self.game.is_moving():
                        self.animate(self.RBPimages)
                    else :
                        self.image = pygame.image.load(get_image1_path("Right_Back_PorteQQC"))
            if self.dir == "right":
                if self.game.is_moving():
                    self.animate(self.RFPEFimages)
                else:
                    self.image = pygame.image.load(get_image1_path("Right_Front_PorteEngraisFraise_"))
            if self.dir == "left":
                if self.game.is_moving():
                    self.animate(self.LFPEFimages)
                else:
                    self.image = pygame.image.load(get_image1_path("Left_Front_PorteEngraisFraise_"))
        # composte carotte
        elif self.hold == self.game.composte_carotte:
            if self.dir == "down":
                if self.left:
                    if self.game.is_moving():
                        self.animate(self.LFPECimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Left_Front_PorteEngraisCarotte_"))
                else:
                    if self.game.is_moving():
                        self.animate(self.RFPECimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Right_Front_PorteEngraisCarotte_"))
            if self.dir == "up":
                if self.left:
                    if self.game.is_moving():
                        self.animate(self.LBPimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Left_Back_PorteQQC_"))
                else:
                    if self.game.is_moving():
                        self.animate(self.RBPimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Right_Back_PorteQQC"))
            if self.dir == "right":
                if self.game.is_moving():
                    self.animate(self.RFPECimages)
                else:
                    self.image = pygame.image.load(get_image1_path("Right_Front_PorteEngraisCarotte_"))
            if self.dir == "left":
                if self.game.is_moving():
                    self.animate(self.LFPECimages)
                else:
                    self.image = pygame.image.load(get_image1_path("Left_Front_PorteEngraisCarotte_"))
        # composte poire
        elif self.hold == self.game.composte_poire:
            if self.dir == "down":
                if self.left:
                    if self.game.is_moving():
                        self.animate(self.LFPEPimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Left_Front_PorteEngraisPoire_"))
                else:
                    if self.game.is_moving():
                        self.animate(self.RFPEPimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Right_Front_PorteEngraisPoire_"))
            if self.dir == "up":
                if self.left:
                    if self.game.is_moving():
                        self.animate(self.LBPimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Left_Back_PorteQQC_"))
                else:
                    if self.game.is_moving():
                        self.animate(self.RBPimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Right_Back_PorteQQC"))
            if self.dir == "right":
                if self.game.is_moving():
                    self.animate(self.RFPEPimages)
                else:
                    self.image = pygame.image.load(get_image1_path("Right_Front_PorteEngraisPoire_"))
            if self.dir == "left":
                if self.game.is_moving():
                    self.animate(self.LFPEPimages)
                else:
                    self.image = pygame.image.load(get_image1_path("Left_Front_PorteEngraisPoire_"))

        elif self.hold == self.game.fraise:
            if self.dir == "down":
                if self.left:
                    if self.hold.croissance >= 100:
                        if self.game.is_moving():
                            self.animate(self.LFPFimages)
                        else:
                            self.image = pygame.image.load(get_image1_path("Left_Front_PorteFraise_"))
                    else:
                        if self.game.is_moving():
                            self.animate(self.LFPBBFimages)
                        else:
                            self.image = pygame.image.load(get_image1_path("Left_Front_PorteBBFraise_"))
                else:
                    if self.hold.croissance >= 100:
                        if self.game.is_moving():
                            self.animate(self.RFPFimages)
                        else:
                            self.image = pygame.image.load(get_image1_path("Right_Front_PorteFraise_"))
                    else:
                        if self.game.is_moving():
                            self.animate(self.RFPBBFimages)
                        else:
                            self.image = pygame.image.load(get_image1_path("Right_Front_PorteBBFraise_"))
            if self.dir == "up":
                if self.left:
                    if self.game.is_moving():
                        self.animate(self.LBPimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Left_Back_PorteQQC_"))
                else:
                    if self.game.is_moving():
                        self.animate(self.RBPimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Right_Back_PorteQQC"))
            if self.dir == "right":
                if self.hold.croissance >= 100:
                    if self.game.is_moving():
                        self.animate(self.RFPFimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Right_Front_PorteFraise_"))
                else:
                    if self.game.is_moving():
                        self.animate(self.RFPBBFimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Right_Front_PorteBBFraise_"))
            if self.dir == "left":
                if self.hold.croissance >= 100:
                    if self.game.is_moving():
                        self.animate(self.LFPFimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Left_Front_PorteFraise_"))
                else:
                    if self.game.is_moving():
                        self.animate(self.LFPBBFimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Left_Front_PorteBBFraise_"))

        elif self.hold == self.game.carotte:
            if self.dir == "down":
                if self.left:
                    if self.hold.croissance >= 100:
                        if self.game.is_moving():
                            self.animate(self.LFPCimages)
                        else:
                            self.image = pygame.image.load(get_image1_path("Left_Front_PorteCarotte_"))
                    else:
                        if self.game.is_moving():
                            self.animate(self.LFPBBCimages)
                        else:
                            self.image = pygame.image.load(get_image1_path("Left_Front_PorteBBCarotte_"))
                else:
                    if self.hold.croissance >= 100:
                        if self.game.is_moving():
                            self.animate(self.RFPCimages)
                        else:
                            self.image = pygame.image.load(get_image1_path("Right_Front_PorteCarotte_"))
                    else:
                        if self.game.is_moving():
                            self.animate(self.RFPBBCimages)
                        else:
                            self.image = pygame.image.load(get_image1_path("Right_Front_PorteBBCarotte_"))
            if self.dir == "up":
                if self.left:
                    if self.game.is_moving():
                        self.animate(self.LBPimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Left_Back_PorteQQC_"))
                else:
                    if self.game.is_moving():
                        self.animate(self.RBPimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Right_Back_PorteQQC"))
            if self.dir == "right":
                if self.hold.croissance >= 100:
                    if self.game.is_moving():
                        self.animate(self.RFPCimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Right_Front_PorteCarotte_"))
                else:
                    if self.game.is_moving():
                        self.animate(self.RFPBBCimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Right_Front_PorteBBCarotte_"))
            if self.dir == "left":
                if self.hold.croissance >= 100:
                    if self.game.is_moving():
                        self.animate(self.LFPCimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Left_Front_PorteCarotte_"))
                else:
                    if self.game.is_moving():
                        self.animate(self.LFPBBCimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Left_Front_PorteBBCarotte_"))

        elif self.hold == self.game.poire:
            if self.dir == "down":
                if self.left:
                    if self.hold.croissance >= 100:
                        if self.game.is_moving():
                            self.animate(self.LFPPimages)
                        else:
                            self.image = pygame.image.load(get_image1_path("Left_Front_PortePoire_"))
                    else:
                        if self.game.is_moving():
                            self.animate(self.LFPBBPimages)
                        else:
                            self.image = pygame.image.load(get_image1_path("Left_Front_PorteBBPoire_"))
                else:
                    if self.hold.croissance >= 100:
                        if self.game.is_moving():
                            self.animate(self.RFPPimages)
                        else:
                            self.image = pygame.image.load(get_image1_path("Right_Front_PortePoire_"))
                    else:
                        if self.game.is_moving():
                            self.animate(self.RFPBBPimages)
                        else:
                            self.image = pygame.image.load(get_image1_path("Right_Front_PorteBBPoire_"))
            if self.dir == "up":
                if self.left:
                    if self.game.is_moving():
                        self.animate(self.LBPimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Left_Back_PorteQQC_"))
                else:
                    if self.game.is_moving():
                        self.animate(self.RBPimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Right_Back_PorteQQC"))
            if self.dir == "right":
                if self.hold.croissance >= 100:
                    if self.game.is_moving():
                        self.animate(self.RFPPimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Right_Front_PortePoire_"))
                else:
                    if self.game.is_moving():
                        self.animate(self.RFPBBPimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Right_Front_PorteBBPoire_"))
            if self.dir == "left":
                if self.hold.croissance >= 100:
                    if self.game.is_moving():
                        self.animate(self.LFPPimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Left_Front_PortePoire_"))
                else:
                    if self.game.is_moving():
                        self.animate(self.LFPBBPimages)
                    else:
                        self.image = pygame.image.load(get_image1_path("Left_Front_PorteBBPoire_"))
        else:
            if self.dir == "down":
                if self.left:
                    if self.game.is_moving():
                        self.animate(self.LFimages)
                    else:
                        self.image = pygame.image.load("Asset/Player/Idle/Player_Left_Front_Idle.png")
                else:
                    if self.game.is_moving():
                        self.animate(self.RFimages)
                    else :
                        self.image = pygame.image.load("Asset/Player/Idle/Player_Right_Front_Idle.png")
            if self.dir == "up":
                if self.left:
                    if self.game.is_moving():
                        self.animate(self.LBimages)
                    else :
                        self.image = pygame.image.load("Asset/Player/Idle/Player_Left_Back_Idle.png")
                else:
                    if self.game.is_moving():
                        self.animate(self.RBimages)
                    else :
                        self.image = pygame.image.load("Asset/Player/Idle/Player_Right_Back_Idle.png")
            if self.dir == "right":
                if self.game.is_moving():
                    self.animate(self.RFimages)
                else:
                    self.image = pygame.image.load("Asset/Player/Idle/Player_Right_Front_Idle.png")
            if self.dir == "left":
                if self.game.is_moving():
                    self.animate(self.LFimages)
                else:
                    self.image = pygame.image.load("Asset/Player/Idle/Player_Left_Front_Idle.png")
        self.y = -self.game.camera.y + 470


    def affiche(self):
        self.game.screen.blit(self.game.player.image, (1024 / 2 -36, 768 / 2 -70))

    def animate(self, dir):
        self.chargement_image += 6
        if self.chargement_image >= 12:
            self.current_image += 1
            if self.current_image >= len(dir):
                # remettre l'anim au depart
                self.current_image = 0
            self.image = dir[self.current_image]
            self.chargement_image = 0

def get_image1_path(sprite_name):
    path = f"Asset/animation/Player/{sprite_name}/{sprite_name}"
    return path + str(1) + '.png'


def load_animation_images(sprite_name):
    #charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    #recuperer le chemin du dossier pour ce sprite
    path = f"Asset/animation/Player/{sprite_name}/{sprite_name}"
    #boucler sur chaque image dans ce dossier
    for num in range(1,11): #1ere et dernière image
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    #renvoyer contenu de la liste d'images
    return images

#definir un dictionnaire qui va contenir les images chargées de chaque sprite
animations = {
    'Right_Back_Run_': load_animation_images('Right_Back_Run_'),
    'Left_Back_Run_': load_animation_images('Left_Back_Run_'),
    'Right_Front_Run_': load_animation_images('Right_Front_Run_'),
    'Left_Front_Run_': load_animation_images('Left_Front_Run_'),
    ############
    'Right_Back_PorteQQC': load_animation_images('Right_Back_PorteQQC'),
    'Left_Back_PorteQQC_': load_animation_images('Left_Back_PorteQQC_'),
    ############
    'Right_Front_PorteArrosoir_': load_animation_images('Right_Front_PorteArrosoir_'),
    'Left_Front_PorteArrosoir_': load_animation_images('Left_Front_PorteArrosoir_'),
    ############
    'Left_Front_PorteEngraisFraise_': load_animation_images('Left_Front_PorteEngraisFraise_'),
    'Right_Front_PorteEngraisFraise_': load_animation_images('Right_Front_PorteEngraisFraise_'),
    #############
    'Left_Front_PorteEngraisCarotte_': load_animation_images('Left_Front_PorteEngraisCarotte_'),
    'Right_Front_PorteEngraisCarotte_': load_animation_images('Right_Front_PorteEngraisCarotte_'),
    #############
    'Left_Front_PorteEngraisPoire_': load_animation_images('Left_Front_PorteEngraisPoire_'),
    'Right_Front_PorteEngraisPoire_': load_animation_images('Right_Front_PorteEngraisPoire_'),
    #############
    'Left_Front_PorteBBFraise_': load_animation_images('Left_Front_PorteBBFraise_'),
    'Right_Front_PorteBBFraise_': load_animation_images('Right_Front_PorteBBFraise_'),
    #############
    'Left_Front_PorteBBPoire_': load_animation_images('Left_Front_PorteBBPoire_'),
    'Right_Front_PorteBBPoire_': load_animation_images('Right_Front_PorteBBPoire_'),
    #############
    'Left_Front_PorteBBCarotte_': load_animation_images('Left_Front_PorteBBCarotte_'),
    'Right_Front_PorteBBCarotte_': load_animation_images('Right_Front_PorteBBCarotte_'),
    #############
    'Left_Front_PorteFraise_': load_animation_images('Left_Front_PorteFraise_'),
    'Right_Front_PorteFraise_': load_animation_images('Right_Front_PorteFraise_'),
    #############
    'Left_Front_PortePoire_': load_animation_images('Left_Front_PortePoire_'),
    'Right_Front_PortePoire_': load_animation_images('Right_Front_PortePoire_'),
    #############
    'Left_Front_PorteCarotte_': load_animation_images('Left_Front_PorteCarotte_'),
    'Right_Front_PorteCarotte_': load_animation_images('Right_Front_PorteCarotte_')
}