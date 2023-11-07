import pygame

pygame.init()
police = pygame.font.SysFont("freesans",50)
nb_click = 0
nb_click_texte = police.render(str(nb_click), 1 ,(0,0,0))
hauteur = 800
largeur = 1000
screen = pygame.display.set_mode((largeur, hauteur))
titre = 0
background = pygame.Surface(screen.get_size())
CIEL = 0 , 200 ,255
cookie = pygame.image.load("png-clipart-cookie-cookie.png")

run = True
while run:
    background.fill(CIEL)
    screen.blit(background, (0,0))
    screen.blit(cookie, (hauteur//2 , largeur//2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
                nb_click = nb_click + 1
                nb_click_texte = police.render(str(nb_click), 1 ,(0,0,0))
            if pygame.mouse.get_pressed() == (0, 0, 1) :
                nb_click = nb_click - 1
                nb_click_texte = police.render(str(nb_click), 1 ,(0,0,0))
    screen.blit(nb_click_texte, (100 , 100))
    pygame.display.update()


pygame.quit()
quit()