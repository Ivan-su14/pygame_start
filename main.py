import pygame
import sys
fps = 60
pygame.display.set_caption('Hello world')
pygame.init()

x=100
y=100
color= (123, 234, 234)

disp = pygame.display.set_mode((500, 500))
#pygame.display.update()
clock = pygame.time.Clock()



while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                x += 10
            elif event.button == 1:
                if x > 50:
                    x -= 10
    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 5
            elif event.key == pygame.K_RIGHT:
                x += 5
            elif event.key == pygame.K_UP:
                y -= 5
            elif event.key == pygame.K_DOWN:
                y += 5
            '''
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x -= 5
    if key[pygame.K_RIGHT]:
        x += 5

    press = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    if press[1]:
        pygame.draw.circle(disp, color, pos)
        disp.fill((0, 0, 0))
        pygame.display.update()

   # pygame.draw.rect(disp, (255, 245, 100), (50, 50, 100, 100), 5) #50-koordinati pryamougolnika, 100,100 razmer pryamougolnika
   # disp.fill((0, 0, 0))
    pygame.draw.circle(disp, color, (mouse_x, mouse_y), 50, 10) # 100,100-koord kruga


    pygame.display.update()