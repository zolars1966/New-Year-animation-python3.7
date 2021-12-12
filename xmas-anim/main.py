import numpy as np
import pygame
import random
 
size = width, height = 1366, 768
fps = 60
minu = -max(height, width//2)
 
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.Font('SantasSleighFull Deluxe.ttf', 120)
textsurface = myfont.render('Some Text', True, (255, 0, 0))

snow_list = np.random.randint(0, max(width, height*2), (50, 2))
snow_list1 = np.random.randint(0, max(width, height*2), (50, 2))
snow_list2 = np.random.randint(0, max(width, height*2), (50, 2))
snow_list3 = np.random.randint(0, max(width, height*2), (50, 2))

while True:
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit("\033[31m\033[1mHappy New Year!\033[0m\033[34m")

    snow_list[:, 1] += 3
    snow_list1[:, 1] += 2
    snow_list2[:, 1] += 1
    snow_list3[:, 1] += 1
    snow_list[:, 0] += np.random.randint(-10, 10, (50))//10
    snow_list1[:, 0] += np.random.randint(-6, 6, (50))//6
    snow_list2[:, 0] += np.random.randint(-3, 3, (50))//3
    snow_list3[:, 0] += np.random.randint(-1, 1, (50))

    for i in range(len(snow_list)):
 
        pygame.draw.circle(screen, (255, 255, 255), snow_list[i], 4)
        pygame.draw.circle(screen, (200, 200, 200), snow_list1[i], 3)
        pygame.draw.circle(screen, (150, 150, 150), snow_list2[i], 2)
        pygame.draw.circle(screen, (100, 100, 100), snow_list2[i], 1)

        if snow_list[i][1] > height:
            snow_list[i][1] = random.randrange(minu, 0)
            snow_list[i][0] = random.randrange(0, width)
        if snow_list1[i][1] > height:
            snow_list1[i][1] = random.randrange(minu, 0)
            snow_list1[i][0] = random.randrange(0, width)
        if snow_list2[i][1] > height:
            snow_list2[i][1] = random.randrange(minu, 0)
            snow_list2[i][0] = random.randrange(0, width)
        if snow_list3[i][1] > height:
            snow_list3[i][1] = random.randrange(minu, 0)
            snow_list3[i][0] = random.randrange(0, width)

        if snow_list[i][0] < 0:
            snow_list[i][0] = width
        if snow_list1[i][0] < 0:
            snow_list1[i][0] = width
        if snow_list2[i][0] < 0:
            snow_list2[i][0] = width
        if snow_list3[i][0] < 0:
            snow_list3[i][0] = width

    textsurface = myfont.render('Happy New Year!', True, [random.randint(150, 255)]*3)
    screen.blit(textsurface, (355, 315))

    pygame.display.flip()
    clock.tick(fps)
 
