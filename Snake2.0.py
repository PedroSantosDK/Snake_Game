#importacão das bibliotecas
#teste
import pygame as pg
from pygame.locals import *
from sys import exit
from random import randint, shuffle
import os 

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, "imagens")
diretorio_sons = os.path.join(diretorio_principal, "sons")

#iniciando o pygame

white= (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

snake_colors = []
snake_colors.append(white)
snake_colors.append(black)
snake_colors.append(red)
snake_colors.append(green)
snake_colors.append(blue)

pg.init()

fim_jogo = False
game_pause = False
inical = False

#dimensões da janela
largura = 640
altura = 480

#paleta de cores

#velocidade da cobra
velocidade = 5
x_cobra = largura/2
y_cobra = altura/2

x_controle = velocidade
y_controle = 0

#criando uma randomizacão nas posicoes da maça
x_maca = randint(40,600)
y_maca = randint(50, 430)

#definindo a cobra
lista_cobra = []
comprimento_inicial = 3

#condição de morte
morreu = False

bt_scale = (50*3, 30*2)

#importando as imagens e sons 
aplee_image = pg.image.load(r"E:\Pedro\git\Snake_Game\imagens\aplee.png")

menu_logo = pg.image.load(r"E:\Pedro\git\Snake_Game\imagens\menu_logo.png")
menu_logo = pg.transform.scale(menu_logo, (31*10, 31*10))
menu_logor = menu_logo.get_rect(center = (largura//2, 100))

pg.mixer_music.set_volume(0.20)
musica_fundo = pg.mixer_music.load(r"E:\Pedro\git\Snake_Game\sons\THE GOLDEN MANSION.wav")

comendo = pg.mixer.Sound(r"E:\Pedro\git\Snake_Game\sons\coin.wav")
comendo.set_volume(10.0)

game_over = pg.mixer.Sound(r"E:\Pedro\git\Snake_Game\sons\game_over_1.mp3")
game_over.set_volume(10)

menu = pg.mixer.Sound(r"E:\Pedro\git\Snake_Game\sons\menu song.ogg")
pg.mixer_music.play(-1)
menu.set_volume(0.2)

pg.mixer_music.stop()

on_button_menu = pg.image.load(r"E:\Pedro\git\Snake_Game\imagens\botões\Button on.png")
on_button_menu = pg.transform.scale(on_button_menu, bt_scale)

bt_quit = pg.image.load(r"E:\Pedro\git\Snake_Game\imagens\botões\exit_button.png")
bt_quit = pg.transform.scale(bt_quit, (32*4, 12*4))
quit_rect = bt_quit.get_rect(center = (320, 420))

bt_play = pg.image.load(r"E:\Pedro\git\Snake_Game\imagens\botões\play_button.png")
bt_play = pg.transform.scale(bt_play, (32*5, 12*5))
play_rect = bt_play.get_rect(center = (320, 350))

#definindo os textos do jogo
fonte = pg.font.SysFont('arial', 40, True, True)
pontos = 0
fonte2 = pg.font.SysFont('arial', 20, True, True)   

fonte_menu = pg.font.SysFont('arial', 70, True, True)
mensagem_menu = 'Menu'
mensagem_menuf = fonte_menu.render(mensagem_menu, False, (0,0,0))

fonte_menu2 = pg.font.SysFont('arial', 70, True, True)
mensagem_menu2 = 'Menu'
mensagem_menu2f = fonte_menu2.render(mensagem_menu2, False, (50,50,50))

#convertendo a variavel velocidade, para não dar erro
vel = velocidade

#criando a janela, definindo o titulo dela e setando uma espera de tempo para atualizar o jogo
tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('Snake Game')
relogio = pg.time.Clock()

#acrescentando tamanho a cobra
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pg.draw.rect(tela, snake_colors[0],(XeY[0],XeY[1],20,20))

#replay do jogo. caso  derrota, reinicia os valores de pontuacão, velocidade, tamanho da cobra e redefinicão na variavel morreu
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cabeca, lista_cobra, x_maca, y_maca, velocidade, vel, morreu
    velocidade = 5
    pontos = 0
    vel = velocidade
    comprimento_inicial = 3
    x_cobra = largura/2
    y_cobra = altura/2
    lista_cabeca = []
    lista_cobra = []
    x_maca = randint(40,600)
    y_maca = randint(50,430)
    morreu = False
    pg.mixer_music.play(-1)

#importando e carregando imagens para o programa
image = pg.image.load(r"E:\Pedro\git\Snake_Game\imagens\Grass.png").convert()
image = pg.transform.scale(image, (largura, altura))

#loop principal
while inical != True:
    tela.fill((255,0,255))
    pg.mouse.set_visible(True)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == MOUSEBUTTONDOWN:
            pg.mouse.get_pos()

            if quit_rect.collidepoint(event.pos):
                pg.quit()
                exit()

            if play_rect.collidepoint(event.pos):
                inical = not inical

    tela.blit(menu_logo, menu_logor)
    tela.blit(bt_quit, quit_rect)
    tela.blit(bt_play, play_rect)
    pg.display.flip()

else:
    pg.mixer_music.play(-1)
    while not fim_jogo:

        if not game_pause:
            menu.stop()
            pg.mouse.set_visible(False)

    #exibindo os textos criados, pintado a tela e criando a condição para sair do jogo
            relogio.tick(30)
            tela.fill(white)
            mensagem = f'Pontos: {pontos}'
            texto_formatado2 = fonte.render(mensagem, False, black)

            mensagem2 = f'Velocidade: {vel}'
            texto_formatado3 = fonte.render(mensagem2, False, (0,0,75))

            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    exit()        

                #leitura de teclas clicadas no jogo
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        game_pause = not game_pause

                    if event.key == K_a:
                        if x_controle == velocidade:
                            pass
                        else:
                            x_controle = -velocidade
                            y_controle = 0
                    if event.key == K_d:
                        if x_controle == +velocidade:
                            pass
                        else:
                            x_controle = velocidade
                            y_controle = 0 
                    if event.key == K_w:
                        if y_controle == velocidade:
                            pass
                        else:
                            y_controle = -velocidade
                            x_controle = 0
                    if event.key == K_s:
                        if y_controle == -velocidade:
                            pass
                        else:
                            y_controle = velocidade
                            x_controle = 0
                    if event.key == K_LEFT:
                        if x_controle == velocidade:
                            pass
                        else:
                            x_controle = -velocidade
                            y_controle = 0
                    if event.key == K_RIGHT:
                        if x_controle == +velocidade:
                            pass
                        else:
                            x_controle = velocidade
                            y_controle = 0 
                    if event.key == K_UP:
                        if y_controle == velocidade:
                            pass
                        else:
                            y_controle = -velocidade
                            x_controle = 0
                    if event.key == K_DOWN:
                        if y_controle == -velocidade:
                            pass
                        else:
                            y_controle = velocidade
                            x_controle = 0

            #alocando a velocidade da cobra, de acordo com o controle pressionado
            x_cobra = x_cobra + x_controle
            y_cobra = y_cobra + y_controle

            #desenhando a maçã e a cobra na tela
            tela.blit(image, (0,0))
            cobra = pg.draw.rect(tela, snake_colors[0], (x_cobra, y_cobra, 20, 20))
            hitbox_maca = pg.draw.circle(tela, (0, 0, 0), [x_maca, y_maca], 11, 20)
            maca = aplee_image.get_rect(center = (x_maca, y_maca))

            #criando a colisão entre a maça e a cobra, aumentando o comprimento da cobra em 1 a cada colisão, e acrescentando 0.2 de velocidade a cada colisão
            if cobra.colliderect(hitbox_maca):
                shuffle(snake_colors)
                x_maca = randint (40, 600)
                y_maca = randint (50, 430)
                pontos = pontos + 1
                comprimento_inicial = comprimento_inicial + 1
                velocidade = velocidade + 0.2
                vel = round(velocidade)
                comendo.play()

            #defininco a parte inicial da cobra
            lista_cabeca = []
            lista_cabeca.append(x_cobra)
            lista_cabeca.append(y_cobra)

            lista_cobra.append(lista_cabeca)
            
            #condições que levam a game over: a cobra se encostar e/ou a cobra encostar nas bordas da tela
            if lista_cobra.count(lista_cabeca) > 1 or x_cobra > largura or x_cobra < 0 or y_cobra < 0 or y_cobra > altura:
                game_over.play()
                fonte3 = pg.font.SysFont('arial', 40, False, True)
                pg.mixer_music.stop()
                mensagem = 'GAME OVER!'
                texto_formatado = fonte3.render(mensagem, True, red)
                morreu = True
                while morreu:
                    tela.fill(black)
                    for event in pg.event.get():
                        if event.type == QUIT:
                            pg.quit()
                            exit()
                        if event.type == KEYDOWN:
                            if event.key == K_r:
                                reiniciar_jogo()
                    
                    tela.blit(texto_formatado, (200, 220))
                    pg.display.update()

            #limpando o excesso do corpo da cobra
            if len(lista_cobra) > comprimento_inicial:
                del lista_cobra[0]
            
            aumenta_cobra(lista_cobra)

            #printando os textos criados e atualizando a tela
            tela.blit(texto_formatado2, (430,15))
            tela.blit(texto_formatado3, (10,435))
            tela.blit(texto_timer, (230,30))
            tela.blit(aplee_image, maca)
        
        else:
            if game_pause:
                tela.fill((255,0,255))
                pg.mixer_music.stop()
                menu.play()
                pg.mouse.set_visible(True)
                button_menu = on_button_menu.get_rect(center = (320,300))

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        exit()

                    if event.type == MOUSEBUTTONDOWN:
                        pg.mouse.get_pos()
                        if button_menu.collidepoint(event.pos):
                            game_pause = not game_pause

            tela.blit(on_button_menu, button_menu)
            tela.blit(mensagem_menu2f, (230,30))
            tela.blit(mensagem_menuf, (225,25))

        pg.display.flip()