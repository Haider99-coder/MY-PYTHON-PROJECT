import pygame
from sys import exit

pygame.init()
screen_1 = pygame.display.set_mode((800,400))
pygame.display.set_caption('starwok')
clock = pygame.time.Clock()
test_font = pygame.font.Font( None , 50)
#no means no font type , doesnt look good colour with none


sky_Surface = pygame.image.load('image sky.png').convert_alpha()
ground_surface = pygame.image.load('groundimage2.png').convert_alpha()
text_surface = test_font.render('FACE YOUR FAITH ! ', False , 'purple').convert_alpha()




pixel_surface = pygame.image.load('man4.png').convert_alpha()
pixel_rect = pixel_surface.get_rect(midbottom = (41,300))





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen_1.blit(sky_Surface,(0,0))
    screen_1.blit(ground_surface,(0,150))
    screen_1.blit(text_surface, (300,50))

    pixel_rect.x += 4
    if pixel_rect.right >= 800: pixel_rect.left = 100
    screen_1.blit(pixel_surface,pixel_rect)
    
   

    # this creates the movment of playin to o from riht to left contionously so the playe doesnt go off the screen



    pygame.display.update()
    clock.tick(60)








    





