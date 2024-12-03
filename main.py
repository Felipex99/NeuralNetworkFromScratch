import pygame

pygame.init()
screen = pygame.display.set_mode((500,720),pygame.RESIZABLE)
clock = pygame.time.Clock()
playerPosition = pygame.Vector2(screen.get_width()/2,screen.get_height()/2)
playerPosition2 = pygame.Vector2(screen.get_width()/2,screen.get_height()/2)
menuPosition = pygame.Vector2(10,10)
menuPosition2 = pygame.Vector2(10,40)
fonte = pygame.font.Font(None,40)
running = True
radius = 30
delta = 63
velocidade = 6
textoPosicao1 = ""
textoPosicao2 = ""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    textoPosicao1 = f"Posição x1: {playerPosition.x} Posição y1: {playerPosition.y}"
    textoPosicao2 = f"Posição x2: {playerPosition2.x} Posição y2: {playerPosition2.y}"
    textSurface1 = fonte.render(textoPosicao1,True,"white","red")
    textSurface2 = fonte.render(textoPosicao2,True,"white","blue")
    pygame.draw.circle(screen, "black",playerPosition,radius+2)
    pygame.draw.circle(screen, "red",playerPosition,radius)

    direction = playerPosition-playerPosition2
    distance = direction.length()
    if distance>delta:
        direction = direction.normalize()
        playerPosition2+=direction*1.35*velocidade

    pygame.draw.circle(screen, "black",playerPosition2,radius+2)
    pygame.draw.circle(screen, "blue",playerPosition2,radius)

    print(playerPosition)
    screen.blit(textSurface1, menuPosition)
    screen.blit(textSurface2, menuPosition2)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] | keys[pygame.K_UP]:
        playerPosition.y -= velocidade 
    if keys[pygame.K_s] | keys[pygame.K_DOWN]:
        playerPosition.y += velocidade
    if keys[pygame.K_d]|keys[pygame.K_RIGHT]:
        playerPosition.x += velocidade
    if keys[pygame.K_a] | keys[pygame.K_LEFT]:
        playerPosition.x -= velocidade
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()