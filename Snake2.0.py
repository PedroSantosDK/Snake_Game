#importacão das bibliotecas
#teste
import pygame as pg
from pygame.locals import *
from sys import exit
from random import randint, shuffle
import os 
from Text_Maker import MyGameText

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, "imagens")
diretorio_sons = os.path.join(diretorio_principal, "sons")

#iniciando o pygame

play_buttons = []
play_index1 = 0
play_index2 = 1

quit_buttons = []
quit_index1 = 0
quit_index2 = 1

return_buttons = []
return_index1 = 0
return_index2 = 1

white = (255,255,255)
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

#dimensões da janela
largura = 640
altura = 480

tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('Snake Game')
relogio = pg.time.Clock()

mgt = MyGameText()

re_match_text = mgt.create_text("Presione 'R' para reiniciar", 15, (255,0,0))

fim_jogo = False
game_pause = False
inical = False

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
aplee_image = pg.image.load(os.path.join(diretorio_imagens, "aplee.png"))

menu_logo = pg.image.load(os.path.join(diretorio_imagens, "menu_logo.png"))
menu_logo = pg.transform.scale(menu_logo, (31*10, 31*10))
menu_logor = menu_logo.get_rect(center = (largura//2, 100))

pg.mixer_music.set_volume(0.20)
musica_fundo = pg.mixer_music.load(os.path.join(diretorio_sons, "THE_GOLDEN_MANSION.wav"))

comendo = pg.mixer.Sound(os.path.join(diretorio_sons, "coin.wav"))
comendo.set_volume(10.0)

game_over = pg.mixer.Sound(os.path.join(diretorio_sons, "game_over_1.mp3"))
game_over.set_volume(10)

menu = pg.mixer.Sound(os.path.join(diretorio_sons, "menu_song.ogg"))
pg.mixer_music.play(-1)
menu.set_volume(0.2)

pg.mixer_music.stop()

bt_return = pg.image.load(os.path.join(diretorio_imagens, "return_button.png"))
bt_return = pg.transform.scale(bt_return, bt_scale)
return_rect = bt_return.get_rect(center = (320,300))

return_buttons.append(bt_return)
return_buttons.append(return_rect)

bt_return_hover = pg.image.load(os.path.join(diretorio_imagens, "return_button_hover.png"))
bt_return_hover = pg.transform.scale(bt_return_hover, bt_scale)
return_hover_rect = bt_return.get_rect(center = (320,300))

return_buttons.append(bt_return_hover)
return_buttons.append(return_hover_rect)

bt_quit = pg.image.load(os.path.join(diretorio_imagens, "exit_button.png"))
bt_quit = pg.transform.scale(bt_quit, (32*4, 12*4))
quit_rect = bt_quit.get_rect(center = (320, 420))

quit_buttons.append(bt_quit)
quit_buttons.append(quit_rect)

bt_quit_hover = pg.image.load(os.path.join(diretorio_imagens, "exit_button_hover.png"))
bt_quit_hover = pg.transform.scale(bt_quit_hover, (32*4, 12*4))
quit_hover_rect = bt_quit_hover.get_rect(center = (320, 420))

quit_buttons.append(bt_quit_hover)
quit_buttons.append(quit_hover_rect)

bt_play = pg.image.load(os.path.join(diretorio_imagens, "play_button.png"))
bt_play = pg.transform.scale(bt_play, (32*5, 12*5))
play_rect = bt_play.get_rect(center = (320, 350))

play_buttons.append(bt_play)
play_buttons.append(play_rect)

bt_play_hover = pg.image.load(os.path.join(diretorio_imagens, "play_button_hover.png"))
bt_play_hover = pg.transform.scale(bt_play_hover, (32*5, 12*5))
play_hover_rect = bt_play_hover.get_rect(center = (320, 350))

play_buttons.append(bt_play_hover)
play_buttons.append(play_hover_rect)

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

#acrescentando tamanho a cobra
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pg.draw.rect(tela, snake_colors[0],(XeY[0],XeY[1],20,20))

#replay do jogo. caso  derrota, reinicia os valores de pontuacão, velocidade, tamanho da cobra e redefinicão na variavel morreu
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cabeca, velocidade, vel, lista_cobra, x_maca, y_maca, morreu
    velocidade = 5
    vel = velocidade
    x_cobra = largura/2
    y_cobra = altura/2
    pontos = 0
    comprimento_inicial = 3
    lista_cabeca = []
    lista_cobra = []
    x_maca = randint(40,600)
    y_maca = randint(50,430)
    morreu = False
    pg.mixer_music.play(-1)

#importando e carregando imagens para o programa
image = pg.image.load(os.path.join(diretorio_imagens, "Grass.png")).convert()
image = pg.transform.scale(image, (largura, altura))

#loop principal
while inical != True:
    tela.fill((255,0,255))
    pg.mouse.set_visible(True)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == MOUSEMOTION:
            XeY = pg.mouse.get_pos()

            if play_rect.collidepoint(XeY[0], XeY[1]):
                play_index1 = 2
                play_index2 = 3
            else:
                play_index1 = 0
                play_index2 = 1

            if quit_rect.collidepoint(XeY[0], XeY[1]):
                quit_index1 = 2
                quit_index2 = 3
            else:
                quit_index1 = 0
                quit_index2 = 1


        if event.type == MOUSEBUTTONDOWN:
            pg.mouse.get_pos()

            if quit_rect.collidepoint(event.pos):
                pg.quit()
                exit()

            if play_rect.collidepoint(event.pos):
                inical = not inical

    tela.blit(menu_logo, menu_logor)
    tela.blit(quit_buttons[quit_index1], quit_buttons[quit_index2])
    tela.blit(play_buttons[play_index1], play_buttons[play_index2])
    pg.display.flip()

else:
    pg.mixer_music.play(-1)
    while not fim_jogo:

        if not game_pause:
            menu.stop()
            pg.mouse.set_visible(False)

    #exibindo os textos criados, pintado a tela e criando a condição para sair do jogo
            relogio.tick(30)
            print(f"velocidade: {velocidade}\nvel: {vel}")
            os.system("cls")
            tela.fill(white)


            text_points = mgt.create_text(f'Pontos: {pontos}', 35, (black))
            text_vel = mgt.create_text(f'Velocidade: {vel}', 25, (0,0,75))

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
                        if x_controle == -velocidade:
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

                    if event.key == K_RIGHT:
                        if x_controle == -velocidade:
                            pass
                        else:
                            x_controle = velocidade
                            y_controle = 0

                    if event.key == K_LEFT:
                        if x_controle == velocidade:
                            pass
                        else:
                            x_controle = -velocidade
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
                pg.mixer_music.stop()
                text_game_over = mgt.create_text('GAME OVER!', 40, red, 'arial')
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
                    
                    tela.blit(text_game_over, (200, 220))
                    tela.blit(re_match_text, (225, 260))
                    pg.display.update()

            #limpando o excesso do corpo da cobra
            if len(lista_cobra) > comprimento_inicial:
                del lista_cobra[0]
            
            aumenta_cobra(lista_cobra)

            #printando os textos criados e atualizando a tela
            tela.blit(text_points, (430,10))
            tela.blit(text_vel, (10,435))
            tela.blit(aplee_image, maca)
        
        else:
            if game_pause:
                tela.fill((255,0,255))
                pg.mixer_music.stop()
                menu.play()
                pg.mouse.set_visible(True)

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        exit()

                    if event.type == MOUSEMOTION:
                        XeY = pg.mouse.get_pos()

                        if return_rect.collidepoint(XeY[0], XeY[1]):
                            return_index1 = 2
                            return_index2 = 3
                        else:
                            return_index1 = 0
                            return_index2 = 1

                    if event.type == MOUSEBUTTONDOWN:
                        pg.mouse.get_pos()
                        if return_rect.collidepoint(event.pos):
                            game_pause = not game_pause

            tela.blit(return_buttons[return_index1], return_buttons[return_index2])
            tela.blit(mensagem_menu2f, (230,30))
            tela.blit(mensagem_menuf, (225,25))

        pg.display.flip()