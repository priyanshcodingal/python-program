import pygame

pygame.init()

window = pygame.display.set_mode((400,400))

window.fill((0,0,255))

red = (255,0,0)

pygame.draw.circle(window, red, (200,200),50)

pygame.draw.circle(window, red,(100,100),50,3)

pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()