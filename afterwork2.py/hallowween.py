import pygame

pygame.init()

screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("halloween face !")

x = 275
y = 175
speed = 5

running = True

while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x =x - speed

    
    if keys[pygame.K_RIGHT]:
        x =x + speed

    
    if keys[pygame.K_UP]:
        y =y - speed

    
    if keys[pygame.K_DOWN]:
        y =y + speed

    pygame.draw.circle(screen, (255,140,0),(x,y),50)

    pygame.draw.circle(screen, (0,0,0),(x-18,y-10),7)
    pygame.draw.circle(screen, (0,0,0),(x+18,y+10),7)

    pygame.draw.arc(screen,(0,0,0),(x-20,y,40,25),3.14, 6.28,4)

    pygame.display.update()

pygame.quit()





