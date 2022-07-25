import pygame
import sys
import random

fps = 60
pygame.display.set_caption('Hello world')
pygame.init()

x = 100
y = 100
a = random.randint(0, 500)
b = random.randint(0, 500)
color = (123, 234, 234)
color2 = (223, 14, 234)



disp = pygame.display.set_mode((600, 600))
# pygame.display.update()
clock = pygame.time.Clock()

while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
            elif event.key == pygame.K_RIGHT:
                x += 1
            elif event.key == pygame.K_UP:
                y -= 1
            elif event.key == pygame.K_DOWN:
                y += 1


    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x -= 1
    if key[pygame.K_RIGHT]:
        x += 1
    if key[pygame.K_UP]:
        y -= 1
    if key[pygame.K_DOWN]:
        y += 1


    if a+100 <= x and b+50 <= y:
        pygame.quit()
        sys.exit()


    if x >= a-100 and y >= b-50:
        pygame.quit()
        sys.exit()


    disp.fill((0, 0, 0))
    pygame.draw.rect(disp, color, (x, y, 100, 50), 5) #50-koordinati pryamougolnika, 100,50 razmer pryamougolnika

    pygame.draw.rect(disp, color2, (a, b, 100, 50), 5)
    pygame.display.update()