import pygame

pygame.init()

tela = pygame.display.set_mode((1280, 1024))
# tela.pygame.set_caption("Titulo")

run = True

while run == True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False
            quit()
        tela.fill("darkblue")
        pygame.display.flip()
pygame.quit()