import pygame
import sys
pygame.init()

black=(0, 0, 0)
green=(0, 255, 0)
yellow = (255, 255, 0)

posY_block = 150

posX_circle = 80
posY_circle = 150

circle_right = True
circle_top = True

Width = 800
Height = 400
fps = 60
pygame.display.set_caption('Pinpong')
screen = pygame.display.set_mode((Width, Height))

clock = pygame.time.Clock()
speed = 5

while True:
    clock.tick(fps)
    screen.fill(black)
    pr_key = pygame.key.get_pressed()
    if pr_key[pygame.K_UP]:
        if posY_block > 0:
            posY_block -= speed
    if pr_key[pygame.K_DOWN]:
        if posY_block + 100 < Height:
            posY_block += speed

    if posX_circle - 50 <= 0:
        circle_right = True

    if posY_circle - 50 <= 0:
        circle_top = False

    if posY_circle + 50 >= Height:
        circle_top = True

    if circle_right:
        posX_circle += speed
    else:
        posX_circle -= speed

    if circle_top:
        posY_circle -= speed
    else:
        posY_circle += speed

    if posY_block <= posY_circle <= posY_block + 100 and Width - 20 <= posX_circle + 50 <= Width:
        circle_right = False
    elif posX_circle + 50 > Width:
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen, green, (780, posY_block, 20, 100))
    pygame.draw.circle(screen, yellow, (posX_circle, posY_circle), 20)

    pygame.display.update()