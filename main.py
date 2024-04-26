import pygame
from sys import exit

pygame.init()
screen_1 = pygame.display.set_mode((800,400))
pygame.display.set_caption('starwok')
clock = pygame.time.Clock()
test_font = pygame.font.Font( None , 50)
#no means no font type , doesnt look good colour with none


sky_Surface = pygame.image.load('image sky.jpg')
ground_surface = pygame.image.load('ground image.webp')
text_surface = test_font.render('enter the space wok ', False , 'green')
pixel_surface = pygame.image.load('Pictures/pixel-man.png')
pixel_x_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen_1.blit(ground_surface,(0,0))
    screen_1.blit(sky_Surface,(0,300))
    screen_1.blit(text_surface, (300,50))
    screen_1.blit(pixel_surface,(pixel_x_pos , 250))
    



    pygame.display.update()
    clock.tick(60)





