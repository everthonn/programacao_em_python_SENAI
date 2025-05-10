import pygame
#PONG

pygame.init()
janela = pygame.display.set_mode([1500,500])

branco = (255,255,255)
preto = (0,0,0)

#posicionamento inicial das raquetes
raquete1_x, raquete1_y = 50, 225
raquete2_x, raquete2_y = 1450, 225

bola_x, bola_y = 750,220

velocidade_raquete =5 
velocidade_bola_x,velocidade_bola_y = 0.7,0.7

raquete_largura, raquete_altura = 20,100
bola_largura, bola_altura = 20,20

placar_1 = 0
placar_2 = 0

font = pygame.font.SysFont(None,55)

def desenhar():
    janela.fill(branco)
    pygame.draw.rect(janela, preto,(raquete1_x,raquete1_y,raquete_largura,raquete_altura))
    pygame.draw.rect(janela, preto,(raquete2_x, raquete2_y, raquete_largura,raquete_altura))
    pygame.draw.ellipse(janela, preto,(bola_x, bola_y, bola_largura, bola_altura))

    placar_texto = font.render(f"{placar_1} | {placar_2}", True, preto)

    janela.blit(placar_texto, (200,20))

loop = True

while loop:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            loop = False

#movimentação raquetes

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and raquete1_y > 0:
        raquete1_y -= velocidade_raquete 
    if keys[pygame.K_s] and raquete1_y < 1500:
        raquete1_y += velocidade_raquete


    if keys[pygame.K_UP] and raquete2_y > 0:
        raquete2_y -= velocidade_raquete 
    if keys[pygame.K_DOWN] and raquete2_y < 500:
        raquete2_y += velocidade_raquete 

#vlocidade da bola

    bola_x += velocidade_bola_x
    bola_y -= velocidade_bola_y

#bola n sair da tela por cima

    if bola_y <= 0 or bola_y >= 498 - bola_altura:
        velocidade_bola_y = -velocidade_bola_y

# colisão
    
    if (raquete1_x < bola_x <raquete1_x + raquete_largura) and (raquete1_y < bola_y < raquete1_y +raquete_altura ):
        velocidade_bola_x = -velocidade_bola_x

    if (raquete2_x < bola_x <raquete2_x + raquete_largura) and (raquete2_y < bola_y < raquete2_y +raquete_altura ):
        velocidade_bola_x = -velocidade_bola_x

    if (bola_x <= 0):
        placar_2 +=1
        bola_x,bola_y = 750,250

    if bola_x >=1500:
        placar_1 += 1
        bola_x,bola_y = 750,250

    desenhar()

    pygame.display.update()





