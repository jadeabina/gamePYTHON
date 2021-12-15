import pygame
import os
import random



TELA_LARGURA = 48
TELA_ALTURA = 48

IMAGEM_MENU = pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_inicio_menu_game', 'menu.png'))))
IMAGEM_GAME_OVER = pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_game_over', 'Game_over.png'))))
IMAGENS_CENARIO = [
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'Layer-0.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile2.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile3.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile4.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile5.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile6.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile7.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile8.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile9.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile10.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile11.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile12.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile13.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile14.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile15.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile16.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile17.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile18.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile19.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile20.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile21.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile22.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile23.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile24.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile25.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile26.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile27.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile28.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile29.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile30.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile31.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile32.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile33.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile34.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile35.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile36.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile37.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile38.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile39.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile40.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile41.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile42.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile43.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile44.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile45.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile46.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile47.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile48.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile49.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile50.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile51.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile52.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile53.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile54.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile55.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile56.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile57.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile58.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile59.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile60.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile61.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile62.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile63.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile64.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile65.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile66.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile67.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile68.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile69.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile70.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile71.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile72.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile73.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile74.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile75.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile76.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile77.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile78.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile79.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile80.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile81.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile82.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile83.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile84.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile85.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile86.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile87.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile88.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1', 'tile89.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile90.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile91.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile92.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile93.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile94.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile95.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile96.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile97.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile98.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile99.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile100.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile101.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile102.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile103.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile104.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile105.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile106.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile107.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile108.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile109.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile110.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile111.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile112.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile113.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile114.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile115.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile116.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile117.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile118.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile119.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile120.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile121.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile122.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile123.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile124.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile125.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile126.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile127.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tiles1','tile128.png')))),


]
IMAGENS_PERSONAGEM1 = [
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_pers_principal3', 'StreamMan.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_pers_principal3', 'StreamMan_attack1.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_pers_principal3', 'StreamMan_attack2.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_pers_principal3', 'StreamMan_attack3.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_pers_principal3', 'StreamMan_death.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_pers_principal3', 'StreamMan_hurt.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_pers_principal3', 'StreamMan_idle.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_pers_principal3', 'StreamMan_jump.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_pers_principal3', 'StreamMan_run.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_pers_principal3', 'StreamMan_walk.png')))),
]
IMAGENS_INIMIGO1 = [
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_inimigo1', 'Centipede.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_inimigo1', 'Centipede_attack1.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_inimigo1', 'Centipede_attack2.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_inimigo1', 'Centipede_attack3.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_inimigo1', 'Centipede_death.png')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_inimigo1', 'Centipede_hurt.png')))),
]
IMAGENS_OBJSETOS_TILES = [
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),
    pygame.transform.scale2x(pygame.image.load((os.path.join('src/img_tile_objet', '')))),


]




pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial',40)#por morte de inimigo
FONTE_VIDA = pygame.font.SysFont('arial',40)#por porcentagem vida




class Personagem1:
    SRC= IMAGENS_PERSONAGEM1
    #PERSONAGEM01


class Cenario:
    SRC= IMAGENS_CENARIO
    #CENARIO


class Inimigo:
    SRC= IMAGENS_INIMIGO1
    #INIMIGO

class TileObjects:
    SRC=IMAGENS_OBJSETOS_TILES
    #OBJETOS DE TELA

class  GameOver:
    SRC= IMAGEM_GAME_OVER
    #GAME OVER




# tela de inicio



# tela de escolha de personagens

# movimentação de personagens

# iniciar jogo

# cenario1

# inimigo

# movimento de inimigo






























#def main():





#if __name__ == '__main__':
 #   main ()