import pygame

pygame.init()
 
screen_width, screen height = (900,900)

displaysurface = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("adding image and bg imgae")

background image = pygame.transform.scale(
    pygame.image.load("ninjaimage.png").convert(),
    (screen_width,screen_height)
)
cristiano = pygame.transform,scale(
    pygame.image.load("cristiano.jpg").convert_alpha(),(200,200))

cristiano_rect = cristiano_image.get_rect(center = (screen_width//2,screen_height//2 - 30))

    