import pygame
import math

from music import Music
from game import Game


# Initialisation de pygame
pygame.init()

#definir une clock
clock = pygame.time.Clock()
FPS = 60

# taille d'écran
BOX_WIDTH = 1024
BOX_HEIGHT = 768
screen = pygame.display.set_mode((BOX_WIDTH, BOX_HEIGHT))

# Titre + Icon(32px)
pygame.display.set_caption("Farmer's Strange Dreams")
icon = pygame.image.load("Asset/Image/Icon.png")
pygame.display.set_icon(icon)

#Music
pygame.mixer.init()
music = Music()

# Background
background = pygame.image.load("Asset/Menu/Main/Fond_Menu_V2.png")
background_rect = background.get_rect()
game = Game(screen, music)

music.channel_back_music.play(music.back_music)

# Importer bannière
# banner = pygame.image.load("Asset/Menu/Fond_Menu_V2.png")
# #banner = pygame.transform.scale(banner, (500, 500))
# banner_rect = banner.get_rect()
# #banner_rect.x = math.ceil(screen.get_width()/4)

# création boutons menus
play_button = pygame.image.load("Asset/Menu/Main/BtnPlay_V2.png")
#play_button = pygame.transform.scale(play_button, (450, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 4)
play_button_rect.y = math.ceil(screen.get_height() / 2.5)

htp_button = pygame.image.load("Asset/Menu/Main/BtnHowToPlay_V2.png")
# htp_button = pygame.transform.scale(htp_button, (200, 200))
htp_button_rect = htp_button.get_rect()
htp_button_rect.x = math.ceil(screen.get_width() / 6)
htp_button_rect.y = math.ceil(screen.get_height() / 1.6)

credit_button = pygame.image.load("Asset/Menu/Main/BtnCredit_V2.png")
# htp_button = pygame.transform.scale(htp_button, (200, 200))
credit_button_rect = credit_button.get_rect()
credit_button_rect.x = math.ceil(screen.get_width() / 2)
credit_button_rect.y = math.ceil(screen.get_height() / 1.6)

quit_button = pygame.image.load("Asset/Menu/Main/BtnQuit_V2.png")
# htp_button = pygame.transform.scale(htp_button, (200, 200))
quit_button_rect = quit_button.get_rect()
quit_button_rect.x = math.ceil(screen.get_width() / 3.33)
quit_button_rect.y = math.ceil(screen.get_height() / 1.3)

return_menu_button = pygame.image.load("Asset/Menu/BtnMenu_V4.png")
return_menu_button = pygame.transform.scale(return_menu_button, (240, 80))
return_menu_button_rect = return_menu_button.get_rect()
return_menu_button_rect.x = 10
return_menu_button_rect.y = math.ceil(screen.get_height() / 1.2)


# Game Loop
running = True
#choix Niveau Loop
level_selector = False

htp = False

credit = False

while running:

    # Background
    #screen.blit(background, (game.background.x + game.camera.x, game.background.y + game.camera.y))
    screen.blit(background, background_rect)

    #verifier si notre jeu a commencé ou non
    if game.is_playing:
        # screen.blit(game.fruit.image,  (game.fruit.rect.x + game.camera.x, game.fruit.rect.y + game.camera.y))
        game.update(screen)
    elif game.is_over:
        game_over_bg = pygame.image.load("Asset/Menu/GameOver_V2.png")
        game_over_bg_rect = game_over_bg.get_rect()
        screen.blit(game_over_bg,game_over_bg_rect)

        screen.blit(return_menu_button, return_menu_button_rect)

    elif game.is_ended:
        coor_bg = game.bg.get_rect()
        coor_bg.x = -1044
        coor_bg.y = -22
        screen.blit(game.bg, coor_bg)

        game_ended_bg = pygame.image.load("Asset/Menu/Victory/Victory_V2.png")
        game_ended_bg_rect = game_ended_bg.get_rect()
        screen.blit(game_ended_bg, game_ended_bg_rect)

        cadre_or = pygame.image.load("Asset/Menu/Victory/BtnOr_V2.png")
        cadre_or_rect = cadre_or.get_rect()
        cadre_or_rect.x = math.ceil(screen.get_width() / 1.5)
        cadre_or_rect.y = math.ceil(screen.get_height() / 2)

        cadre_argent = pygame.image.load("Asset/Menu/Victory/BtnArgent_V2.png")
        cadre_argent_rect = cadre_argent.get_rect()
        cadre_argent_rect.x = math.ceil(screen.get_width() / 3)
        cadre_argent_rect.y = math.ceil(screen.get_height() / 2)

        cadre_bronze = pygame.image.load("Asset/Menu/Victory/BtnBronze_V2.png")
        cadre_bronze_rect = cadre_bronze.get_rect()
        cadre_bronze_rect.x = 10
        cadre_bronze_rect.y = math.ceil(screen.get_height() / 2)

        cadre_score = pygame.image.load("Asset/Menu/Victory/BtnScore_V2.png")
        cadre_score_rect = cadre_score.get_rect()
        cadre_score_rect.x = math.ceil(screen.get_width() / 4)
        cadre_score_rect.y = math.ceil(screen.get_height() / 1.5)

        font = pygame.font.Font(None, 125)
        text = font.render(str(game.score),1,(120,88,61))

        font_or = pygame.font.Font(None, 90)
        text_or = font_or.render(str(300), 1, (120, 88, 61))

        font_argent = pygame.font.Font(None, 90)
        text_argent = font_argent.render(str(200), 1, (120, 88, 61))

        font_bronze = pygame.font.Font(None, 90)
        text_bronze = font_bronze.render(str(100), 1, (120, 88, 61))


        screen.blit(return_menu_button, return_menu_button_rect)
        screen.blit(cadre_score, cadre_score_rect)
        screen.blit(cadre_bronze, cadre_bronze_rect)
        screen.blit(cadre_argent, cadre_argent_rect)
        screen.blit(cadre_or, cadre_or_rect)
        screen.blit(text, (cadre_score_rect.x + 260, cadre_score_rect.y+45))
        screen.blit(text_bronze, (cadre_bronze_rect.x + 150, cadre_bronze_rect.y + 15))
        screen.blit(text_argent, (cadre_argent_rect.x + 150, cadre_argent_rect.y + 15))
        screen.blit(text_or, (cadre_or_rect.x + 150, cadre_or_rect.y + 15))

    elif level_selector:
        game = Game(screen, music)

        easy_button = pygame.image.load("Asset/Menu/Level_Select/BtnFacile_V2.png")
        # play_button = pygame.transform.scale(play_button, (450, 150))
        easy_button_rect = easy_button.get_rect()
        easy_button_rect.x = math.ceil(screen.get_width() / 3)
        easy_button_rect.y = math.ceil(screen.get_height() / 2.5)

        normal_button = pygame.image.load("Asset/Menu/Level_Select/BtnMoyen_V2.png")
        # play_button = pygame.transform.scale(play_button, (450, 150))
        normal_button_rect = normal_button.get_rect()
        normal_button_rect.x = math.ceil(screen.get_width() / 3)
        normal_button_rect.y = math.ceil(screen.get_height() / 1.7)

        hard_button = pygame.image.load("Asset/Menu/Level_Select/BtnDifficile_V2.png")
        # play_button = pygame.transform.scale(play_button, (450, 150))
        hard_button_rect = hard_button.get_rect()
        hard_button_rect.x = math.ceil(screen.get_width() / 3)
        hard_button_rect.y = math.ceil(screen.get_height() /1.3)



        screen.blit(easy_button, easy_button_rect)
        screen.blit(normal_button, normal_button_rect)
        screen.blit(hard_button, hard_button_rect)
        screen.blit(return_menu_button, return_menu_button_rect)

    elif htp:
        htp_image = pygame.image.load("Asset/Menu/HowToPlay_V2.png")
        # play_button = pygame.transform.scale(play_button, (450, 150))
        htp_image_rect = htp_image.get_rect()
        htp_image_rect.x = 10
        htp_image_rect.y = 10

        screen.blit(htp_image, htp_image_rect)
        screen.blit(return_menu_button, return_menu_button_rect)

    elif credit:
        credit_bg = pygame.image.load("Asset/Menu/Credit/FondSansTitre_V2.png")
        credit_bg_rect = credit_bg.get_rect()
        screen.blit(credit_bg, credit_bg_rect)

        image1 = pygame.image.load("Asset/Menu/Credit/Adam_V2.png")
        image1_rect = image1.get_rect()
        image1_rect.x = screen.get_width()/3

        image2 = pygame.image.load("Asset/Menu/Credit/Felix_V2.png")
        image2_rect = image2.get_rect()
        image2_rect.x = screen.get_width() / 3
        image2_rect.y = 180

        image3 = pygame.image.load("Asset/Menu/Credit/Ludwig_V2.png")
        image3_rect = image3.get_rect()
        image3_rect.x = screen.get_width() / 3
        image3_rect.y = 360

        image4 = pygame.image.load("Asset/Menu/Credit/Romain_V2.png")
        image4_rect = image4.get_rect()
        image4_rect.x = screen.get_width() / 3
        image4_rect.y = 540

        screen.blit(image1, image1_rect)
        screen.blit(image2, image2_rect)
        screen.blit(image3, image3_rect)
        screen.blit(image4, image4_rect)
        screen.blit(return_menu_button, return_menu_button_rect)

    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(htp_button, htp_button_rect)
        screen.blit(credit_button, credit_button_rect)
        screen.blit(quit_button, quit_button_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        # que l'évènement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            game.is_playing = False
            game.is_over = False
            game.is_ended = False
            pygame.quit()
            print("Fermeture du jeu")
            # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            if event.key == pygame.K_h:
                print(game.grille.grille)
                print(game.grille.getCoord(1,1))
                #print(game.grille.getCase(pygame.Vector2(96,0)))

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification pour savoir si la souris est en collision avec le bouton jouer
            # if play_button_rect.collidepoint(event.pos):
            #     #lancer le jeu
            #     if game.is_over:
            #         game.is_over = False
            #         print("over")
            #     elif game.is_ended:
            #         game.is_ended = False
            #         print("end")
            #     elif not level_selector:
            #         level_selector = True
            #     elif level_selector:
            #         print("lancer Lvl2")
            #         level_selector = False
            #     else :
            #         #game.is_playing = True
            #         print("play")
            # if play_buttonLvl3_rect.collidepoint(event.pos):
            #     print("lancer Lvl3")
            #     level_selector = False
            # if play_buttonLvl1_rect.collidepoint(event.pos):
            #     print("lancer Lvl1")
            #     game.init(1)
            #     game.is_playing = True
            #     level_selector = False
            if game.is_over :
                if return_menu_button_rect.collidepoint(event.pos):
                    game.is_over = False
                print("over")
            elif game.is_ended:
                if return_menu_button_rect.collidepoint(event.pos):
                    game.is_ended = False
                print("ended")
            elif level_selector:
                if easy_button_rect.collidepoint(event.pos):
                    print("level1")
                    game.init(1)
                    game.is_playing = True
                    level_selector = False
                if normal_button_rect.collidepoint(event.pos):
                    print("level2")
                    game.init(2)
                    game.is_playing = True
                    level_selector = False
                if hard_button_rect.collidepoint(event.pos):
                    print("level3")
                    game.init(3)
                    game.is_playing = True
                    level_selector = False
                if return_menu_button_rect.collidepoint(event.pos):
                    level_selector = False
            elif htp :
                if return_menu_button_rect.collidepoint(event.pos):
                    htp = False

            elif credit:
                if return_menu_button_rect.collidepoint(event.pos):
                    credit = False
            else:
                if play_button_rect.collidepoint(event.pos):
                    level_selector = True
                if quit_button_rect.collidepoint(event.pos):
                    running = False
                    game.is_playing = False
                    game.is_over = False
                    game.is_ended = False
                    pygame.quit()
                    print("Fermeture du jeu")
                if htp_button_rect.collidepoint(event.pos):
                    htp = True
                if credit_button_rect.collidepoint(event.pos):
                    credit = True


    # Fixer nombre de fps
    clock.tick(FPS)