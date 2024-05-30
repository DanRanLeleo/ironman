import pygame, random

pygame.init()
tamanho = (800,600)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
pygame.display.set_caption("Iron Man")
branco = (255,255,255)
preto = (0,0,0)
iron = pygame.image.load("assets/iron.png")
fundo = pygame.image.load("assets/fundo.png")
missel = pygame.image.load("assets/missile.png")
posicaoXPersona = 400
posicaoYPersona = 300
movimentoXPersona = 0
movimentoYPersona = 0
posicaoXMissel = 400
posicaoYMissel = -240
velocidadeMissel = 1
missileSound = pygame.mixer.Sound("assets/missile.wav")
pygame.mixer.Sound.play(missileSound)
fonte = pygame.font.SysFont("comicsans",14)
pygame.mixer.music.load("assets/ironsound.mp3")
pygame.mixer.music.play(-1)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            movimentoXPersona = 5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            movimentoXPersona = -5
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentoXPersona = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoXPersona = 0
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            movimentoYPersona = 5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            movimentoYPersona = -5
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            movimentoYPersona = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            movimentoYPersona = 0

        
    posicaoXPersona = posicaoXPersona + movimentoXPersona
    posicaoYPersona = posicaoYPersona + movimentoYPersona

    if posicaoXPersona >= 0 and posicaoXPersona <=800:
        posicaoXPersona < 10
    elif posicaoXPersona > 800:
        posicaoXPersona = 790
    if posicaoYPersona < 0 :
        posicaoYPersona < 10
    elif posicaoYPersona > 473 :
        posicaoYPersona = 463

    tela.fill(branco)
    tela.blit(fundo, (0,0))
    #pygame.draw.circle(tela, preto, (posicaoXPersona,posicaoYPersona), 40, 0)
    tela.blit( iron, (posicaoXPersona, posicaoYPersona))
    posicaoYMissel = posicaoYMissel + velocidadeMissel
    if posicaoYMissel > 600:
        posicaoYMissel = -240
        velocidadeMissel = velocidadeMissel + 1
        posicaoXMissel = random.randint(0,800)
    tela.blit( missel, (posicaoXMissel, posicaoYMissel))

    pygame.display.update()
    relogio.tick(60)